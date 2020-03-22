import unittest
from ..code.Expression.UnaryExpression.TerminalExpression import TerminalExpression
from ..code.Process.Parser import Parser

class TestParser(unittest.TestCase):
    
    def test_parser_unary(self):
        string = '2'
        self.assertEqual (
            Parser(string).expression(),
            [
                TerminalExpression(2)
            ]
        )
    
    def test_parser_binary(self):
        string = '2+2'
        self.assertEqual (
            Parser(string).expression(),
            [
                TerminalExpression(2),
                '+',
                TerminalExpression(2)
            ]
        )
    
    def test_parser_nary(self):
        string = '2+2+2+2+2'
        self.assertEqual (
            Parser(string).expression(),
            [
                TerminalExpression(2),
                '+',
                TerminalExpression(2),
                '+',
                TerminalExpression(2),
                '+',
                TerminalExpression(2),
                '+',
                TerminalExpression(2)
            ]
        )
    
    def test_parser_bracket_unary(self):
        string = '(2)'
        self.assertEqual (
            Parser(string).expression(),
            [
                '(',
                TerminalExpression(2),
                ')'
            ]
        )
    
    def test_parser_bracket_binary(self):
        string = '(2+2)'
        self.assertEqual (
            Parser(string).expression(),
            [
                '(',
                TerminalExpression(2),
                '+',
                TerminalExpression(2),
                ')'
            ]
        )
    
    def test_parser_bracket_nary(self):
        string = '(2+2+2+2+2)'
        self.assertEqual (
            Parser(string).expression(),
            [
                '(',
                TerminalExpression(2),
                '+',
                TerminalExpression(2),
                '+',
                TerminalExpression(2),
                '+',
                TerminalExpression(2),
                '+',
                TerminalExpression(2),
                ')'
            ]
        )
    
    def test_all_operators(self):
        ops = ['+', '-', '*', '/', '^', 'v']
        
        for op in ops:
            string = '2' + op + '2'
            self.assertEqual (
                Parser(string).expression(),
                [
                    TerminalExpression(2),
                    op,
                    TerminalExpression(2)
                ]
            )
            
        
if __name__ == '__main__': 
    unittest.main() 