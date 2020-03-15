from Expression.UnaryExpression.TerminalExpression import TerminalExpression
from Expression.BinaryExpression.AddExpression import AddExpression
from Expression.BinaryExpression.SubExpression import SubExpression
from Expression.BinaryExpression.MulExpression import MulExpression
from Expression.BinaryExpression.DivExpression import DivExpression
import re, collections

expr = '(2+4*(5-2)-4)/2/(2/2)'    
expr = re.findall('[\d.]+|[)(*-/+]', expr)

def toClass(expr):
    for i in range(len(expr)):
        if expr[i].isnumeric():
            expr[i] = TerminalExpression(expr[i])
    return expr

expr = toClass(expr)

def calc(expr):
    if len(expr) == 3:
        if expr[1] == '+':
            return [AddExpression(expr[0], expr[2])]
        if expr[1] == '-':
            return [SubExpression(expr[0], expr[2])]
        if expr[1] == '*':
            return [MulExpression(expr[0], expr[2])]
        if expr[1] == '/':
            return [DivExpression(expr[0], expr[2])]
    if '/' in expr or '*' in expr:
        for i in range(len(expr)):
            if expr[i] == '*' or expr[i] == '/':
                return calc(expr[:i-1] + calc(expr[i-1:i+2]) + expr[i+2:])
    else:
        for i in range(len(expr)):
            if expr[i] == '+' or expr[i] == '-':
                return calc(calc(expr[:i+2]) + expr[i+2:])

def examine(expr):
    if '(' not in expr:
        return calc(expr)
    else:
        lpr = 0
        rpr = 0
        lpr_count = 0
        for i in range(len(expr)):
            if expr[i] == '(':
                if lpr_count == 0:
                    lpr = i
                lpr_count += 1
            if expr[i] == ')':
                if lpr_count == 1:
                    rpr = i
                    break
                lpr_count -= 1
        return examine(expr[:lpr] + examine(expr[lpr+1:rpr]) + expr[rpr+1:])

print(examine(expr)[0].solve())