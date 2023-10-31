# importing the Random module
import random
# a list of monster names
monster_list = ["Snivelling Goblin", "Dark Elf", "Cave Troll", "Giant Spider", "Dire Wolf"]
# a list of the commands you can use
commands = ["north", "south", "east", "west", "get sword", "get book", "get bread", "get key", "get horn", 
"get potion", "get hammer", "examine sword", "examine book", "examine bread", "examine key", "examine horn",
 "examine potion", "examine hammer", "eat bread", "give bread to old man", "put book in bookcase", "open chest",
  "put horn on stand", "drink potion", "give hammer to dwarf", "get gem", "examine gem", "examine chest",
  "examine bookcase", "examine stand", "examine dwarf", "examine old man", "examine gemstone"]

#creating the classes needed for the game
class Monster:

  def __init__(self, name, health):
    self.name = name
    self.health = health
    
  def __repr__(self):
    return "This is a {name}. It is a foul creature that has dwelled in this dungeon for far too long. \
It's health is {health}.".format(name = self.name, health = self.health)
  
  def attack(self):
    attack_damage = random.randint(3, 7)
    boss_attack_damage = random.randint(6, 12)
    if hero.health > 0 and current_monster == monster1 or hero.health > 0 and current_monster == monster2:
      print("You are attacked and take {damage} points of damage.".format(damage = attack_damage))
      hero.health -= attack_damage

      if hero.health <= 0:
        print("The {enemy} lunges and inflicts a fatal blow. You crash to the floor, your breathing slows. \
As the light begins to fade you wonder if you were really ready for a challenge like this.".format(enemy = current_monster.name))
        print("Unfortunately, this is were your adventure ends. Goodbye.")
        exit()
      else:
        game()
    elif hero.health > 0 and current_monster == boss:
      print("You are hit and take {damage} points of damage.".format(damage = boss_attack_damage))
      hero.health -= boss_attack_damage

      if hero.health <= 0:
        print("The Dark Elf Priestess casts a spell at you and this time you don't recover. The light slips \
away and your adventure comes to an end. Goodbye.")
        exit()
      else:
        game()


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

  def use_book(self):
    if current_room == 7 and "book" in self.inventory:
      print("You put the book back on it's shelf. As soon as you let go of the book the bookcase slides to it's left, \
revealing a hidden passage to the east.")
      bookcase.bookcase_full = True
      self.inventory.remove("book")
    elif current_room == 7 and "book" not in self.inventory:
      print("You do not have a book.")
    else:
      print("There is no bookcase here.")
    game()

  def use_bread(self):
    if current_room == 24 and choice.lower() == "give bread to old man" and "bread" in self.inventory:
      print("The Old Man smiles, thanks you for your generosity and gives you a gemstone.")
      old_man.has_eaten = True
      self.inventory.remove("bread")
      self.gems += 1
      self.inventory.append("gemstone")
      gems()
    elif current_room == 24 and choice.lower() == "give bread to old man" and "bread" not in self.inventory:
      print("You are not carrying any bread")
    elif choice.lower() == "eat bread" and "bread" in self.inventory:
      print("You eat the bread, and it was delicious.")
      self.inventory.remove("bread")
    elif choice.lower() == "eat bread" and "bread" not in self.inventory:
      print("You don't have any bread to eat.")
    else:
      print("There is no old man here.")
    game()

  def use_potion(self):
    if self.gems == 3 and "potion" in self.inventory:
      print("You drink the potion and feel restored.")
      self.health = 45
      self.inventory.remove("potion")
    elif self.gems < 3 and "potion" in self.inventory:
      print("You drink the potion and it restores your health points.")
      self.health = 30
      self.inventory.remove("potion")
    else:
      print("You don't have any potion.")
    game()

  def use_horn(self):
    if current_room == 19 and "horn" in self.inventory:
      print("You place the horn onto the stand. The stand begins to vibrate and then lowers several inches \
into the ground. As it lowers, two doorways to the north and east appear.")
      stand.horn_on_stand = True
      self.inventory.remove("horn")
    elif current_room == 19 and "horn" not in self.inventory:
      print("You are not carrying a horn.")
    else:
      print("There is no stand here.")
    game()

  def use_hammer(self):
    if current_room == 8 and "hammer" in self.inventory:
      print("The Dwarf takes the hammer from you. He stares at it for a few seconds, and then with a sudden swing of his arms, \
he smashes the large pile of rocks to dust leaving a doorway to the west.")
      self.inventory.remove("hammer")
      dwarf.has_hammer = True
    elif current_room == 8 and "hammer" not in self.inventory:
      print("You do not have a hammer.")
    else:
      print("There is no Dwarf here.")
    game()

  def use_key(self):
    if current_room == 16 and "key" in self.inventory:
      print("You take the key from your pocket and open the chest.")
      self.inventory.remove("key")
      chest.chest_open = True
    elif current_room == 16 and chest.chest_open == True:
      print("The chest is already open.")
    elif current_room == 16 and chest.chest_open == False and "key" not in self.inventory:
      print("You do not have a key.")
    else:
      print("There is no chest here.")
    game()

  def attack(self):
    global monster_in_room
    if current_room == 14 or current_room == 23:
      if monster_in_room == True and current_monster.health > 0:
        attack_points = random.randint(8, 18)
        print("You hit the {enemy} with your sword inflicting {damage} points \
of damage.".format(enemy = current_monster.name, damage = attack_points))
        current_monster.health -= attack_points

        if current_monster.health <= 0:
          print("You have defeated the {enemy}. You search the area and pickup \
a gemstone.".format(enemy = current_monster.name))
          monster_in_room = False
          self.gems += 1
          self.inventory.append("gemstone")
          gems()
        else:
          current_monster.attack()
      else:
        print("There is nothing to attack.")
    elif current_room == 25:
      attack_points = random.randint(8, 18)
      print("You slice at the {boss} inflicting {damage} points of \
damage.".format(boss = current_monster.name, damage = attack_points))
      current_monster.health -= attack_points

      if current_monster.health <= 0:
        print("With a lunging blow, you defeat the Dark Elf Priestess. The darkness that enveloped the \
dungeon has lifted. The Wizard appears in front of you. He hands you a bag of gold coins and thanks you for \
everything you have done. Before you have a chance to respond, he snaps his fingers and you find yourself back in your home.")
        print("Thankyou for playing my little adventure.")
        exit()
      else:
        current_monster.attack()
    game()

  def movement(self):
    if current_room == 1 and choice.lower() == "north":
      room_2()
    elif current_room == 2 and choice.lower() == "north":
      room_4()
    elif current_room == 2 and choice.lower() == "south":
      room_1()
    elif current_room == 2 and choice.lower() == "east":
      room_5()
    elif current_room == 2 and choice.lower() == "west":
      room_3()
    elif current_room == 3 and choice.lower() == "east":
      room_2()
    elif current_room == 3 and choice.lower() == "west":
      room_8()
    elif current_room == 3 and choice.lower() == "south":
      room_6()
    elif current_room == 4 and choice.lower() == "south":
      room_2()
    elif current_room == 4 and choice.lower() == "east":
      room_19
    elif current_room == 5 and choice.lower() == "west":
      room_2()
    elif current_room == 5 and choice.lower() == "south":
      room_7()
    elif current_room == 6 and choice.lower() == "north":
      room_3()
    elif current_room == 6 and choice.lower() == "south":
      room_11()
    elif current_room == 7 and choice.lower() == "north":
      room_5()
    elif current_room == 7 and choice.lower() == "south":
      room_9()
    elif current_room == 7 and choice.lower() == "east" and room_7.hidden_passage == True:
      room_10()
    elif current_room == 8 and choice.lower() == "west" and room_8.hidden_passage == True:
      room_22()
    elif current_room == 8 and choice.lower() == "east":
      room_3()
    elif current_room == 9 and choice.lower() == "north":
      room_7()
    elif current_room == 9 and choice.lower() == "south":
      room_13()
    elif current_room == 10 and choice.lower() == "east":
      room_14()
    elif current_room == 10 and choice.lower() == "west":
      room_7()
    elif current_room == 11 and choice.lower() == "north":
      room_6()
    elif current_room == 11 and choice.lower() == "south":
      room_12()
    elif current_room == 12 and choice.lower() == "west":
      room_16()
    elif current_room == 12 and choice.lower() == "south":
      room_15()
    elif current_room == 13 and choice.lower() == "west":
      room_17()
    elif current_room == 13 and choice.lower() == "north":
      room_9()
    elif current_room == 14 and choice.lower() == "west" and monster_in_room == False:
      room_10()
    elif current_room == 15 and choice.lower() == "north":
      room_12()
    elif current_room == 15 and choice.lower() == "east":
      room_18()
    elif current_room == 16 and choice.lower() == "east":
      room_12()
    elif current_room == 17 and choice.lower() == "south":
      room_18()
    elif current_room == 17 and choice.lower() == "east":
      room_13()
    elif current_room == 18 and choice.lower() == "north":
      room_17()
    elif current_room == 18 and choice.lower() == "west":
      room_15()
    elif current_room == 19 and choice.lower() == "west":
      room_4()
    elif current_room == 19 and choice.lower() == "north" and room_19.hidden_passage == True:
      room_20()
    elif current_room == 19 and choice.lower() == "east" and room_19.hidden_passage == True:
      room_21()
    elif current_room == 20 and choice.lower() == "north":
      room_24()
    elif current_room == 20 and choice.lower() == "south":
      room_19()
    elif current_room == 21 and choice.lower() == "west":
      room_19()
    elif current_room == 22 and choice.lower() == "north":
      room_23()
    elif current_room == 22 and choice.lower() == "east":
      room_8()
    elif current_room == 23 and choice.lower() == "south" and monster_in_room == False:
      room_22()
    elif current_room == 24 and choice.lower() == "west":
      room_25()
    elif current_room == 24 and choice.lower() == "south":
      room_20()
    elif current_room == 25 and choice.lower() == "east":
      room_24()
    else:
      print("You can't go that way.")
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

def room_2():
  global current_room
  current_room = 2
  print("You are standing at a crossroads. You can go north, south, east or west.")
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
  potion_in_room = True
  if choice.lower() == "examine potion" and "potion" in hero.inventory:
    print("This is a health potion. It fully restores your health points.")
  elif choice.lower() == "examine potion" and "potion" not in hero.inventory:
    print("You are not carrying any potion.")
  elif current_room == 15 and choice.lower() == "get potion" and potion_in_room == True:
    hero.inventory.append("potion")
    print("You pick up the potion and put it in your satchel.")
    potion_in_room = False
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
  elif current_room == 16 and choice.lower() == "get hammer" and chest.chest_open == True and hammer.hammer_in_chest == True:
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
    print("As soon as you receive the 3rd gemstone, you feel your health points increase.")
    hero.health = 45
  elif choice.lower() == "examine gemstone" and "gemstone" in hero.inventory:
    print("It is a blue gemstone.")
  elif choice.lower() == "examine gemstone" and "gemstone" not in hero.inventory:
    print("You don't have a gemstone.")
  game()

# functions for interactive objects
def bookcase():
  bookcase_full = False
  if current_room == 7 and bookcase_full == False:
    print("A large bookcase stands against the eastern wall. It's shelves are full of books, \
except for one space on the middle shelf.")
  elif current_room == 7 and bookcase_full == True:
    print("The large bookcase, now full of books, has slid to the side granting access to a secret passage to the east.")
  else:
    print("There is no bookcase here.")
  game()

def chest():
  chest_open = False
  if current_room == 16 and chest_open == False:
    print("It is a large metal chest. It has rust running along it's edges and is currently locked.")
  elif current_room == 16 and hammer.hammer_in_chest == True and chest.chest_open == True:
    print("The chest contains a Dwarven hammer.")
  elif current_room == 16 and hammer.hammer_in_chest == False and chest.chest_open == True:
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
  if current_room == 24 and has_eaten == False:
    print("There is an Old Man sitting against the northern wall. His clothes and hair are dirty and he looks very hungry.")
  elif current_room == 24 and has_eaten == True:
    print("The Old Man looks quite content now.")
  else:
    print("There is no Old Man here.")
  game()

def dwarf():
  has_hammer = False
  if current_room == 8 and has_hammer == False:
    print("There is a Dwarf pacing back and forth muttering something about misplacing an important item.")
  elif current_room == 8 and has_hammer == True:
    print("The Dwarf is sitting cross-legged on the floor cleaning his hammer.")
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
  elif choice.lower() == "examine gemstone":
    gems()
  elif choice.lower() == "inventory":
    print(hero.inventory)
    game()
  elif choice.lower() == "attack":
    hero.attack()
  elif choice.lower() == "examine bookcase":
    bookcase()
  elif choice.lower() == "put book in bookcase":
    hero.use_book()
  elif choice.lower() == "examine chest":
    chest()
  elif choice.lower() == "open chest":
    hero.use_key()
  elif choice.lower() == "examine stand":
    stand()
  elif choice.lower() == "put horn on stand":
    hero.use_horn()
  elif choice.lower() == "examine old man":
    old_man()
  elif choice.lower() == "give bread to old man" or choice.lower() == "eat bread":
    hero.use_bread()
  elif choice.lower() == "examine dwarf":
    dwarf()
  elif choice.lower() == "give hammer to dwarf":
    hero.use_hammer()
  elif choice.lower() == "drink potion":
    hero.use_potion()
  elif choice.lower() == "north" or choice.lower() == "south" or choice.lower() == "east" or choice.lower() == "west":
    hero.movement()
  elif choice.lower() == "help":
    print(commands)
    game()
  else:
    print("That won't work.")
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
monster_in_room = False
current_room = 0
choice = ""

print("The old man whispers something and you are suddenly surrounded by a thick black smoke. \
After a few moments the smoke clears and you look around.")

room_1()
