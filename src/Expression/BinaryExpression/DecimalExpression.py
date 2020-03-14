from .BinaryExpression import BinaryExpression
from ..UnaryExpression.TerminalExpression import TerminalExpression
import sys
import math

class DecimalExpression(BinaryExpression):
    def __init__(self, left_expression, right_expression):
        super().__init__(left_expression, right_expression)
    def solve(self):
        return (self.left_expression.solve() + (self.right_expression.solve() / math.pow(10, len(str(self.right_expression.solve())))))

A = DecimalExpression(TerminalExpression(15),TerminalExpression(1))
print(A.solve())