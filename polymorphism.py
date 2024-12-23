class vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("move!")

class Car(vehicle):
  #def __init__(self, brand, model):
   # self.brand = brand
    #self.model = model

  #def move(self):
   # print("Drive!")
   pass

class Boat(vehicle):
  def move(self):
    print("Sail!")

class Plane(vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

#for x in (car1, boat1, plane1):
 # x.move()
#boat1.move()
#for x in (car1, boat1, plane1):
 # print(x.brand)
  #print(x.model)
  #x.move()

#boat1.move()
#plane1.move()
#print(plane1.brand)

#boat1.move()

#for x in (car1,boat1,plane1):
 # x.move()

car1.move()
boat1.move()
plane1.move()