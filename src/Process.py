from parser import Parser
from Expression.BinaryExpression.AddExpression import AddExpression
from Expression.BinaryExpression.SubExpression import SubExpression
from Expression.BinaryExpression.MulExpression import MulExpression
from Expression.BinaryExpression.DivExpression import DivExpression

class Process:
    def __init__(self, expr):
        self.__result = self.calculate(expr)
    
    def result(self):
        return self.__result[0].solve()

    def calculate(self, expr):
        if len(expr) == 3:
            if expr[1] == '+':
                return [AddExpression(expr[0], expr[2])]
            if expr[1] == '-':
                return [SubExpression(expr[0], expr[2])]
            if expr[1] == '*':
                return [MulExpression(expr[0], expr[2])]
            if expr[1] == '/':
                return [DivExpression(expr[0], expr[2])]
        
        if '^' in expr or 'v' in expr:
            for i in range(len(expr)):
                if expr[i] == '^' or expr[i] == 'v':
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
            if ")" not in expr:
                return self.calculate(expr)
            else:
                raise Exception("You are missing a closing bracket")
        
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
            return examine(expr[:lpr] + examine(expr[lpr+1:rpr]) + expr[rpr+1:])