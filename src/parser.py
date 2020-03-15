import re, collections

expr = '2^2'    
expr = re.findall('[\d.]+|[)(*-/+^v]', expr)

def examine(expr):
    print(expr)
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

def calc(expr):
    print(expr)
    if len(expr) == 3:
        if expr[1] == '+':
            return [str(float(expr[0]) + float(expr[2]))]
        if expr[1] == '-':
            return [str(float(expr[0]) - float(expr[2]))]
        if expr[1] == '*':
            return [str(float(expr[0]) * float(expr[2]))]
        if expr[1] == '/':
            return [str(float(expr[0]) / float(expr[2]))]
        if expr[1] == '^':
            return [str(float(expr[0])**float(expr[2]))]
        if expr[1] == 'v':
            return [str(float(expr[0])**(1/float(expr[2])))]
    if '^' in expr or 'v' in expr:
        for i in range(len(expr)):
            if expr[i] == '^' or expr[i] == 'v':
                return calc(expr[:i-1] + calc(expr[i-1:i+2]) + expr[i+2:])
    if '/' in expr or '*' in expr:
        for i in range(len(expr)):
            if expr[i] == '*' or expr[i] == '/':
                return calc(expr[:i-1] + calc(expr[i-1:i+2]) + expr[i+2:])
    else:
        for i in range(len(expr)):
            if expr[i] == '+' or expr[i] == '-':
                return calc(calc(expr[:i+2]) + expr[i+2:])

print(examine(expr))