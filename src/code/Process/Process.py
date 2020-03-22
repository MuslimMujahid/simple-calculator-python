from .Parser import Parser
from ..Expression.BaseExpression import Expression
from ..Expression.BinaryExpression import AddExpression
from ..Expression.BinaryExpression import SubExpression
from ..Expression.BinaryExpression import MulExpression
from ..Expression.BinaryExpression import DivExpression
from ..Expression.BinaryExpression import PowerExpression
from ..Expression.BinaryExpression import ModExpression
from ..Expression.UnaryExpression import TerminalExpression
from ..Expression.UnaryExpression import NegativeExpression
from ..Expression.UnaryExpression import SqrtExpression
from ..Expression.UnaryExpression import CosExpression
from ..Expression.UnaryExpression import SinExpression
from ..Expression.UnaryExpression import TanExpression

class Process:
    
    '''
    
    Type
    self.__parser : objek Parser()
    self.__result : float/integer

    Fungsi
    self.__parser : menyimpan hasil parsing
    self.__parser : menyimpan hasil perhitungan
        
    '''
    
    def __init__(self, expr):
        self.__parser = Parser(expr)
        self.__result = self.examine(self.__parser.expression())[0].solve()
        
        if self.__result.is_integer():
            self.__result = int(self.__result)
    
    def result(self):
        return self.__result

    def calculate(self, expr):
        if len(expr) == 1:

            if not isinstance(expr[0], Expression):
                raise Exception(f'Syntax error near {expr[0]}') 
            
            return expr
        
        if len(expr) == 2:
            if (
                not isinstance(expr[1], Expression) or
                expr[0] not in '-vcosintan'
            ):
                raise Exception(f'Syntax error near {expr[1]}')
            
            if expr[0] == '-':
                return [NegativeExpression(expr[1])]
            if expr[0] == 'v':
                return [SqrtExpression(expr[1])]
            if expr[0] == 'cos':
                return [CosExpression(expr[1])]
            if expr[0] == 'sin':
                return [SinExpression(expr[1])]
            if expr[0] == 'tan':
                return [TanExpression(expr[1])]
            
        if len(expr) == 3:
            
            if (
                not isinstance(expr[0], Expression) or
                not isinstance(expr[2], Expression) or
                expr[1] not in '+-*/^%' 
            ):
                 raise Exception(f'Syntax error near {expr[1]}')
            
            if expr[1] == '+':
                return [AddExpression(expr[0], expr[2])]
            if expr[1] == '-':
                return [SubExpression(expr[0], expr[2])]
            if expr[1] == '*':
                return [MulExpression(expr[0], expr[2])]
            if expr[1] == '/':
                return [DivExpression(expr[0], expr[2])]
            if expr[1] == '^':
                return [PowerExpression(expr[0], expr[2])]
            if expr[1] == '%':
                return [ModExpression(expr[0], expr[2])]
        
        
        if 'v' in expr:
            i = expr.index('v')
            return self.calculate(expr[:i] + self.calculate(expr[i:i+2]) + expr[i+2:])
            
        if '^' in expr:
            i = expr.index('^')
            return self.calculate(expr[:i-1] + self.calculate(expr[i-1:i+2]) + expr[i+2:])
        
        if '/' in expr or '*' in expr:
            i = expr.index('/' if '/' in expr else '*')
            return self.calculate(expr[:i-1] + self.calculate(expr[i-1:i+2]) + expr[i+2:])
        
        if 'cos' in expr or 'sin' in expr or 'tan' in expr:
            i = 0
            if 'cos' in expr:
                i = expr.index('cos')
            elif 'sin' in expr:
                i = expr.index('sin')
            else:
                i = expr.index('tan')
            return self.calculate(expr[:i] + self.calculate(expr[i:i+2]) + expr[i+2:])
        
        else:
            i = expr.index('+' if '+' in expr else '-')
            return self.calculate(expr[:i-1] + self.calculate(expr[i-1:i+2]) + expr[i+2:])

    
    def examine(self, expr):
        if '(' not in expr:
            return self.calculate(expr)
        else:
            lpr = 0
            rpr = 0
            lpr_count = 0
            for i in range(len(expr)):
                
                # Cari pasang bracket
                if expr[i] == '(':
                    if lpr_count == 0:
                        lpr = i
                    lpr_count += 1
                if expr[i] == ')':
                    if lpr_count == 1:
                        rpr = i
                        break
                    lpr_count -= 1
                    
                # Kalau loop nya sampai akhir berarti ada bracket yang kurang
                if i == len(expr)-1:
                    raise Exception('You miss a bracket.')
            
            # Lakukan examine tersendiri untuk bagian bracket
            # kemudian examine ulang keseluruhan
            return self.examine(expr[:lpr] + self.examine(expr[lpr+1:rpr]) + expr[rpr+1:])