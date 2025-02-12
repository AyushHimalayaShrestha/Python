#abstract classes are classes that contain one or more abstract methods.An abstract method is a method that is declared but contains no implementations.Abstract class cannot be instantiated and require subclass to provide implementation for the abstract methods. 

from abc import ABC, abstractmethod
class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

class Triangle(Polygon):
    def __init__(self,b,h):
        self.b=b,
        self.h=h

    def area(self):
        return 1/2*self.b*self.h        
    
class Reactangle(Polygon):
    def __init__(self,l,b):
        self.l=l,
        self.b=b  
    def area(self):
        return self.l*self.b

t=Triangle(3,5)
print(t.area())       