from tkinter import *
from  tkinter import ttk

class GUI:
    def __init__(self, root):
        root.title("Tubes Kalkulator")
        self.root = root
        self.list = []
        self.history = []
        self.ans = None
        self.expression = ''
        self.getButtonToScreen()
        
        self.screen = Text(root, state='disabled', width=30, height=2,background="white", foreground="black")
        self.screen.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
        self.screen.configure(state='normal')
   
    def pushToScreen(self, exp_form, newline=False):
        self.screen.configure(state='normal')
        self.screen.insert(END, exp_form)
        self.expression += str(exp_form)
        self.screen.configure(state ='disabled')

    def deleteScreen(self):
        self.expression = ''
        self.screen.configure(state='normal')
        self.screen.delete('1.0', END)
    
    def getButtonToScreen(self):    
        self.list.append(self.onClick(u"\u221A"))
        self.list.append(self.onClick('MC',None))
        self.list.append(self.onClick('MR',None))
        self.list.append(self.onClick('ans'))
        self.list.append(self.onClick(7))
        self.list.append(self.onClick(8))
        self.list.append(self.onClick(9))
        self.list.append(self.onClick("clear",None))
        self.list.append(self.onClick(4))
        self.list.append(self.onClick(5))
        self.list.append(self.onClick(6))
        self.list.append(self.onClick(u"\u00F7"))
        self.list.append(self.onClick(1))
        self.list.append(self.onClick(2))
        self.list.append(self.onClick(3))
        self.list.append(self.onClick('*'))
        self.list.append(self.onClick(0))
        self.list.append(self.onClick('.'))
        self.list.append(self.onClick('+'))
        self.list.append(self.onClick('-'))
        self.grid_up()
        self.grid_bottom()

    def grid_bottom(self):
        equalButton = self.onClick('=',None,9).grid(row=6,column=3,columnspan=1)
        openButton = self.onClick(u"\u0028").grid(row=6,column=1,columnspan=1)
        closeButton = self.onClick(u"\u0029").grid(row=6,column=2,columnspan=1)

    def grid_up(self):
        index=0
        i=1
        while (i<6):
            for j in range(4):
                self.list[index].grid(row=i, column=j)
                index=index+1
            i=i+1

    def onClick(self, _text, push=True,width=9):
        return ttk.Button(self.root, text=_text, command = lambda: self.Parse(_text, push), width=width)

    def parseExpAkar(self,b):
        akar = u"\u221A"
        newExp = ''
        i = 0
        while (i<len(b)):
            if (b[i] == akar):
                j = i+1
                while (j<len(b) and b[j] not in '+-/*'):
                    newExp+=b[j]
                    j+=1
                    i+=1
                newExp += '**0.5' 
            else:   
                newExp+=b[i]
            i+=1
        return newExp

    def Parse(self, getExpr, push=True):
        if (push != None):
            self.pushToScreen(getExpr)
        else:   
            if (getExpr == '='): 
                self.expression = self.expression.replace(u"\u00F7", '/')
                if (u"\u221A" in self.expression):
                    self.expression = self.parseExpAkar(self.expression)
                if ("ans" in self.expression):
                    self.expression = self.expression.replace("ans", str(self.ans))
                print(self.expression)
                result = eval(self.expression)
                self.ans = result
                self.deleteScreen()
                self.pushToScreen(result, newline=True)
            elif getExpr == "clear":
                self.deleteScreen()
            elif getExpr == "MC":
                self.history.append(self.ans)
            elif getExpr == "MR":
                self.pushToScreen(self.history.pop(), newline=True)

root = Tk()
my_gui = GUI(root)
root.mainloop()
