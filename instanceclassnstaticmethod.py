#class methods -> are methods that are not bound to an instance of a class but to a class itself.Class methods can only access and modify class variables and not instance variable.

#instance variable -> can access and modify both class and instance variable


#static methods -> unlike instance and class methods, static methods cannot access class attributes or instance attributes.In python we create static method using @staticmethod decorator.
 
class Account:
    minbalance=1000 #class variable

    def __init__(self,accountNo,name,balance):
        self.accountNo=accountNo,
        self.name=name,
        self.balance=balance

    def display(self):
        print('Account Number:',self.accountNo)
        print('Name:',self.name)
        print('Balance:',self.balance)

    def deposit(self,amount):
        self.balance=self.balance+amount    

    @classmethod
    def displayMin(account):
        print('Minimum Balance:',account.minbalance)
        
    @staticmethod
    def checkbalance(amount,balance):
        if(amount>balance):
            return -1
        else:
            return 1

    def withdraw(self,amount):
        r=Account.checkbalance(amount,self.balance)
        if r == -1:
            print('Insufficient Balance')
        else:
            self.balance=self.balance-amount


a=Account(1001,'Ayush Himalaya Shrestha',200000)
a.displayMin()
a.display()
a.deposit(1200)
a.display()     
a.withdraw(500)
a.display()                   
