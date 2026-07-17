class Planet():
  def __init__(self, name, type, star):
    if not isinstance(name, str) or not (type, str) or not (star, str):
      raise TypeError("name, type, and star should be string")
    if name == "" or type == "" or star == "":
      raise ValueError("name, type and star should not be empty ")

    self.name = name
    self.type = type
    self.star = star

    def orbit(self):
      return f"{self.name} is orbiting around {self.star}..."
    def __str__(self):
      return f"Planet : {self.name} | Type: {self.type} | Star : {self.star}"

planet_1 = Planet("Earth", "Liveable", "Sun")
planet_2 = Planet("Mars", "not Liveable", "Sun")
planet_3 = Planet("Jupiter", "not liveable", "Sun")
print(planet_1)
print(planet_2)
print(planet_3)
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
