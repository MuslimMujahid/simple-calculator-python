from tkinter import *
from  tkinter import ttk
from Buttons import Buttons

class App:
    '''
    Class ini mengatur desain user interface
    
    self.root : objek Tk()
    self.Buttons : objek Buttons()
    ...
    '''
    def __init__(self, root):
        # Konfigurasi awal
        self.root = root
        root.configure(background = '#9e9e9e')
        root.title("Calculator")
        root.iconbitmap('icon.ico')

        # Buat button
        self.Buttons = Buttons(_command = self.controller)
        
        # Form Ekspresi
        self.form = Text(root, state='disabled', width=28, height=4,background= "ghostwhite", foreground="black")
        self.form.grid(row=0, column=0, columnspan=4, padx=2, pady=20)
        self.form.configure(state='normal')
        
        # Teks pada screen
        self.display = ''
   
    def pushToForm(self, exp_form, newline=False):
        pass
    
    def deleteForm(self):
        pass

    def controller(self, getExpr, push=True):
        pass
