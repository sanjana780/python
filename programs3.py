# wap to calculate the area of circle of radius R
#are=p2
#p = int(input("enter the area"))
#area = p*p
#print(area)

import math
R = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
area = math.pi * R ** 2

# Print the result
print(f"The area of the circle is: {area:.2f}")

