from Expression.UnaryExpression.TerminalExpression import TerminalExpression
from Expression.UnaryExpression.NegativeExpression import NegativeExpression
from Expression.BinaryExpression.AddExpression import AddExpression
from Expression.BinaryExpression.SubExpression import SubExpression
from Expression.BinaryExpression.MulExpression import MulExpression
from Expression.BinaryExpression.DivExpression import DivExpression
from Expression.BinaryExpression.PowerExpression import PowerExpression
from Expression.BinaryExpression.SqrtExpression import SqrtExpression
import re, collections

class Parser:
    def __init__(self, string):
        self.__expr = []
        charList = re.findall('[\d.]+|[)(*-/+^v]', string)
        i = 0
        try:
            while(i < len(charList)):
                if charList[i].isnumeric():
                    self.__expr.append(TerminalExpression(int(charList[i])))
                elif charList[i] == "-":
                    if(i == 0):
                        i += 1
                        self.__expr.append(NegativeExpression(int(charList[i])))
                    elif(charList[i-1] == "(" or charList[i-1] == ")"):
                        i += 1
                        self.__expr.append(NegativeExpression(int(charList[i])))
                    else:
                        int(charList[i-1])
                        self.__expr.append('-')
                else:
                    self.__expr.append(charList[i])
                i += 1

        except IndexError as IE:
            raise Exception("The expression at the end of operation is false")

    def expression(self):
        return self.__expr