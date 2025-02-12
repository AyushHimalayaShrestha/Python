#dictionary is a data type use to store data in key:value pairs

student={
    'first_name':'Ayush',
    'last_name':'Himalaya Shrestha',
    'age':25,
    'address':'Balaju, MachhaPokhari',
    'gender':'Male'
}
print(student)
print(type(student))
print(student['first_name'])

#keys() -> it only prints all the keys from the dictionary
print(student.keys())

#values() -> it only prints all the values from the dictionary
print(student.values())
print(len(student))