from ..BaseExpression.Expression import Expression
from abc import ABC, abstractmethod

class BinaryExpression(Expression):
    def __init__(self, left_expression, right_expression):
        self.left_expression  = left_expression
        self.right_expression = right_expression
    @abstractmethod
    def solve(self):
        pass