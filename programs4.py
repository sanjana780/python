# 29  wap to swap the two values
# a- with temp
# b- without temp
#a = int(input("enter any number"))
#b = int(input("enter any number"))
#a = b
#b = temp
#temp = a
#print(a)
#print(b)


a = input("Enter the first value: ")
b = input("Enter the second value: ")

#print(f"Original values - a: {a}, b: {b}")
temp = a
a = b
b = temp
#print(f"Swapped values - a: {a}, b: {b}")
print(a)
print(b)
   

#(b) without using temp swap values
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

#print(f"Original values - a: {a}, b: {b}")

a = a + b
b = a - b
a = a - b
#print(f"Swapped values - a: {a}, b: {b}")
print(a)
print(b)