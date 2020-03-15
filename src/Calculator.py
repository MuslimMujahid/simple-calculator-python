from parser2 import Parser
from Expression.BinaryExpression.AddExpression import AddExpression
from Expression.BinaryExpression.SubExpression import SubExpression
from Expression.BinaryExpression.MulExpression import MulExpression
from Expression.BinaryExpression.DivExpression import DivExpression

class Calculator:
    def __init__(self, expr):
        if(isinstance(expr, str)):
            self.expr = Parser(expr).getExpression()
        elif(isinstance(expr, list)):
            self.expr = expr
    
    def printInfo(self):
        for expression in self.expr:
            print(expression)

    def getResult(self, expr = None):
        if(expr == None):
            expr = self.expr
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
                    return self.getResult(expr[:i-1] + Calculator(expr[i-1:i+2]).getResult() + expr[i+2:])
        
        if '/' in expr or '*' in expr:
            for i in range(len(expr)):
                if expr[i] == '*' or expr[i] == '/':
                    return  self.getResult(expr[:i-1] + Calculator(expr[i-1:i+2]).getResult() + expr[i+2:])
        
        else:
            for i in range(len(expr)):
                if expr[i] == '+' or expr[i] == '-':
                    return self.getResult(Calculator(expr[:i+2]).getResult() + expr[i+2:])

    
    def examine(self):
        if '(' not in self.expr:
            if ")" not in self.expr:
                return self.getResult()
            else:
                raise Exception("You are missing a closing bracket")
        
        else:
            lpr = 0
            rpr = 0
            lpr_count = 0
            for i in range(len(self.expr)):
                if expr[i] == '(':
                    if lpr_count == 0:
                        lpr = i
                    lpr_count += 1
                if expr[i] == ')':
                    if lpr_count == 1:
                        rpr = i
                        break
                    lpr_count -= 1
            return examine(expr[:lpr] + examine(self.expr[lpr+1:rpr]) + self.expr[rpr+1:])
        

a = Calculator("5-2*3")
print(a.getResult())