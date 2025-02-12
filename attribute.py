#attribute -> properties of an object

class Employee:
   def __init__(self,fullname,gender,address,age):
      self.name=fullname,
      self.gender=gender,
      self.address=address,
      self.age=age     
      


obj_ayush=Employee('Ayush Himalaya Shrestha','Male','Balaju',25)
print(obj_ayush.name,obj_ayush.gender,obj_ayush.address,obj_ayush.age)

