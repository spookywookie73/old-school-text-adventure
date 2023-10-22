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
    game()


# functions for the rooms
def room_1():
  global current_room
  current_room = 1
  if "sword" in hero.inventory:
    print("You are standing in a small room. There is a doorway to the north.")
  else:
    print("You are standing in a small room. There is a sword on the floor and a doorway to the north.")
  game()

# functions for the items that can be used
def sword():
  if current_room == 1 and "sword" not in hero.inventory:
    hero.inventory.append("sword")
    print("You pick up the sword.")
    game()
  elif "sword" in hero.inventory:
    print("The only sword available is sheathed on your belt.")
    game()

def horn():
  if "horn" in hero.inventory:
    print("There is no horn to pick up.")
    game()
  elif current_room == 17 and "horn" not in hero.inventory:
    hero.inventory.append("horn")
    print("You pick up the horn and put it in your satchel.")
    game()
  else:
    print("There is no horn to pick up.")
    game()

def bread():
  if "bread" in hero.inventory:
    print("There is no bread to pick up.")
    game()
  elif current_room == 5 and "bread" not in hero.inventory:
    hero.inventory.append("bread")
    print("You pick up the bread and put it in your satchel.")
    game()
  else:
    print("There is no bread to pick up.")
    game()

def key():
  if "key" in hero.inventory:
    print("There is no key to pick up.")
    game()
  elif current_room == 4 and "key" not in hero.inventory:
    hero.inventory.append("key")
    print("You pick up the key and put it in your pocket.")
    game()
  else:
    print("There is no key to pick up.")
    game()

def potion():
  if "potion" in hero.inventory:
    print("There is no potion to pick up.")
    game()
  elif current_room == 15 and "potion" not in hero.inventory:
    hero.inventory.append("potion")
    print("You pick up the potion and put it in your satchel.")
    game()
  else:
    print("There is no potion to pick up.")
    game()

def hammer():
  if "hammer" in hero.inventory:
    print("There is no hammer to pick up.")
    game()
  elif current_room == 5 and "hammer" not in hero.inventory:
    hero.inventory.append("hammer")
    print("You pick up the hammer and put it in your satchel.")
    game()
  else:
    print("There is no hammer to pick up.")
    game()

# functions for running the game and battles
def game():
  global current_room
  choice = input("What do you want to do? : ")
  if choice.lower() == "health":
    hero.health_points()
  if choice.lower() == "get sword":
    sword()
  if choice.lower() == "get horn":
    horn()
  if choice.lower() == "get bread":
    bread()
  if choice.lower() == "get key":
    key()
  if choice.lower() == "get potion":
    potion()
  if choice.lower() == "get hammer":
    hammer()
  if choice.lower() == "inventory":
    print(hero.inventory)
    game()
  


# start of game
print("You are standing in a candle lit room. Behind a table, thumbing through multiple books, \
stands an old man wearing what appears to be a wizard's robe. He looks at you and start's to talk. \
'Welcome brave adventurer, I have a quest for you. I need you to clear this dungeon of the evil that dwells there. \
If you complete this task you will be handsomely rewarded. Good Luck!'")
heroes_name = input("Please input your name and press enter to begin. : ")

hero = Adventurer(heroes_name)
monster1 = Monster(random.choice(monster_list), random.randint(10, 20))
monster2 = Monster(random.choice(monster_list), random.randint(10, 20))
monster3 = Monster(random.choice(monster_list), random.randint(10, 20))
boss = Monster("Dark Elf Priestess", 40)

current_monster = monster1
current_room = 0

print("The old man whispers something and you are suddenly surrounded by a thick black smoke. \
After a few moments the smoke clears and you look around.")

room_1()
