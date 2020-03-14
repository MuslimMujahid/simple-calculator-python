from tkinter import *
from  tkinter import ttk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Python Calculator")
        
        # create screen widget
        self.screen = Text(master, state='disabled', width=30, height=2,background="white", foreground="black")

        # position screen in window
        self.screen.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
        self.screen.configure(state='normal')

        # initialize screen value as empty
        self.equation = ''
        
        # create buttons using method createButton
        b1 =  self.createButton(7)
        b2 = self.createButton(8)
        b3 = self.createButton(9)
        #b4 = self.createButton(u"\u232B",None)
        b4 = self.createButton("erase",None)
        b5 = self.createButton(4)
        b6 = self.createButton(5)
        b7 = self.createButton(6)
        b8 = self.createButton(u"\u00F7")
        b9 = self.createButton(1)
        b10 = self.createButton(2)
        b11 = self.createButton(3)
        b12 = self.createButton('*')
        b13 = self.createButton(0)
        b14 = self.createButton('.')
        b15 = self.createButton('+')
        b16 = self.createButton('-')
        b17 = self.createButton('=',None,9)
        b18 = self.createButton(u"\u221A")
        b19 = self.createButton('MC')
        b20 = self.createButton('MR')
        b21 = self.createButton('ans')
        b22 = self.createButton(u"\u0028")
        b23 = self.createButton(u"\u0029")
        

        # buttons stored in list
        buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21]

        # intialize counter
        count = 0
        # arrange buttons with grid manager
        for row in range(1,5):
            for column in range(4):
                buttons[count].grid(row=row,column=column)
                count += 1
        # arrange last button '=' at the bottom
        buttons[16].grid(row=6,column=0,columnspan=1)
        b22.grid(row=6,column=1,columnspan=1)
        b23.grid(row=6,column=2,columnspan=1)
        i = 17
        k = 0
        while (i<=20 and k<=3):
            buttons[i].grid(row=5,column=k)
            i+=1
            k+=1
        

    def createButton(self,val,write=True,width=9):
        # this function creates a button, and takes one compulsory argument, the value that should be on the button
        return ttk.Button(self.master, text=val,command = lambda: self.click(val,write), width=width)

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
                self.clear_screen()
                self.insert_screen(answer,newline=True)
            elif text == "erase":
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
my_gui = Calculator(root)
root.mainloop()
