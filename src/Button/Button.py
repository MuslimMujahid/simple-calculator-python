from tkinter import *
from  tkinter import ttk
import tkinter.font as font

class CustomButton(Button):
    
    '''
    
    Type
    self.__defaultBackground : string
    self.__activeBackground : string
    
    Fungsi 
    self.__defaultBackground : menyimpan default background
    self.__activeBackground : menyimpan active background
    
    '''
    
    def __init__(self, _text, _width = 8, _color = '#fbf8ea', _activecolor = '#f0eddf' , _command = None, _push=True):
        Button.__init__(
            self, text = _text, 
            bg = _color,
            activebackground = _activecolor,
            height = 3, 
            width = _width,
            borderwidth = 1,
            command = self.onClick(_command, _text, _push),
            font = font.Font(family='Helvetica', size = 9, weight = 'bold')
        )
        
        self.__defaultBackground = self["background"]
        self.__activebackground = self["activebackground"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self.__activebackground

    def on_leave(self, e):
        self['background'] = self.__defaultBackground

    def onClick (self, _command, _text, _push):
        return (lambda: _command(_text, _push))


        
