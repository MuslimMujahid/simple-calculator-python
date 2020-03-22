from .BinaryExpression import BinaryExpression

class ModExpression(BinaryExpression):
    
    ''' 
    
    left_expression : TerminalExpression
    right_expression : TerminalExpression
    
    '''
    
    def __init__(self, left_expression, right_expression):
        super().__init__(left_expression, right_expression)
    
    def __str__(self):
        return self.solve() 
    
    def __eq__(self, other):
        if not isinstance(other, ModExpression):
            return NotImplemented
        
        return self.solve() == other.solve()
    
    def solve(self):
        return (self.left_expression.solve() % self.right_expression.solve())
