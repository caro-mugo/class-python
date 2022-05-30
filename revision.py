class Vehicle:
    color = "white"
    def __init__(self,name,max_speed,mileage):
      self.name = name
      self.max_speed = max_speed
      self.mileage = mileage
    
   
    def car(self):
        return f" Hello carol congratulations  for purchasing a {self.name} whose color is {self.color} with a speed of {self.max_speed} and a mileage of {self.mileage} "
    def caps(self,capacity):
        return f"Your {self.name} has a capacity of {capacity}"
    