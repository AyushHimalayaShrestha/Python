# methods -> a function defined inside the body of the class

class Employee:
    def work(self):
        print('He is a programmer')

    def salary(self,pay):
        print('Basic Salary is',pay)    


obj_ayush=Employee()
obj_ayush.work()
obj_ayush.salary(150000)