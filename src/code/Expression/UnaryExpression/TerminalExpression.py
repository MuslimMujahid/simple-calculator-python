from .UnaryExpression import UnaryExpression

class TerminalExpression(UnaryExpression):
    
    ''' value : float '''
    
    def __init__(self, value):
        super().__init__(value)
    
    def __str__(self):
        return self.solve() 
    
    def __eq__(self, other):
        if not isinstance(other, TerminalExpression):
            return NotImplemented
        
        return self.solve() == other.solve()
        
    def solve(self):
        return self.value