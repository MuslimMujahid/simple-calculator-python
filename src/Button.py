from tkinter import *
from  tkinter import ttk

class CustomButton(Button):
    def __init__(self, _text, _color = 'ghostwhite'):
        Button.__init__(self, text = _text, bg = _color, width = 8, height = 3, borderwidth = 1)
        #Button['font'] = myFont
    
    #def onClick(self, push = True):


# root = Tk()
# root.geometry('200x200')

# my_button = CustomButton(root, text='red button')
# my_button.pack()

# root.mainloop()

        
