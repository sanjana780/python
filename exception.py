""" a = int(input("enter first number:"))
b = int(input("enter second number:")) 
try:
    c=a/b
    print(c)
except:
    print("cant devide")
else:
    print("sana") """     #alt+shift+A

# 2 program

""" a=10
try:
    a=a+a
    print(a)
except:
    print("cant devide")
else:
    print("sana")
 """


""" try:
 f = open("demofile.txt")
 try:
    f.write("sanjana kairo")
 except:
    print("something went wrong when writing to the file")
 finally:
    f.close()
except:
 print("something went wrong when opening the file")  """


""" x=10
try:
    print(x)
except:
    print("something went wrong")
finally:
    print("finished") """



""" try:
    print("hello")
except:
    print("something went wrong")
else:
    print("finished") """




try:
    print("hello")
except:
    print("something went wrong")

    #print("hello")


try:
    print("hello")
except NameError:
    print("something went wrong")
except:
    print("something went wrong")
print("hello")