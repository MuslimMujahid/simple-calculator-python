from Button import CustomButton

class Buttons:
    def __init__(self, _command):
        # Push Grid Button
        self.list = []
        self.command = _command        
        self.getButtonToForm()
    
    def getButtonToForm(self):    
        # kegunaan : membuat button kalkulator
        self.list.append(CustomButton('MC', 'light pink', _command = self.command, _push=None))
        self.list.append(CustomButton('MR', 'light pink', _command = self.command, _push=None))
        self.list.append(CustomButton("CLEAR",'light coral', _command = self.command, _push=None))
        self.list.append(CustomButton('^', 'khaki', _command = self.command))
        self.list.append(CustomButton(7, _command = self.command))
        self.list.append(CustomButton(8, _command = self.command))
        self.list.append(CustomButton(9, _command = self.command))
        self.list.append(CustomButton(u"\u221A", 'khaki', _command = self.command))
        self.list.append(CustomButton(4, _command = self.command))
        self.list.append(CustomButton(5, _command = self.command))
        self.list.append(CustomButton(6, _command = self.command))
        self.list.append(CustomButton("/", 'khaki', _command = self.command))
        self.list.append(CustomButton(1, _command = self.command))
        self.list.append(CustomButton(2, _command = self.command))
        self.list.append(CustomButton(3, _command = self.command))
        self.list.append(CustomButton('*', 'khaki', _command = self.command))
        self.list.append(CustomButton(0, _command = self.command))
        self.list.append(CustomButton('.', _command = self.command))
        self.list.append(CustomButton('+', _command = self.command))
        self.list.append(CustomButton('-', 'khaki', _command = self.command))
        self.grid_up()
        self.grid_bottom()

    def grid_bottom(self):
        # kegunaan : mengatur grid
        equalButton = CustomButton('=','DarkSeaGreen2', _command = self.command, _push=None).grid(row=6,column=3)
        powerButton = CustomButton('ANS', _command = self.command).grid(row=6,column=0)
        openButton = CustomButton(u"\u0028", _command = self.command).grid(row=6,column=1)
        closeButton = CustomButton(u"\u0029", _command = self.command).grid(row=6,column=2)

    def grid_up(self):
        # kegunaan : mengatur grid
        index=0
        i=1
        while (i<6):
            for j in range(4):
                self.list[index].grid(row=i, column=j)
                index=index+1
            i=i+1