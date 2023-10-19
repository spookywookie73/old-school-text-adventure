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
  

class Adventurer:

  def __init__(self, name, health = 30, inventory = []):
    self.name = name
    self.health = health
    self.inventory = inventory

  def __repr__(self):
    return "The name of this adventurer is {name}. {name} has bravely accepted the challenge to rid this \
dungeon of it's evil.".format(name = self.name)
  
  def health_points(self):
    if self.health > 1:
      print("You have {hp} health points.".format(hp = self.health))
    else:
      print("You have {hp} health point.".format(hp = self.health))



def game():
  choice = input("What do you want to do? : ")
  if choice.lower() == "health":
    hero.health_points()


# start game
print("You are standing in a candle lit room. Behind a table, thumbing through multiple books, \
stands an old man wearing what appears to be a wizard's robe. He looks at you and start's to talk. \
'Welcome brave adventurer, I have a quest for you. I need you to clear this dungeon of the evil that dwells there. \
If you complete this task you will be handsomely rewarded. Good Luck!'")
heroes_name = input("Please enter your name and press enter to begin. : ")

hero = Adventurer(heroes_name)
monster1 = Monster(random.choice(monster_list), random.randint(10, 20))
monster2 = Monster(random.choice(monster_list), random.randint(10, 20))
monster3 = Monster(random.choice(monster_list), random.randint(10, 20))
boss = Monster("Dark Elf Priestess", 40)

current_monster = monster1

game()
