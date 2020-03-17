from ..BaseExpression.Expression import Expression
from abc import ABC, abstractmethod

class UnaryExpression(Expression):
    def __init__(self, value):
        self.value = float(value)
        
    @abstractmethod
    def solve(self):
        pass
