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
        self.__last_input = '' # Menyimpan push terakhir ke form
        self.__last_command = '' # Menympan command terakhir
        
        # Loop
        self.root.mainloop()
    
    def pushToForm(self, exp_form, newline=False):
        # Menampilkan exp_form ke layar
        self.form.configure(state='normal')
        self.form.insert(END, exp_form)
        self.display += str(exp_form)
        self.form.configure(state ='disabled')
        
    def deleteForm(self):
        # Membersihkan layar
        self.display = ''
        self.form.configure(state='normal')
        self.form.delete('1.0', END)
    
    def controller(self, getExpr, push=True):
        # Controller tombol kalkulator
        if (push != None):
            print(getExpr)
            self.pushToForm(getExpr)
            self.__last_input = getExpr        
        
        else:   
            if (getExpr == '='): 
            
                # Gantikan karakter akar dengan 'v'
                # gantikan ANS dengan jawaban terakhir
                if u"\u221A" in self.display:
                    self.display = self.display.replace(u'\u221A', 'v')
                if "ANS" in self.display:
                    self.display = self.display.replace("ANS", str(self.__last_answer.result()))
            
                self.__last_answer = Process(self.display)
                self.deleteForm()
                self.pushToForm(self.__last_answer.result(), newline=True)
                
                self.__last_input = str(self.__last_answer.result())
            
            elif getExpr == "CLEAR":
                
                # Bersihkan layar
                self.deleteForm()
            
            elif getExpr == "MC":
            
                # Simpan ke memory
                self.__memory.put(self.__last_answer.result())                
            
            elif getExpr == "MR":

                # Hanya memproses jika queue tidak kosong
                if self.__memory.empty():
                    return
                
                # Jika command terakhir adalah MR maka hapus 
                # hasil dari MR sebelumnya dan tampilkan
                # hasil MR yang baru
                if self.__last_command is 'MR':
                    new_display = self.display[:len(self.display)-len(self.__last_input)]
                    self.deleteForm()
                    self.pushToForm(new_display, newline=True)
                
                self.__last_input = str(self.__memory.get())
                self.pushToForm(self.__last_input)
        
        # Simpan command terakhir
        self.__last_command = getExpr
        
                