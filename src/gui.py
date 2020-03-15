from tkinter import *
from  tkinter import ttk
from button import CustomButton

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
        self.list = []
        self.getButtonToForm()
        
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

    def deleteForm(self):
        # kegunaan : delete semua karakter pada form
        self.expression = ''
        self.form.configure(state='normal')
        self.form.delete('1.0', END)
    
    def getButtonToForm(self):    
        # kegunaan : membuat button kalkulator
        self.list.append(CustomButton('MC', 'light pink'))
        self.list.append(CustomButton('MR', 'light pink'))
        self.list.append(CustomButton("CLEAR",'light coral'))
        self.list.append(CustomButton('^', 'khaki'))
        self.list.append(CustomButton(7))
        self.list.append(CustomButton(8))
        self.list.append(CustomButton(9))
        self.list.append(CustomButton(u"\u221A", 'khaki'))
        self.list.append(CustomButton(4))
        self.list.append(CustomButton(5))
        self.list.append(CustomButton(6))
        self.list.append(CustomButton("/", 'khaki'))
        self.list.append(CustomButton(1))
        self.list.append(CustomButton(2))
        self.list.append(CustomButton(3))
        self.list.append(CustomButton('*', 'khaki'))
        self.list.append(CustomButton(0))
        self.list.append(CustomButton('.'))
        self.list.append(CustomButton('+'))
        self.list.append(CustomButton('-', 'khaki'))
        self.grid_up()
        self.grid_bottom()

    def grid_bottom(self):
        # kegunaan : mengatur grid
        equalButton = CustomButton('=','DarkSeaGreen2').grid(row=6,column=3)
        powerButton = CustomButton('ANS').grid(row=6,column=0)
        openButton = CustomButton(u"\u0028").grid(row=6,column=1)
        closeButton = CustomButton(u"\u0029").grid(row=6,column=2)

    def grid_up(self):
        # kegunaan : mengatur grid
        index=0
        i=1
        while (i<6):
            for j in range(4):
                self.list[index].grid(row=i, column=j)
                index=index+1
            i=i+1

    def onClick(self, _text, push=True, _color = 'ivory'):
        # kegunaan : event-handler button dan memasukannya ke Form satu per satu
        return Button(self.root, text=_text, width=7, height = 2, bg = _color, command = lambda: self.Parse(_text, push))

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
