from Expression.UnaryExpression.TerminalExpression import TerminalExpression
from Expression.BinaryExpression.AddExpression import AddExpression
from Expression.BinaryExpression.SubExpression import SubExpression
from Expression.BinaryExpression.MulExpression import MulExpression
from Expression.BinaryExpression.DivExpression import DivExpression
from Expression.BinaryExpression.PowerExpression import PowerExpression
from Expression.BinaryExpression.SqrtExpression import SqrtExpression
import re, collections

expr = '(4/2^2)v3'    

class Parser:
    def __init__(self, string):
        self.expr = []
        charList = re.findall('[\d.]+|[)(*-/+^v]', string)
        i = 0
        try:
            while(i < len(charList)):
                if charList[i].isnumeric():
                    self.expr.append(TerminalExpression(int(charList[i])))
                elif charList[i] == "-":
                    if(i == 0):
                        i += 1
                        self.expr.append(NegativeExpression(int(charList[i])))
                    elif(charList[i-1] == "(" or charList[i-1] == ")"):
                        i += 1
                        self.expr.append(NegativeExpression(int(charList[i])))
                    else:
                        int(charList[i-1])
                        self.expr.append('-')
                else:
                    self.expr.append(charList[i])
                i += 1

        except IndexError as IE:
            raise Exception("The expression at the end of operation is false")

    def getExpression(self):
        return self.expr
    #debugging method
    def printInfo(self):
        for charList in self.expr:
            print(charList)

# expr = '(2+4*(-5-2)-4)/2/(2/2)'
# added = 0
# expr = re.findall('[\d.]+|[)(*-/+]', expr)
# i = 0