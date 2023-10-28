# importing the Random module
import random
# a list of monster names
monster_list = ["Snivelling Goblin", "Dark Elf", "Cave Troll", "Giant Spider", "Dire Wolf"]
# a list of the commands you can use
commands = ["north", "south", "east", "west", "get sword", "get book", "get bread", "get key", "get horn", 
"get potion", "get hammer", "examine sword", "examine book", "examine bread", "examine key", "examine horn",
 "examine potion", "examine hammer", "eat bread", "give bread to old man", "put book in bookcase", "open chest",
  "put horn on stand", "drink potion", "give hammer to dwarf", "get gem", "examine gem", "examine chest",
  "examine bookcase", "examine stand", "examine dwarf", "examine old man"]

#creating the classes needed for the game
class Monster:

  def __init__(self, name, health):
    self.name = name
    self.health = health
    
  def __repr__(self):
    return "This is a {name}. It is a foul creature that has dwelled in this dungeon for far too long. \
It's health is {health}.".format(name = self.name, health = self.health)
  

class Adventurer:

  def __init__(self, name, health = 30, gems = 0, inventory = []):
    self.name = name
    self.health = health
    self.gems = gems
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
  if choice.lower() == "examine sword" and "sword" in hero.inventory:
    print("This is a medium sized sword. The handle is in good condition and the blade is surprisingly sharp.")
  elif choice.lower() == "examine sword" and "sword" not in hero.inventory:
    print("You are not holding a sword.")
  elif current_room == 1 and choice.lower() == "get sword" and "sword" not in hero.inventory:
    hero.inventory.append("sword")
    print("You pick up the sword.")
  elif choice.lower() == "get sword" and "sword" in hero.inventory:
    print("The only sword available is sheathed on your belt.")
  else:
    print("There is no sword here.")
  game()

def horn():
  if choice.lower() == "examine horn" and "horn" in hero.inventory:
    print("This is an ordinary looking bulls horn used for making a noise.")
  elif choice.lower() == "examine horn" and "horn" not in hero.inventory:
    print("You do not have a horn.")
  elif current_room == 17 and choice.lower() == "get horn" and "horn" not in hero.inventory:
    hero.inventory.append("horn")
    print("You pick up the horn and put it in your satchel.")
  elif choice.lower() == "get horn" and "horn" in hero.inventory:
    print("The only horn available is in your satchel.")
  else:
    print("There is no horn to pick up.")
  game()

def bread():
  if choice.lower() == "examine bread" and "bread" in hero.inventory:
    print("This is a freshly baked small loaf of bread. It's still warm and smells delicious.")
  elif choice.lower() == "examine bread" and "bread" not in hero.inventory:
    print("You do not have any bread.")
  elif current_room == 5 and choice.lower() == "get bread" and "bread" not in hero.inventory:
    hero.inventory.append("bread")
    print("You pick up the bread and put it in your satchel.")
  elif choice.lower() == "get bread" and "bread" in hero.inventory:
    print("The only bread available is in your satchel.")
  else:
    print("There is no bread to pick up.")
  game()

def key():
  if choice.lower() == "examine key" and "key" in hero.inventory:
    print("This is a medium sized key suitable for opening a chest.")
  elif choice.lower() == "examine key" and "key" not in hero.inventory:
    print("You do not have a key.")
  elif current_room == 4 and choice.lower() == "get key" and "key" not in hero.inventory:
    hero.inventory.append("key")
    print("You pick up the key and put it in your pocket.")
  elif choice.lower() == "get key" and "key" in hero.inventory:
    print("The only key here is in your pocket.")
  else:
    print("There is no key to pick up.")
  game()

def potion():
  if choice.lower() == "examine potion" and "potion" in hero.inventory:
    print("This is a health potion. It fully restores your health points.")
  elif choice.lower() == "examine potion" and "potion" not in hero.inventory:
    print("You are not carrying any potion.")
  elif current_room == 15 and choice.lower() == "get potion" and "potion" not in hero.inventory:
    hero.inventory.append("potion")
    print("You pick up the potion and put it in your satchel.")
  elif choice.lower() == "get potion" and "potion" in hero.inventory:
    print("The only potion here is attached to your belt.")
  else:
    print("There is no potion to pick up.")
  game()

def hammer():
  hammer_in_chest = True
  if choice.lower() == "examine hammer" and "hammer" in hero.inventory:
    print("This is a magnificent hammer. It has dwarven runes engraved down the handle and the head is unblemished.")
  elif choice.lower() == "examine hammer" and "hammer" not in hero.inventory:
    print("You are not carrying a hammer.")
  elif current_room == 16 and choice.lower() == "get hammer" and chest.chest_open == True and hammer_in_chest == True and "hammer" not in hero.inventory:
    hero.inventory.append("hammer")
    print("You pick up the hammer and put it in your satchel.")
    hammer_in_chest = False
  elif choice.lower() == "get hammer" and "hammer" in hero.inventory:
    print("You are already carrying the hammer.")
  else:
    print("There is no hammer to pick up.")
  game()

def book():
  if choice.lower() == "examine book" and "book" in hero.inventory:
    print("The book is standard sized. The front and back covers are creased and it's title is 'The Secret Passage'.")
  elif choice.lower() == "examine book" and "book" not in hero.inventory:
    print("You do not have a book.")
  elif current_room == 11 and choice.lower() == "get book" and "book" not in hero.inventory:
    hero.inventory.append("book")
    print("You pick up the book and put it in your satchel.")
  elif choice.lower() == "get book" and "book" in hero.inventory:
    print("You already have the book.")
  else:
    print("There is no book to pick up.")
  game()

def gems():
  if hero.gems == 3:
    print("As soon as you receive the 3rd gemstone, you feel your health points increase")
    hero.health = 45
  elif choice.lower() == "examine gemstone" and "gemstone" in hero.inventory:
    print("It is a blue gemstone.")
  #elif choice.lower() == "examine gemstone" and "gemstone" not in hero.inventory:
  else:
    print("You don't have a gemstone.")
  game()

# functions for interactive objects
def bookcase():
  bookcase_full = False
  if current_room == 7 and choice.lower() == "put book in bookcase" and "book" in hero.inventory and bookcase_full == False:
    print("You put the book back on it's shelf. As soon as you let go of the book the bookcase slides to it's left, \
revealing a hidden passage to the east.")
    bookcase_full = True
    hero.inventory.remove("book")
  elif current_room == 7 and choice.lower() == "put book in bookcase" and "book" not in hero.inventory:
    print("You do not have a book.")
  #elif choice.lower() == "put book in bookcase" and current_room != 7:
   # print("There is no bookcase here.")
  elif current_room == 7 and choice.lower() == "examine bookcase" and bookcase_full == False:
    print("A large bookcase stands against the eastern wall. It's shelves are full of books, \
except for one space on the middle shelf.")
  elif current_room == 7 and choice.lower() == "examine bookcase" and bookcase_full == True:
    print("The large bookcase, now full of books, has slid to the side granting access to a secret passage.")
  else:
    print("There is no bookcase here.")
  game()

def chest():
  chest_open = False
  if choice.lower() == "open chest" and current_room == 16 and "key" in hero.inventory:
    print("You take the key from your pocket and open the chest.")
    hero.inventory.remove("key")
    chest_open = True
  elif current_room == 16 and choice.lower() == "open chest" and chest_open == True:
    print("The chest is already open.")
  elif current_room == 16 and choice.lower() == "open chest" and chest_open == False and "key" not in hero.inventory:
    print("You do not have a key.")
  elif current_room == 16 and choice.lower() == "examine chest" and chest_open == False:
    print("It is a large metal chest. It has rust running along it's edges and is currently locked.")
  elif current_room == 16 and choice.lower() == "examine chest" and hammer.hammer_in_chest == True and chest_open == True:
    print("The chest contains a Dwarven hammer.")
  elif current_room == 16 and choice.lower() == "examine chest" and hammer.hammer_in_chest == False and chest_open == True:
    print("The large chest lies open and empty.")
  else:
    print("There is no chest here.")
  game()

def stand():
  horn_on_stand = False
  if current_room == 19 and horn_on_stand == False:
    print("This ornate marble stand has a flat top and an engraving of a man blowing a horn on it's side.")
  elif current_room == 19 and horn_on_stand == True:
    print("The ornate stand is now shorter than it was and now has a horn placed upon it.")
  else:
    print("There is no stand in this room.")
  game()

def old_man():
  has_eaten = False
  if current_room == 24 and choice.lower() == "give bread to old man" and "bread" in hero.inventory:
    print("The Old Man smiles, thanks you for your generosity and gives you a gemstone.")
    has_eaten = True
    hero.inventory.remove("bread")
    hero.gems += 1
    hero.inventory.append("gemstone")
    gems()
  elif current_room == 24 and choice.lower() == "give bread to old man" and "bread" not in hero.inventory:
    print("You are not carrying any bread")
  elif current_room == 24 and choice.lower() == "examine old man" and has_eaten == False:
    print("There is an Old Man sitting against the northern wall. His clothes and hair are dirty and he looks very hungry.")
  elif current_room == 24 and choice.lower() == "examine old man" and has_eaten == True:
    print("The Old Man looks quite content now.")
  else:
    print("There is no Old Man here.")
  game()

def dwarf():
  has_hammer = False
  if current_room == 8 and has_hammer == False:
    print("There is a Dwarf pacing back and forth muttering something about misplacing an important item.")
    #game()
  elif current_room == 8 and has_hammer == True:
    print("The Dwarf is sitting cross-legged on the floor cleaning his hammer.")
    #game()
  else:
    print("There is no Dwarf here.")
  game()

# functions for running the game and battles
def game():
  global choice
  choice = input("What do you want to do? : ")
  if choice.lower() == "health":
    hero.health_points()
  elif choice.lower() == "get sword" or choice.lower() == "examine sword":
    sword()
  elif choice.lower() == "get horn" or choice.lower() == "examine horn":
    horn()
  elif choice.lower() == "get bread" or choice.lower() == "examine bread":
    bread()
  elif choice.lower() == "get key" or choice.lower() == "examine key":
    key()
  elif choice.lower() == "get potion" or choice.lower() == "examine potion":
    potion()
  elif choice.lower() == "get hammer" or choice.lower() == "examine hammer":
    hammer()
  elif choice.lower() == "get book" or choice.lower() == "examine book":
    book()
  elif choice.lower() == "get gemstone":
    gems()
  elif choice.lower() == "inventory":
    print(hero.inventory)
    game()
  #elif choice.lower() == "attack":
   # print("There is nothing here to attack.")
   # game()
  elif choice.lower() == "examine bookcase":
    bookcase()
  elif choice.lower() == "help":
    print(commands)
    game()
  else:
    print("That won't work.")
  


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
choice = ""

print("The old man whispers something and you are suddenly surrounded by a thick black smoke. \
After a few moments the smoke clears and you look around.")

room_1()
