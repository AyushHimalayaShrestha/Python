#loop -> repeatation or iteration
#for loop
#while loop

fruits=['apple','mango','cherry','grapes']
for x in fruits:
    print(x)

for i in range(20):
    print(i,end=" ")    

print('\n')#line break

for j in range(2,30,3):
    print(j, end=" ")
    print('\n')

for letter in 'Hello':
    print(letter)    

#while loop
a=1
while a<10:
    print(a)
    a+=1

#break
b=1
while(b<20):
    if b==10:
       break 
    print(b)
    b+=1

#continue
for i in range(2,201):
    for j in range(2,201):
        if i%2==0:
            break
