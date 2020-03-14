from ..BaseExpression.Expression import Expression
from abc import ABC, abstractmethod

class UnaryExpression(ABC):
    def __init__(self, value):
        self.value = value
    @abstractmethod
    def solve(self):
        pass
