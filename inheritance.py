#class Person:
 #   def __init__(self, name, rollno):
  #      self.name = name
   #     self.rollno = rollno

    #def myfunc(self):
     # print("hello my name is" + self.name)
      #print("hello my name is" + self.rollno)


#p1 = Person("sanjana", 10)

#print("before remove p1 is" , p1.rollno)
#print("before remove p1 is" , p1.name)



#class student (Person):
 #   def __init__(self, fname, lrollno):
  #      self.fname = fname
   #     self.lrollno =lrollno

    # def printname(self):
     # print(self.fname,self.lrollno)
     

#x = student("sana",30)
#x.printname()






#new program

class Person:
    def __init__(self, fname, lname):
     self.lastname = lname

    def printname(self):
       print(self.firstname, self.lastname)

x = person("sana","kk")
x.printname()

class Student(Person):
    def __init__(self, fname, lname):
     self.firstname = fname
     self.lastname = lname

    def printname(self):
     print(self.firstname,self.lastname)

    def input(self):
      print('hi')
     

x = Student("sana", "kairo")
x.printname()
x.input



