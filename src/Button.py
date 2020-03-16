from tkinter import *
from  tkinter import ttk

class CustomButton(Button):
    def __init__(self, _text, _color = 'ghostwhite', _command = None, _push=True):
        Button.__init__(
            self, text = _text, 
            bg = _color, 
            width = 8, 
            height = 3, 
            borderwidth = 1, 
            command = lambda: _command(_text, _push)
        )


        
