class Account:
    minBalance=50000 #this is class variable

    def __init__(self,accountNo,name,balance):
        self.accountNo=accountNo, #instance vairable defined inside __init__ function
        self.fullname=name,
        self.balance=balance

    def display(self):
        print('Account Number:',self.accountNo)
        print('Name:',self.fullname)
        print('Balance:',self.balance)


obj_ayush=Account(607010005832,'Ayush Himalaya Shrestha',150000)

#to print minBalance
print('Minimum Balance:',Account.minBalance)
obj_ayush.display()
