from .UnaryExpression import UnaryExpression
import math

class CosExpression(UnaryExpression):
    
    ''' value : TerminalExpression '''
    
    def __init__(self, value):
        super().__init__(value.solve())
    
    def __str__(self):
        return self.solve() 
    
    def __eq__(self, other):
        if not isinstance(other, CosExpression):
            return NotImplemented
        
        return self.solve() == other.solve()
    
    def solve(self):
        return math.cos(math.radians(self.value))

