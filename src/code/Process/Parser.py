from ..Expression.UnaryExpression.TerminalExpression import TerminalExpression
from ..Expression.UnaryExpression.NegativeExpression import NegativeExpression
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
    
    Type
    self.__expr : list
    
    Fungsi
    self.__expr : menyimpan hasil parsing 
    
    '''
    
    def __init__(self, string):
        string = re.findall('[cos|sin|tan]+|[\d.]+|[)(*-/+^v%]', string)

        # Mengubah tiap operan menjadi TerminalExpression
        # dan jika diawali tanda '-'  menjadi NegativeExpression
        try:
            if string[0] == '-':
                string = [NegativeExpression(TerminalExpression(string[1]))] + string[2:]     
            for i in range(len(string)):
                if string[i].isnumeric() or '.' in string[i]:
                    string[i] = TerminalExpression(string[i])
                    
            self.__expr = string                

        except IndexError as IE:
            raise Exception("The expression at the end of operation is false")
            
    def expression(self):
        return self.__expr