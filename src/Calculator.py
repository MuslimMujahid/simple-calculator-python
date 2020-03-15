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

    def getResult(self):
        if len(self.expr) == 3:
            if self.expr[1] == '+':
                return AddExpression(self.expr[0], self.expr[2]).solve()
            if self.expr[1] == '-':
                return SubExpression(self.expr[0], self.expr[2]).solve()
            if self.expr[1] == '*':
                return MulExpression(self.expr[0], self.expr[2]).solve()
            if self.expr[1] == '/':
                return DivExpression(self.expr[0], self.expr[2]).solve()
        
        if '/' in self.expr or '*' in self.expr:
            for i in range(len(self.expr)):
                expmiddle = self.expr[i-1:i+2]
                expright  = self.expr[i-1:i+2]
                expleft   = self.expr[:i-1]
                if self.expr[i] == '*' or self.expr[i] == '/':
                    return  Calculator(expleft).getResult() + Calculator(expmiddle).getResult() + Calculator(expright).getResult()
        
        else:
            for i in range(len(self.expr)):
                if self.expr[i] == '+' or self.expr[i] == '-':
                    expleft  = self.expr[:i+2]
                    expright = self.expr[i+2:]
                    return Calculator(expleft).getResult() + Calculator(expright).getResult()

    
    def examine(self):
        if '(' not in expr:
            if ")" not in expr:
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


a = Calculator("5+2+3")
a.printInfo()
print(a.getResult())