from Expression.UnaryExpression.TerminalExpression import TerminalExpression
from Expression.UnaryExpression.NegativeExpression import NegativeExpression

import re, collections

# expr = '(2+4*(-5-2)-4)/2/(2/2)'
# added = 0
# expr = re.findall('[\d.]+|[)(*-/+]', expr)
# i = 0

class Parser:
    def __init__(self, string):
        self.expr = []
        i = 0
        try:
            while(i < len(string)):
                if string[i].isnumeric():
                    self.expr.append(TerminalExpression(int(string[i])))
                
                elif string[i] == "-":
                    if(i == 0):
                        i += 1
                        self.expr.append(NegativeExpression(int(string[i])))
                    elif(string[i-1] == "(" or string[i-1] == ")"):
                        i += 1
                        self.expr.append(NegativeExpression(int(string[i])))
                    else:
                        int(string[i-1])
                        self.expr.append('-')
                
                elif string[i] in "+*/()":
                    self.expr.append(string[i])
                
                i += 1
        except IndexError as IE:
            raise Exception("The expression at the end of operation is false")

    #debugging method
    def printInfo(self):
        for string in self.expr:
            print(string)

    def getExpression(self):
        return self.expr
