from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ..Process.Parser import Parser
from ..Process.Process import Process
from .App import App
import queue
import tkinter.font as font

class Calculator(App):
    
    '''
    
    Class ini memegang akses keseluruh
    komponen pembangun aplikasi

    Type
    self.__memory : queue
    self.__last_answer : float
    self.__display : string
    self.__last_input : string
    self.__last_command : string
    
    Fungsi
    self.__memory : menyimpan hasil perhitungan dalam bentuk antrian
    self.__last_answer : menyimpan jawaban terakhir
    self.__display : menyimpan expresi  
    self.__last_input : menyimpan push terakhir yang dilakukan ke form
    self.__last_command : menyimpan command terakhir yang digunakan user
    
    '''
    
    def __init__ (self):

        # Inisialisasi GUI
        super().__init__()
        self.initRoot()
        self.initForm()        
        # self.root.iconbitmap('icon.ico')
                        
        # Inisialisasi sistem
        self.display = ''
        self.__memory = queue.LifoQueue(maxsize=3)
        self.__last_answer = False
        self.__last_input = ''
        self.__last_command = ''
        
        # Loop
        self.root.mainloop()
        
    
    def initRoot(self):
        self.root.configure(background = '#9e9e9e')
        self.root.title("Calculator")
    
    def initForm(self):
        self.form = Text(
            self.root, 
            state='disabled', 
            width=28, 
            height=4,
            background= "ghostwhite", 
            foreground="black",
            font = font.Font(family='Helvetica', size = 11, weight = 'bold')
        )
        self.form.grid(row=0, column=0, columnspan=4, padx=2, pady=20)
        self.form.configure(state='normal')
    
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
        if push is not None:
            
            if getExpr is 'cos' or getExpr is 'sin' or getExpr is 'tan':
                getExpr += '('
            
            self.pushToForm(getExpr)
            self.__last_input = getExpr        

        else:   
            if (getExpr == '='): 
            
                # Gantikan karakter akar dengan 'v'
                # gantikan ANS dengan jawaban terakhir
                if u"\u221A" in self.display:
                    self.display = self.display.replace(u'\u221A', 'v')
                if "ANS" in self.display:
                    try:
                        self.display = self.display.replace("ANS", str(self.__last_answer.result()))
                    except AttributeError:
                        messagebox.showerror("ANS Error", "Jawaban terakhir masih kosong")
                        return
                try:
                    self.__last_answer = Process(self.display)
                except Exception as error:
                    messagebox.showerror("Syntax Error", error.args[0])
                    return
                
                self.deleteForm()
                self.pushToForm(self.__last_answer.result(), newline=True)
                self.__last_input = str(self.__last_answer.result())
            
            elif getExpr == "CLEAR":
                # Bersihkan layar dan hapus isi memori
                self.deleteForm()
                self.__memory = queue.LifoQueue(maxsize=3)
            
            elif getExpr == "MC":
                if (self.__memory.__sizeof__ == 3):
                    messagebox.showinfo("Memory Error", "Anda tidak bisa melakukan penyimpanan lebih dari 3 kali")
                else:
                    try:
                        # Simpan ke memory
                        self.__memory.put(self.__last_answer.result())
                        self.deleteForm()
                    except AttributeError as attr:
                        messagebox.showinfo("Memory Error", "Anda belum memasukan angka untuk disimpan dalam memori!")
  
            elif getExpr == "MR":

                # Hanya memproses jika queue tidak kosong
                if self.__memory.empty():
                    return
                
                # Jika command terakhir adalah MR maka hapus 
                # hasil dari MR sebelumnya dan tampilkan
                # hasil MR yang baru
                if self.__last_command == 'MR':
                    new_display = self.display[:len(self.display)-len(self.__last_input)]
                    self.deleteForm()
                    self.pushToForm(new_display, newline=True)
                
                self.__last_input = str(self.__memory.get())
                self.pushToForm(self.__last_input)
        
        # Simpan command terakhir
        self.__last_command = getExpr
        
                