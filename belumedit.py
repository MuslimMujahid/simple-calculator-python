from tkinter import *
from  tkinter import ttk

class GUI:
    def __init__(self, root):
        root.title("Tubes Kalkulator")
        
        self.root = root
        self.list = []
        self.screen = Text(root, state='disabled', width=30, height=2,background="white", foreground="black")
        self.screen.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
        self.screen.configure(state='normal')

        self.equation = ''

        self.list.append(self.onClick(u"\u221A"))
        self.list.append(self.onClick('MC'))
        self.list.append(self.onClick('MR'))
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

    def grid_up(self):
        index=0
        i=1
        while (i<6):
            for j in range(4):
                self.list[index].grid(row=i, column=j)
                index=index+1
            i=i+1

    def grid_bottom(self):
        equalButton = self.onClick('=',None,9).grid(row=6,column=3,columnspan=1)
        openButton = self.onClick(u"\u0028").grid(row=6,column=1,columnspan=1)
        closeButton = self.onClick(u"\u0029").grid(row=6,column=2,columnspan=1)

        
    def onClick(self,val,write=True,width=9):
        return ttk.Button(self.root, text=val,command = lambda: self.click(val,write), width=width)

    def parseExpAkar(self,b):
        k = u"\u221A"
        newExp=''
        i = 0
        while (i<len(b)):
            if (b[i] == k):
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

    def click(self,text,write):
        if write == None:
            if text == '=' and self.equation: 
                # self.equation = re.sub(u"\u00F7", '/', self.equation)
                self.equation = self.equation.replace(u"\u00F7", '/')
                if (u"\u221A" in self.equation):
                    self.equation = self.parseExpAkar(self.equation)
                print(self.equation)
                answer = str(eval(self.equation))
                self.clear_screen()
                self.insert_screen(answer,newline=True)
            elif text == "clear":
                self.clear_screen()
        else:   
            self.insert_screen(text)
        

    def clear_screen(self):
        self.equation = ''
        self.screen.configure(state='normal')
        self.screen.delete('1.0', END)

    def insert_screen(self, value,newline=False):
        self.screen.configure(state='normal')
        self.screen.insert(END,value)
        self.equation += str(value)
        self.screen.configure(state ='disabled')

root = Tk()
my_gui = GUI(root)
root.mainloop()
