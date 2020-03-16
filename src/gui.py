from tkinter import *
from  tkinter import ttk
from Buttons import Buttons

class GUI:
    def __init__(self, root):
        # Konfigurasi awal
        self.root = root
        root.configure(background = 'black')
        root.title("Calculator")

        # Buat button
        self.Buttons = Buttons(_command = self.controller)
        
        # Form Ekspresi
        self.form = Text(root, state='disabled', width=30, height=4,background= "black", foreground="white")
        self.form.grid(row=0, column=0, columnspan=4, padx=5, pady=20)
        self.form.configure(state='normal')
        
        # Teks pada screen
        self.display = ''
   
    def pushToForm(self, exp_form, newline=False):
        pass
    
    def deleteForm(self):
        pass

    def controller(self, getExpr, push=True):
        pass
