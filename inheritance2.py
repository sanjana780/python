class Ottsubscription:
  def __init__(self,id,plan,total_payment):
    self.id = id
    self.plan = plan
    self.total_payment = total_payment
  def subscribe(self):
     print(self.id)
     print(self.plan)
#x = Ottsubscription(1,22,33)
#x.subscribe()
    
class Premiumsubscription(Ottsubscription):
    def __init__(self,id,plan,total_payment,screens):
     super().__init__(id,plan,total_payment)
     self.screens = screens
    def set_screens(self,screens):
      self.screens = screens

print(self.screens)

x = Premiumsubscription(2,45,77,100)
x.set_screens()      
