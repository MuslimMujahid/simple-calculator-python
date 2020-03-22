from tkinter import *
from  tkinter import ttk
from Buttons import Buttons

class App:
    
    '''
    
    Class ini mengatur desain user interface
    
    self.root : objek Tk()
    self.Buttons : objek Buttons()
    
    '''
    
    def __init__(self):
        # Konfigurasi awal
        self.root = Tk()

        # Buat button
        self.Buttons = Buttons(_command = self.controller)
   
    def pushToForm(self, exp_form, newline=False):
        pass
    
    def deleteForm(self):
        pass

    def controller(self, getExpr, push=True):
        pass
