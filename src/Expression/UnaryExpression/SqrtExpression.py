from .UnaryExpression import UnaryExpression
import math

class SqrtExpression(UnaryExpression):
    def __init__(self, value):
        super().__init__(value)
    def solve(self):
        return math.sqrt(self.value)
