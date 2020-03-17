from Parser import Parser
from Expression.BinaryExpression.AddExpression import AddExpression
from Expression.BinaryExpression.SubExpression import SubExpression
from Expression.BinaryExpression.MulExpression import MulExpression
from Expression.BinaryExpression.DivExpression import DivExpression
from Expression.BinaryExpression.PowerExpression import PowerExpression
from Expression.UnaryExpression.NegativeExpression import NegativeExpression
from Expression.UnaryExpression.SqrtExpression import SqrtExpression

class Process:
    def __init__(self, expr):
        self.__parser = Parser(expr)
        self.__result = self.examine(self.__parser.expression())
    
    def result(self):
        return self.__result[0].solve()

    def calculate(self, expr):
        if len(expr) == 1:
            return expr
        if len(expr) == 2:
            if expr[0] == '-':
                return [NegativeExpression(expr[1])]
            if expr[0] == 'v':
                return [SqrtExpression(expr[1])]
        if len(expr) == 3:
            if expr[1] == '+':
                return [AddExpression(expr[0], expr[2])]
            if expr[1] == '-':
                return [SubExpression(expr[0], expr[2])]
            if expr[1] == '*':
                return [MulExpression(expr[0], expr[2])]
            if expr[1] == '/':
                return [DivExpression(expr[0], expr[2])]
            if expr[1] == '^':
                return [PowerExpression(expr[0], expr[2])]
        
        if 'v' in expr:
            for i in range(len(expr)):
                if expr[i] == 'v':
                    return self.calculate(expr[:i] + self.calculate(expr[i:i+2]) + expr[i+2:])
            
        if '^' in expr:
            for i in range(len(expr)):
                if expr[i] == '^':
                    return self.calculate(expr[:i-1] + self.calculate(expr[i-1:i+2]) + expr[i+2:])
        
        if '/' in expr or '*' in expr:
            for i in range(len(expr)):
                if expr[i] == '*' or expr[i] == '/':
                    return  self.calculate(expr[:i-1] + self.calculate(expr[i-1:i+2]) + expr[i+2:])
        
        else:
            for i in range(len(expr)):
                if expr[i] == '+' or expr[i] == '-':
                    return self.calculate(self.calculate(expr[:i+2]) + expr[i+2:])

    
    def examine(self, expr):
        if '(' not in expr:
            return self.calculate(expr)
        else:
            lpr = 0
            rpr = 0
            lpr_count = 0
            for i in range(len(expr)):
                if expr[i] == '(':
                    if lpr_count == 0:
                        lpr = i
                    lpr_count += 1
                if expr[i] == ')':
                    if lpr_count == 1:
                        rpr = i
                        break
                    lpr_count -= 1
            return self.examine(expr[:lpr] + self.examine(expr[lpr+1:rpr]) + expr[rpr+1:])