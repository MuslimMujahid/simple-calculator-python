from .UnaryExpression import UnaryExpression

class NegativeExpression(UnaryExpression):
    '''
    value : TerminalExpression
    '''
    def __init__(self, value):
        self.value = value.value()
    def solve(self):
        return -self.value

