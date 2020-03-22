from .UnaryExpression import UnaryExpression

class TerminalExpression(UnaryExpression):
    
    ''' value : float '''
    
    def __init__(self, value):
        super().__init__(value)
        
    def solve(self):
        return self.value