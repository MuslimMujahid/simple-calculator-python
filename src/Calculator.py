from parser import Parser
from Process import Process
from gui import GUI
import queue

class Calculator(GUI):

    def __init__ (self, root):

        super().__init__(root)        
        self.__memory = queue.LifoQueue(maxsize=3)
        self.__last_answer = False
        
        self.root.mainloop()
    
    def controller(self, getExpr, push=True):
        # kegunaan : memproses parsing dari Form GUI
        if (push != None):
            self.pushToForm(getExpr)
        else:   
            if (getExpr == '='): 
                if (u"\u221A" in self.expression):
                    self.expression = self.parseExpAkar(self.expression)
                if ("^" in self.expression):
                    self.expression = self.expression.replace("^", "**")
                if ("ans" in self.expression):
                    self.expression = self.expression.replace("ans", str(self.ans))
                print(self.expression)
                result = eval(self.expression)
                self.ans = result
                self.deleteForm()
                self.pushToForm(result, newline=True)
            elif getExpr == "clear":
                self.deleteForm()
            elif getExpr == "MC":
                self.history.append(self.ans)
            elif getExpr == "MR":
                self.pushToForm(self.history.pop(), newline=True)