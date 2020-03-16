from Button import CustomButton

class Buttons:
    def __init__(self):
        # Push Grid Button
        self.list = []
        self.getButtonToForm()
    
    def getButtonToForm(self):    
        # kegunaan : membuat button kalkulator
        self.list.append(CustomButton('MC', 'light pink'))
        self.list.append(CustomButton('MR', 'light pink'))
        self.list.append(CustomButton("CLEAR",'light coral'))
        self.list.append(CustomButton('^', 'khaki'))
        self.list.append(CustomButton(7))
        self.list.append(CustomButton(8))
        self.list.append(CustomButton(9))
        self.list.append(CustomButton(u"\u221A", 'khaki'))
        self.list.append(CustomButton(4))
        self.list.append(CustomButton(5))
        self.list.append(CustomButton(6))
        self.list.append(CustomButton("/", 'khaki'))
        self.list.append(CustomButton(1))
        self.list.append(CustomButton(2))
        self.list.append(CustomButton(3))
        self.list.append(CustomButton('*', 'khaki'))
        self.list.append(CustomButton(0))
        self.list.append(CustomButton('.'))
        self.list.append(CustomButton('+'))
        self.list.append(CustomButton('-', 'khaki'))
        self.grid_up()
        self.grid_bottom()

    def grid_bottom(self):
        # kegunaan : mengatur grid
        equalButton = CustomButton('=','DarkSeaGreen2').grid(row=6,column=3)
        powerButton = CustomButton('ANS').grid(row=6,column=0)
        openButton = CustomButton(u"\u0028").grid(row=6,column=1)
        closeButton = CustomButton(u"\u0029").grid(row=6,column=2)

    def grid_up(self):
        # kegunaan : mengatur grid
        index=0
        i=1
        while (i<6):
            for j in range(4):
                self.list[index].grid(row=i, column=j)
                index=index+1
            i=i+1

    def onClick(self, _text, push=True, _color = 'ivory'):
        print("Click")
        # kegunaan : event-handler button dan memasukannya ke Form satu per satu
        return Button(self.root, text=_text, width=7, height = 2, bg = _color, command = lambda: self.controller(_text, push))