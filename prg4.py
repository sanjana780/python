#wap to swap the two values
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
print(num1,num2)

#before swapping
#num1 =2
#num2 =3
#temp =2

#after swapping
#num1 =3
#num2=2

#perform swaping operation(pattern one)
#temp = num1
#num1 = num2
#num2 = temp

#second pattern
num1 = num1+num2
num2 =  num1-num2
num1 = num1-num2

print(num1,"\n",num2)
