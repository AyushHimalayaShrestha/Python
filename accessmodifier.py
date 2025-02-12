#public -> all the members in python class are public by default and they can be accessed from anywhere
#private -> a double underscore '__' makes the variable private as well as secure.Private members are accessible within the class only.
#protected -> a underscore '_' makes the variable protected. Protected members can only be accessed from the child class.

class AccessTest:
    def __init__(self,a,b,c):
        self.a=a,
        self.__b=b,
        self._c=c

    def display(self):
        print('Display from function inside class')
        print('a=',self.a)
        print('b=',self.__b)
        print('c=',self._c)    

x=AccessTest(10,20,30)
x.display()  