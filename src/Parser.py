from Expression.UnaryExpression.TerminalExpression import TerminalExpression
from Expression.UnaryExpression.NegativeExpression import NegativeExpression
from Expression.BinaryExpression.AddExpression import AddExpression
from Expression.BinaryExpression.SubExpression import SubExpression
from Expression.BinaryExpression.MulExpression import MulExpression
from Expression.BinaryExpression.DivExpression import DivExpression
from Expression.BinaryExpression.PowerExpression import PowerExpression
from Expression.BinaryExpression.SqrtExpression import SqrtExpression
import re, collections

class Parser:
    '''
    Class ini berfungsi untuk melakukan parse
    dari ekspresi yang diterima dalam bentuk string
    kedalam list yang terpisah.
    
    contoh : 
    '2-4*(5+2)/4' 
    akan diubah menjadi
    ['2', '-', '*', '(', '5', '+', '2', ')', '/', '4']
    
    string : Ekspresi dalam bentuk string
    self.__expr : List berisi operan dan operator yang
                  telah dipisahkan dari string 
    '''
    def __init__(self, string):
        string = re.findall('[\d.]+|[)(*-/+^v]', string)
        
        # Mengubah tiap operan menjadi TerminalExpression
        # dan jika diawali tanda '-'  menjadi NegativeExpression
        try:
            if string[0] == '-':
                string = [NegativeExpression(TerminalExpression(string[1]))] + string[2:]     
            for i in range(len(string)):
                if string[i].isnumeric():
                    string[i] = TerminalExpression(string[i])
            self.__expr = string                

        except IndexError as IE:
            raise Exception("The expression at the end of operation is false")
    
    def expression(self):
        return self.__expr