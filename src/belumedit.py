from tkinter import *
from  tkinter import ttk

class GUI:
    def __init__(self, root):
        root.title("Tubes Kalkulator")
        # Constructor queue history, tombol answer, dan parsing expression
        self.history = []
        self.ans = None
        self.expression = ''
        self.root = root

        # Push Grid Button
        self.list = []
        self.getButtonToForm()
        
        # Form Ekspresi
        self.form = Text(root, state='disabled', width=30, height=2,background="white", foreground="black")
        self.form.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
        self.form.configure(state='normal')
   
    def pushToForm(self, exp_form, newline=False):
        # kegunaan : memasukan karakter satu per satu
        self.form.configure(state='normal')
        self.form.insert(END, exp_form)
        self.expression += str(exp_form)
        self.form.configure(state ='disabled')

    def deleteForm(self):
        # kegunaan : delete semua karakter pada form
        self.expression = ''
        self.form.configure(state='normal')
        self.form.delete('1.0', END)
    
    def getButtonToForm(self):    
        # kegunaan : membuat button kalkulator
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
        self.list.append(self.onClick("/"))
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
        # kegunaan : mengatur grid
        equalButton = self.onClick('=',None,9).grid(row=6,column=3,columnspan=1)
        openButton = self.onClick(u"\u0028").grid(row=6,column=1,columnspan=1)
        closeButton = self.onClick(u"\u0029").grid(row=6,column=2,columnspan=1)

    def grid_up(self):
        # kegunaan : mengatur grid
        index=0
        i=1
        while (i<6):
            for j in range(4):
                self.list[index].grid(row=i, column=j)
                index=index+1
            i=i+1

    def onClick(self, _text, push=True,width=9):
        # kegunaan : event-handler button dan memasukannya ke Form satu per satu
        return ttk.Button(self.root, text=_text, command = lambda: self.Parse(_text, push), width=9)

    def parseExpAkar(self, express):
        # kegunaan : membuat ekspresi akar menjadi ekspresi python
        akar = u"\u221A"
        newExp = ''
        i = 0
        while (i<len(express)):
            if (express[i] == akar):
                j = i+1
                while (j<len(express) and express[j] not in '+-/*'):
                    newExp+=express[j]
                    j+=1
                    i+=1
                newExp += '**0.5' 
            else:   
                newExp+=express[i]
            i+=1
        return newExp

    def Parse(self, getExpr, push=True):
        # kegunaan : memproses parsing dari Form GUI
        if (push != None):
            self.pushToForm(getExpr)
        else:   
            if (getExpr == '='): 
                if (u"\u221A" in self.expression):
                    self.expression = self.parseExpAkar(self.expression)
                if ("ans" in self.expression):
                    self.expression = self.expression.replace("ans", str(self.ans))
                print(self.expression)
                result = eval(self.expression)
                self.ans = result
                self.deleteForm()
                self.pushToForm(result, newline=True)
            elif getExpr == "clear":
                self.deleteForm()
            elif getExpr == "MC":
                self.history.append(self.ans)
            elif getExpr == "MR":
                self.pushToForm(self.history.pop(), newline=True)

root = Tk()
create = GUI(root)
root.mainloop()
