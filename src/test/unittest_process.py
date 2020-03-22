import unittest
from ..code.Expression.UnaryExpression.TerminalExpression import TerminalExpression
from ..code.Process.Process import Process

class TestProcess(unittest.TestCase):
    
    def test_calc_unary(self):
        string = '2+3'
        self.assertEqual(Process(string).result(), 5)
    
    def test_calc_allops(self):
        questions = {
            '2+3': 5, 
            '2-3': -1, 
            '2*3': 6, 
            '6/3': 2, 
            '2^3': 8, 
            'v9': 3
        }

        for k, v in questions.items():
            self.assertEqual(Process(k).result(), v)
    
    def test_calc_allops_bracket(self):
        questions = {
            '(2+3)': 5, 
            '(2-3)': -1, 
            '(2*3)': 6, 
            '(6/3)': 2, 
            '(2^3)': 8, 
            '(v9)': 3
        }

        for k, v in questions.items():
            self.assertEqual(Process(k).result(), v)
        
    def test_calc_complex(self):
        questions = {
            '(2^2)+(9/3)+2+2': 11,
            '2+3+4+5*0+1': 10,
            '2+(2+(5+7*3-2)/4)': 10
        }
        
        for k, v in questions.items():
            self.assertEqual(Process(k).result(), v)
        
if __name__ == '__main__': 
    unittest.main() 