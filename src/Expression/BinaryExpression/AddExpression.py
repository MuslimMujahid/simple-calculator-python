from .BinaryExpression import BinaryExpression

class AddExpression(BinaryExpression):
    ''' 
    left_expression : TerminalExpression
    right_expression : TerminalExpression
    '''
    def __init__(self, left_expression, right_expression):
        super().__init__(left_expression, right_expression)
    def solve(self):
        return (float(self.left_expression.solve()) + float(self.right_expression.solve()))
