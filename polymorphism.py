#polymorphism is also known as method overriding
#the term polymorphism means many forms


class Bird:
    def intro(self):
        print('There are many types of birds')
    def fly(self):
        print('Some birds can fly and some cannot')


class Pigeon(Bird):
    def fly(self):
        print('Pigeon can fly')


class Chicken(Bird):
    def fly(self):
        print('Chicken cannot fly')        

obj_b=Bird()

obj_b.intro()
obj_b.fly()

obj_p=Pigeon()
obj_p.fly()

obj_c=Chicken()
obj_c.fly()
