# importing the Random module
import random
# creating a list of monster names
monster_list = ["Snivelling Goblin", "Dark Elf", "Cave Troll", "Giant Spider", "Dire Wolf"]

#creating the classes needed for the game
class Monster:

  def __init__(self, name, health):
    self.name = name
    self.health = health
    
  def __repr__(self):
    return "This is a {name}. It is a foul creature that has dwelled in this dungeon for far too long. \
It's health is {health}.".format(name = self.name, health = self.health)
  
# enemy1 = Monster(random.choice(monster_list), random.randint(10,20))
# print(enemy1)
class Adventurer:

  def __init__(self, name, health = 30, inventory = []):
    self.name = name
    self.health = health
    self.inventory = inventory

  def __repr__(self):
    return "The name of this adventurer is {name}. {name} has bravely accepted the challenge to rid this \
dungeon of it's evil.".format(name = self.name)
  
# hero = Adventurer("Bob")
# print(hero)
