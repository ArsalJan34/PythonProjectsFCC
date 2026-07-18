class GameCharacter:

# createing an method named __init__ it runs automatically everytime you create a new character
# parameters ; self, character_name, job_type
  def __init__(self,character_name,job_type):
    # attributes
    self.name = character_name
    self.job = job_type
    # default attricbutes
    self.health = 100
    self.isalive = True
  # method : an action that this character can do
  # parameter : amount
  def take_damage(self,amount):
    self.health -= amount
    print(f" {self.name} took {amount} damage! health is now {self.health}")
    if self.health <= 0:
      self.isalive = False
      print(f"{self.name} the {self.job} has fallen! ")


# objects / instances

player1 = GameCharacter("Wesker", "Superhuman")
player2 = GameCharacter("Dante", "Celestial")

print(player1.name)
print(player1.job)
player1.take_damage(30)
player1.take_damage(70)
