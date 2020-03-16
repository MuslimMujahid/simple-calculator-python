from tkinter import *
from  tkinter import ttk
from Buttons import Buttons

class GUI:
    def __init__(self, root):
        self.root = root
        root.configure(background = 'black')
        root.title("Calculator")
        # Constructor queue history, tombol answer, dan parsing expression
        #self.history = []
        #self.ans = None
        # self.expression = ''
        

        # Push Grid Button
        self.Buttons = Buttons(_command = self.controller)
        
        # Form Ekspresi
        self.form = Text(root, state='disabled', width=30, height=4,background= "black", foreground="white")
        self.form.grid(row=0,column=0,columnspan=4,padx=5,pady=20)
        self.form.configure(state='normal')
   
    def pushToForm(self, exp_form, newline=False):
        # kegunaan : memasukan karakter satu per satu
        self.form.configure(state='normal')
        self.form.insert(END, exp_form)
        self.expression += str(exp_form)
        self.form.configure(state ='disabled')

    def root(self):
        return self.root

    def controller(self, getExpr, push=True):
        pass
    # def parseExpAkar(self, express):
    #     # kegunaan : membuat ekspresi akar menjadi ekspresi python
    #     akar = u"\u221A"
    #     newExp = ''
    #     i = 0
    #     while (i<len(express)):
    #         if (express[i] == akar):
    #             j = i+1
    #             while (j<len(express) and express[j] not in '+-/*'):
    #                 newExp+=express[j]
    #                 j+=1
    #                 i+=1
    #             newExp += '**0.5' 
    #         else:   
    #             newExp+=express[i]
    #         i+=1
    #     return newExp

    # def Parse(self, getExpr, push=True):
    #     # kegunaan : memproses parsing dari Form GUI
    #     if (push != None):
    #         self.pushToForm(getExpr)
    #     else:   
    #         if (getExpr == '='): 
    #             if (u"\u221A" in self.expression):
    #                 self.expression = self.parseExpAkar(self.expression)
    #             if ("^" in self.expression):
    #                 self.expression = self.expression.replace("^", "**")
    #             if ("ans" in self.expression):
    #                 self.expression = self.expression.replace("ans", str(self.ans))
    #             print(self.expression)
    #             result = eval(self.expression)
    #             self.ans = result
    #             self.deleteForm()
    #             self.pushToForm(result, newline=True)
    #         elif getExpr == "clear":
    #             self.deleteForm()
    #         elif getExpr == "MC":
    #             self.history.append(self.ans)
    #         elif getExpr == "MR":
    #             self.pushToForm(self.history.pop(), newline=True)

# root = Tk()
# create = GUI(root)
# root.mainloop()
