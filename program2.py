#38 (d) wap to calculate the sum of first and last digit of four digit number

number = int(input("Enter a four-digit number: "))
number_str = str(number)

first_digit = int(number_str[0])
last_digit = int(number_str[-1])

sum_of_digits = first_digit + last_digit
print("The sum of the first and last digit is:", sum_of_digits)

#(c) wap to calculate the sum of first and last digit of three digit number

number = int(input("Enter a three-digit number: "))
number_str = str(number)

first_digit = int(number_str[0])
last_digit = int(number_str[-1])

sum_of_digits = first_digit + last_digit
print("The sum of the first and last digit is:", sum_of_digits)


# (b) wap to print the sum of four number
num1 = int(input("enter any number"))
num2 = int(input("enter any number"))
num3 = int(input("enter any number"))
num4 = int(input("enter any number"))
sum = num1+num2+num3+num4
print(sum)


# (a) wap to print the sum of three number
num1 = int(input("enter any number"))
num2 = int(input("enter any number"))
num3 = int(input("enter any number"))

sum = num1+num2+num3
print(sum)
