from .BinaryExpression import BinaryExpression

class SubExpression(BinaryExpression):
    ''' 
    left_expression : TerminalExpression
    right_expression : TerminalExpression
    '''
    def __init__(self, left_expression, right_expression):
        super().__init__(left_expression, right_expression)
    def solve(self):
        return (self.left_expression.solve() - self.right_expression.solve())
