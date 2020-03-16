from tkinter import *
from  tkinter import ttk
from Parser import Parser
from Process import Process
from gui import GUI
import queue

class Calculator(GUI):
    '''
    Class ini mengatur memegang akses keseluruh
    komponen pembangun aplikasi

    root : objek Tk()
    self.__memory : Queue untuk menyimpan hasil perhitungan
    self.__last_answer : Untuk menyimpan jawaban terakhir
    '''
    def __init__ (self, root):

        # Inisialisasi GUI
        super().__init__(root)
        
        # Inisialisasi sistem
        self.__memory = queue.LifoQueue(maxsize=3)
        self.__last_answer = False
        self.__last_input = ''
        
        # Loop
        self.root.mainloop()
    
    def pushToForm(self, exp_form, newline=False):
        # kegunaan : memasukan karakter satu per satu
        self.form.configure(state='normal')
        self.form.insert(END, exp_form)
        self.display += str(exp_form)
        self.form.configure(state ='disabled')
        
    def deleteForm(self):
        self.display = ''
        self.form.configure(state='normal')
        self.form.delete('1.0', END)
    
    def controller(self, getExpr, push=True):
        # kegunaan : memproses parsing dari Form GUI
        if (push != None):
            print(getExpr)
            self.pushToForm(getExpr)
        else:   
            if (getExpr == '='): 
                # if (u"\u221A" in self.expression):
                #     self.expression = self.parseExpAkar(self.expression)
                # if ("^" in self.expression):
                #     self.expression = self.expression.replace("^", "**")
                # if ("ans" in self.expression):
                    # self.expression = self.expression.replace("ans", str(self.__last_answer))
                self.__last_answer = Process(self.display)
                print(self.__last_answer.result())
                self.deleteForm()
                self.pushToForm(self.__last_answer.result(), newline=True)
            elif getExpr == "CLEAR":
                self.deleteForm()
            elif getExpr == "MC":
                self.history.append(self.ans)
            elif getExpr == "MR":
                self.pushToForm(self.history.pop(), newline=True)