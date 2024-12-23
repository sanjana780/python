#class Faculty:
 #   def putdata(self):
  #      self.id= int(input("enter any id"))
  #      self.name= input("enter any name")
   #     self.salary= float(input("enter ur salary"))
    #def result(self):
    #    print(self.id)
     #   print(self.name)
      #  print(self.salary)
#a=Faculty()
#a.putdata()
#a.result()


class Faculty:
    def __init__(self,a,b,c):
        self.id= a
        self.name= b
        self.salary= c
    def result(self):
        print(self.id)
        print(self.name)
        print(self.salary)
a=Faculty(1,'sana',39999)
a.result()