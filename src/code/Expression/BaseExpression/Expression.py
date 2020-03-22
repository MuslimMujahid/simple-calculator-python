# ABC = abstract base class, buat kelas abstrak
from abc import ABC, abstractmethod

class Expression(ABC):
    
    @abstractmethod
    def solve(self):
        pass
