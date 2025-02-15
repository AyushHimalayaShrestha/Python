# methods can have same name and operations but parameter they take as input values are different

class Student:
    def show(self,fname=None,lname=None):
        if fname is not None and lname is not None:
            print('Hello',fname,lname)

        elif fname is not None:
            print('Hello',fname)
        else:
            print('Hello')

obj=Student()
obj.show()
obj.show('Ayush')
obj.show('Ayush','Himalaya Shrestha')                    
