from UnaryExpression import UnaryExpression

class NegativeExpression(UnaryExpression):
    def __init__(self, value):
        self.value = value
    def solve(self):
        return -self.value

