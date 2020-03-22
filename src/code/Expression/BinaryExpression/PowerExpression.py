from .BinaryExpression import BinaryExpression
import math

class PowerExpression(BinaryExpression):
    ''' 
    left_expression : TerminalExpression
    right_expression : TerminalExpression
    '''
    
    def __init__(self, left_expression, right_expression):
        super().__init__(left_expression, right_expression)
    
    def solve(self):
        return math.pow(self.left_expression.solve(), self.right_expression.solve())
