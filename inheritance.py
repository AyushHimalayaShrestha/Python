#inheritance is to form a new class from a parent class or class that have been already defined.The newly formed class is known as derive class and class from which the new class is formed is known as base class.

class Animal:
    def __init__(self):
        print('Animal class created')
    def who(self):
        print('Animal')
    def eat(self):
        print('Some animal are carnivorous and some are herbivorous')

class Dog(Animal):
    def who(self):
        print('Dog')

class GermanShepard(Dog):
    def who(self):
        print('German Shepard')        

    

a=Animal()
print(a)
a.who()
a.eat()

d=Dog()
d.who()
d.eat()

g=GermanShepard()
g.who()
g.eat()