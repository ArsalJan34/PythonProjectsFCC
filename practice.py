class Vehicle:
  def __init__(self,brand,model):
    self.brand = brand
    self.model = model
  def description(self):
      return f"{self.brand} {self.model}"
class Car(Vehicle):
  def description(self):
    return f"Car: {self.brand} {self.model}"
class Bike(Vehicle):
  def description(self):
    return f"Bike: {self.brand} {self.model}"

vehicles = [Car("Toyota", "Corolla"), Bike("Yamaha", "R1")]
for vehicle in vehicles:
  print(vehicle.description())
