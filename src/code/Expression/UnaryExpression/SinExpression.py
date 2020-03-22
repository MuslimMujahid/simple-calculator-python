from .UnaryExpression import UnaryExpression
import math

class SinExpression(UnaryExpression):
    
    ''' value : TerminalExpression '''
    
    def __init__(self, value):
        super().__init__(value.solve())
    
    def __eq__(self, other):
        if not isinstance(other, SinExpression):
            return NotImplemented
        
        return self.solve() == other.solve()
    
    def solve(self):
        return math.sin(self.value)

