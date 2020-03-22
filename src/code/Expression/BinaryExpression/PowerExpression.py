from .BinaryExpression import BinaryExpression
import math

class PowerExpression(BinaryExpression):
    ''' 
    left_expression : TerminalExpression
    right_expression : TerminalExpression
    '''
    
    def __init__(self, left_expression, right_expression):
        super().__init__(left_expression, right_expression)
    
    def __eq__(self, other):
        if not isinstance(other, PowerExpression):
            return NotImplemented
        
        return self.solve() == other.solve()
    
    def solve(self):
        return math.pow(self.left_expression.solve(), self.right_expression.solve())
