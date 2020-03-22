from Button import CustomButton

class Buttons:
    
    '''
    
    Type 
    self.list 
    
    '''
    
    def __init__(self, _command):
        # Push Grid Button
        self.__list = []
        self.__command = _command        
        self.getButtonToForm()
    
    def getButtonToForm(self):    
        # kegunaan : membuat button kalkulator
        CustomButton("CLEAR", _color = '#ffb7a8', _activecolor = '#de8c81', _command = self.__command, _push=None).grid(column = 0, row = 1)
        CustomButton('MC', _color = '#f5e0e7', _activecolor = '#edcad5', _command = self.__command, _push=None).grid(column = 1, row = 1)
        CustomButton('MR', _color = '#f5e0e7', _activecolor = '#edcad5', _command = self.__command, _push=None).grid(column = 2, row = 1)
        CustomButton('^', _color = '#fff5bd',  _activecolor = '#ede4af',_command = self.__command).grid(column = 3, row = 1)

        CustomButton(7, _command = self.__command).grid(column = 0, row = 2)
        CustomButton(8, _command = self.__command).grid(column = 1, row = 2)
        CustomButton(9, _command = self.__command).grid(column = 2, row = 2)
        CustomButton(u"\u221A", _color = '#fff5bd', _activecolor = '#ede4af', _command = self.__command).grid(column = 3, row = 2)

        CustomButton(4, _command = self.__command).grid(column = 0, row = 3)
        CustomButton(5, _command = self.__command).grid(column = 1, row = 3)
        CustomButton(6, _command = self.__command).grid(column = 2, row = 3)
        CustomButton("/", _color = '#fff5bd', _activecolor = '#ede4af', _command = self.__command).grid(column = 3, row = 3)

        CustomButton(1, _command = self.__command).grid(column = 0, row = 4)
        CustomButton(2, _command = self.__command).grid(column = 1, row = 4)
        CustomButton(3, _command = self.__command).grid(column = 2, row = 4)
        CustomButton('*', _color = '#fff5bd', _activecolor = '#ede4af', _command = self.__command).grid(column = 3, row = 4)
        
        CustomButton(0, _command = self.__command).grid(column = 0, row = 5)
        CustomButton('.', _command = self.__command).grid(column = 1, row = 5)
        CustomButton('ANS',  _color = '#e4ffd4',  _activecolor = '#c2dbb4', _command = self.__command).grid(column = 2, row = 5 )
        CustomButton('+', _color = '#fff5bd', _activecolor = '#ede4af', _command = self.__command).grid(column = 3, row = 5)
        
        CustomButton('(',  _command = self.__command).grid(column = 0, row = 6)
        CustomButton(')',  _command = self.__command).grid(column = 1, row = 6)
        CustomButton('-', _color = '#fff5bd', _activecolor = '#ede4af', _command = self.__command).grid(column = 3, row = 6)
        CustomButton('=', _color = '#e4ffd4', _activecolor = '#c2dbb4', _command = self.__command, _push = None).grid(column = 2, row = 6)