from tkinter import *
from  tkinter import ttk

class CustomButton(Button):
    def __init__(self, _text, _width = 8, _color = '#fbf8ea', _command = None, _push=True):
        Button.__init__(
            self, text = _text, 
            bg = _color,
            height = 3, 
            width = _width,
            borderwidth = 1,
            command = lambda: _command(_text, _push)
        )


        
