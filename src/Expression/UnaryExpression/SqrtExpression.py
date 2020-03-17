from .UnaryExpression import UnaryExpression
import math

class SqrtExpression(UnaryExpression):
    ''' 
    value : TerminalExpression
    '''
    def __init__(self, value):
        super().__init__(value.solve())
    def solve(self):
        return math.sqrt(self.value)
