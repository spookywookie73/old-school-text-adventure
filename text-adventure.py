# importing the Random module
import random
# a list of monster names to be used when creating the monster classes
monster_list = ["Snivelling Goblin", "Dark Elf", "Cave Troll", "Giant Spider", "Dire Wolf"]

#creating the classes needed for the game
class Monster:
  # initialize the monster with a name and health
  def __init__(self, name, health):
    self.name = name
    self.health = health
  # a description of the monster class
  def __repr__(self):
    return "This is a {name}. It is a foul creature that has dwelled in this dungeon for far too long. \
It's health is {health}.".format(name = self.name, health = self.health)
  # create a module the monster class uses while attacking
  def attack(self):
    attack_damage = random.randint(3, 7) # chooses a random attack number within a range
    boss_attack_damage = random.randint(7, 15)
    if hero.health > 0 and current_monster == monster1 or hero.health > 0 and current_monster == monster2:
      hero.health -= attack_damage
      print("You are attacked by a {enemy} and take {damage} points of damage. Your health is now {health}.\
".format(damage = attack_damage, enemy = self.name, health = hero.health))
      
      if hero.health <= 0: # if your health is zero, you have died and the game will end
        print("The {enemy} lunges forward and inflicts a fatal blow. You crash to the floor, your breathing slows. \
As the light begins to fade you wonder if you were really ready for a challenge like this.".format(enemy = current_monster.name))
        print("Unfortunately, this is were your adventure ends. Goodbye.\n")
        exit()
      else:
        game() # if you don't die, the game will continue
    elif hero.health > 0 and current_monster == boss:
      hero.health -= boss_attack_damage
      print("A spell from the Drow Priestess hits you and inflicts {damage} points of damage. \
Your health is now {health}.".format(damage = boss_attack_damage, health = hero.health))
      
      if hero.health <= 0:
        print("The Dark Elf Priestess casts a spell at you and this time you don't recover. The light slips \
away and your adventure comes to an end. Goodbye.\n")
        exit()
      else:
        game()


class Adventurer:
  # initialize the adventurer class with a name, health, number of gems and inventory
  def __init__(self, name, health = 30, gems = 0, inventory = ["sword"]):
    self.name = name
    self.health = health
    self.gems = gems
    self.inventory = inventory
    
  def __repr__(self): # adventurer's description
    return "The name of this adventurer is {name}. {name}, with sword in hand, has bravely accepted the challenge to rid this \
dungeon of it's evil.".format(name = self.name)
  
  def health_points(self): #module to show health points
    if self.health > 1:
      print("You have {hp} health points.".format(hp = self.health))
    else:
      print("You have {hp} health point.".format(hp = self.health))
    game()
  # modules to use different items
  def use_book(self):
    global bookcase_full
    if current_room == 7 and "book" in self.inventory:
      print("You put the book back on it's shelf. As soon as you let go of the book the bookcase slides to it's left, \
revealing a hidden passage to the east.")
      bookcase_full = True
      self.inventory.remove("book")
    elif current_room == 7 and "book" not in self.inventory:
      print("You do not have a book.")
    else:
      print("There is no bookcase here.")
    game()

  def use_bread(self):
    global has_eaten
    if current_room == 24 and choice.lower() == "give bread to old man" and "bread" in self.inventory:
      print("The Old Man smiles, thanks you for your generosity and gives you a gemstone.")
      has_eaten = True
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
    global horn_on_stand
    if current_room == 19 and "horn" in self.inventory:
      print("You place the horn onto the stand. The stand begins to vibrate and then lowers several inches \
into the ground. As it lowers, two doorways to the north and east appear.")
      horn_on_stand = True
      self.inventory.remove("horn")
    elif current_room == 19 and "horn" not in self.inventory:
      print("You are not carrying a horn.")
    else:
      print("There is no stand here.")
    game()

  def use_hammer(self):
    global has_hammer
    if current_room == 8 and "hammer" in self.inventory:
      print("The Dwarf takes the hammer from you. He stares at it for a few seconds, and then with a sudden swing of his arms, \
he smashes a large pile of rocks to dust leaving a doorway to the west.")
      self.inventory.remove("hammer")
      has_hammer = True
    elif current_room == 8 and "hammer" not in self.inventory:
      print("You do not have a hammer.")
    else:
      print("There is no Dwarf here.")
    game()

  def use_key(self):
    global chest_open
    if current_room == 16 and "key" in self.inventory:
      print("You take the key from your pocket and open the chest.")
      self.inventory.remove("key")
      chest_open = True
    elif current_room == 16 and chest.chest_open == True:
      print("The chest is already open.")
    elif current_room == 16 and chest.chest_open == False and "key" not in self.inventory:
      print("You do not have a key.")
    else:
      print("There is no chest here.")
    game()

  def attack(self): # module for attacking different monsters
    global monster1_alive
    global monster2_alive
    attack_points = random.randint(8, 18)
    if current_room == 14 and monster1_alive == True and current_monster.health > 0:
      current_monster.health -= attack_points
      print("You hit the {enemy} with your sword inflicting {damage} points of damage. Its health \
is now {health}.".format(enemy = current_monster.name, damage = attack_points, health = current_monster.health))
      
      if current_monster.health <= 0:
        print("You have defeated the {enemy}. You search the area and pickup a gemstone.".format(enemy = current_monster.name))
        monster1_alive = False
        self.gems += 1
        self.inventory.append("gemstone")
        gems()
      else:
        current_monster.attack()

    elif current_room == 23 and monster2_alive == True and current_monster.health > 0:
      current_monster.health -= attack_points
      print("You hit the {enemy} with your sword inflicting {damage} points of damage. Its health \
is now {health}.".format(enemy = current_monster.name, damage = attack_points, health = current_monster.health))
      
      if current_monster.health <= 0:
        print("You have defeated the {enemy}. You search the area and pickup a gemstone.".format(enemy = current_monster.name))
        monster2_alive = False
        self.gems += 1
        self.inventory.append("gemstone")
        gems()
      else:
        current_monster.attack()

    elif current_room == 25:
      current_monster.health -= attack_points
      print("You slice at the {boss} inflicting {damage} points of damage. Her health is now \
{health}.".format(boss = current_monster.name, damage = attack_points, health = current_monster.health))
      
      if current_monster.health <= 0: # if the boss is defeated, you win and the game ends
        print("With a lunging blow, you defeat the Dark Elf Priestess. The darkness that enveloped the \
dungeon has lifted. The Wizard appears in front of you. He hands you a bag of gold coins and thanks you for \
everything you have done. Before you have a chance to respond, he snaps his fingers and you find yourself back in your home.\n")
        print("Thankyou for playing my little adventure.\n")
        exit()
      else:
        current_monster.attack()
    else:
      print("There is nothing to attack.")
    game()

  def movement(self): # module for moving from room to room
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
      room_19()
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
    elif current_room == 7 and choice.lower() == "east" and bookcase_full == True:
      room_10()
    elif current_room == 8 and choice.lower() == "west" and has_hammer == True:
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
    elif current_room == 12 and choice.lower() == "north":
      room_11()
    elif current_room == 12 and choice.lower() == "west":
      room_16()
    elif current_room == 12 and choice.lower() == "south":
      room_15()
    elif current_room == 13 and choice.lower() == "west":
      room_17()
    elif current_room == 13 and choice.lower() == "north":
      room_9()
    elif current_room == 14 and choice.lower() == "west" and monster1_alive == False:
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
    elif current_room == 19 and choice.lower() == "north" and horn_on_stand == True:
      room_20()
    elif current_room == 19 and choice.lower() == "east" and horn_on_stand == True:
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
    elif current_room == 23 and choice.lower() == "south" and monster2_alive == False:
      room_22()
    elif current_room == 24 and choice.lower() == "west":
      room_25()
    elif current_room == 24 and choice.lower() == "south":
      room_20()
    else:
      print("You can't go that way.")
    game()


# functions for the rooms with descriptions
def room_1():
  global current_room
  current_room = 1
  print("You are standing in a small room. There is a doorway to the north.")
  game()

def room_2():
  global current_room
  current_room = 2
  print("You are standing at a crossroads. You can go north, south, east or west.")
  game()

def room_3():
  global current_room
  current_room = 3
  print("You are in a dimly lit room. You can go south, east or west.")
  game()

def room_4():
  global current_room
  current_room = 4
  if key_in_room == True:
    print("You are in a small room. There are skeletal remains on the floor. You can see a key \
amongst the bones. You can go south or east.")
  else:
    print("You are in a small room. There are skeletal remains on the floor. You can go south or east.")
  game()

def room_5():
  global current_room
  current_room = 5
  if bread_in_room == True:
    print("You are in a small room. There is a table with scraps of food on it against the eastern wall. \
Surprisingly, there is also an untouched loaf of bread. You can go south or west.")
  else:
    print("You are in a small room. There is a table with scraps of food on it against the eastern wall. \
You can go south or west.")
  game()

def room_6():
  global current_room
  current_room = 6
  print("You are in a dark room. The only light you see comes from the north or the south.")
  game()

def room_7():
  global current_room
  current_room = 7
  if bookcase_full == True:
    print("You are in a room with a bookcase against the corner of the eastern wall. You can go north, \
south or east.")
  else:
    print("You are in a room with a bookcase against the eastern wall. You can go north or south.")
  game()

def room_8():
  global current_room
  current_room = 8
  if has_hammer == True:
    print("You are in a room illuminated by a dozen or so large candles. There is a Dwarf sitting on the floor. \
You can go east or west.")
  else:
    print("You are in a room illuminated by a dozen or so large candles. There is a Dwarf pacing around the room. \
You can only go back to the east.")
  game()

def room_9():
  global current_room
  current_room = 9
  print("You are in a narrow corridor. You can go north or south.")
  game()

def room_10():
  global current_room
  current_room = 10
  print("You are in a tight walkway that has been carved out of the rock. You can go east or west.")
  game()

def room_11():
  global current_room
  current_room = 11
  if book_in_room == True:
    print("You are in a long corridor. There is a small table off to the side with a book on it. You can go north or south.")
  else:
    print("You are in a long corridor. There is a small table off to the side. You can go north or south.")
  game()

def room_12():
  global current_room
  current_room = 12
  print("You are in a long corridor. You can go north, south or west.")
  game()

def room_13():
  global current_room
  current_room = 13
  print("You are standing in a damp, cold room. You can go north or west.")
  game()

def room_14():
  global current_room
  global current_monster
  current_room = 14
  current_monster = monster1
  if monster1_alive == True: # if a monster is in the room it attacks you
    print("You are in a large room. The eastern side of the room is covered in a strange mist.")
    current_monster.attack()
  elif monster1_alive == False:
    print("You are in a large room. The corpse of a {enemy} lies on the floor. You can only go west.".format(enemy = current_monster.name))
  game()

def room_15():
  global current_room
  current_room = 15
  if potion_in_room == True:
    print("You are in a small room. There are broken bottles scattered across the floor. Amongst the bottles you see \
a vial of potion. You can go north or east.")
  else:
    print("You are in a small room. There are broken bottles scattered across the floor. You can go north or east.")
  game()

def room_16():
  global current_room
  current_room = 16
  if chest_open == True:
    print("You see an open chest with a beam of sunlight shining upon it in the middle of the room. You can go east.")
  else:
    print("You see a chest with a beam of sunlight shining upon it in the middle of the room. You can go east.")
  game()

def room_17():
  global current_room
  current_room = 17
  if horn_in_room == True:
    print("You are in a small room. You see a single, lit candle. Above it, hanging on the wall, is a bulls horn. You can go south or east.")
  else:
    print("You are in a small room. You see a single, lit candle, flickering in the slight breeze. You can go south or east.")
  game()

def room_18():
  global current_room
  current_room = 18
  print("You are in a small walkway. The ceiling is too low to stand so you have to crawl on your hands and knees. You can go north or west.")
  game()

def room_19():
  global current_room
  current_room = 19
  if horn_on_stand == True:
    print("You are in a brightly lit room. There is a humming noise in the air. You can see a small stand, \
with a horn on top of it, in the middle of the room. You can go north, east or west.")
  else:
    print("There is a stand in the middle of this dimly lit room. You can only go west.")
  game()

def room_20():
  global current_room
  current_room = 20
  print("You are in a short corridor. You can go north or south.")
  game()

def room_21():
  global current_room
  current_room = 21
  print("You are in a small room. You can only go west.")
  game()

def room_22():
  global current_room
  current_room = 22
  print("You are standing in a crooked shaped room. You can hear a noise coming from the north. \
You can go north or east.")
  game()

def room_23():
  global current_room
  global current_monster
  current_room = 23
  current_monster = monster2
  if monster2_alive == True:
    print("You are in a large room. There is a strange sound emanating from the shadows.")
    current_monster.attack()
  elif monster2_alive == False:
    print("You are in a large room. The corpse of a {enemy} lies on the floor. You can only go south.".format(enemy = current_monster.name))
  game()

def room_24():
  global current_room
  current_room = 24
  print("You are in a small room. Litter is strewn across the floor. There is an Old Man sitting silently, looking at you. \
You can go south or west.")
  game()

def room_25():
  global current_room
  global current_monster
  current_room = 25
  current_monster = boss
  print("You enter a darkened room. A Dark Elf Priestess walks out of the shadows. She screams that this is the \
last place you will ever see, then casts a spell at you.")
  current_monster.attack()
 

# functions to get the items, with descriptions
def sword():
  print("This is a medium sized sword. The handle is in good condition and the blade is surprisingly sharp.")
  game()

def horn():
  global horn_in_room
  if choice.lower() == "examine horn" and "horn" in hero.inventory:
    print("This is an ordinary looking bulls horn used for making a noise.")
  elif choice.lower() == "examine horn" and "horn" not in hero.inventory:
    print("You do not have a horn.")
  elif current_room == 17 and choice.lower() == "get horn" and horn_in_room == True:
    hero.inventory.append("horn")
    print("You pick up the horn and put it in your satchel.")
    horn_in_room = False
  elif choice.lower() == "get horn" and "horn" in hero.inventory:
    print("The only horn available is in your satchel.")
  else:
    print("There is no horn to pick up.")
  game()

def bread():
  global bread_in_room
  if choice.lower() == "examine bread" and "bread" in hero.inventory:
    print("This is a freshly baked small loaf of bread. It's still warm and smells delicious.")
  elif choice.lower() == "examine bread" and "bread" not in hero.inventory:
    print("You do not have any bread.")
  elif current_room == 5 and choice.lower() == "get bread" and bread_in_room == True:
    hero.inventory.append("bread")
    print("You pick up the bread and put it in your satchel.")
    bread_in_room = False
  elif choice.lower() == "get bread" and "bread" in hero.inventory:
    print("The only bread available is in your satchel.")
  else:
    print("There is no bread to pick up.")
  game()

def key():
  global key_in_room
  if choice.lower() == "examine key" and "key" in hero.inventory:
    print("This is a medium sized key suitable for opening a chest.")
  elif choice.lower() == "examine key" and "key" not in hero.inventory:
    print("You do not have a key.")
  elif current_room == 4 and choice.lower() == "get key" and key_in_room == True:
    hero.inventory.append("key")
    print("You pick up the key and put it in your pocket.")
    key_in_room = False
  elif choice.lower() == "get key" and "key" in hero.inventory:
    print("The only key here is in your pocket.")
  else:
    print("There is no key to pick up.")
  game()

def potion():
  global potion_in_room
  if choice.lower() == "examine potion" and "potion" in hero.inventory:
    print("This is a health potion. It fully restores your health points.")
  elif choice.lower() == "examine potion" and "potion" not in hero.inventory:
    print("You are not carrying any potion.")
  elif current_room == 15 and choice.lower() == "get potion" and potion_in_room == True:
    hero.inventory.append("potion")
    print("You pick up the potion and put it in a pouch on your belt.")
    potion_in_room = False
  elif choice.lower() == "get potion" and "potion" in hero.inventory:
    print("The only potion here is attached to your belt.")
  else:
    print("There is no potion to pick up.")
  game()

def hammer():
  global hammer_in_chest
  if choice.lower() == "examine hammer" and "hammer" in hero.inventory:
    print("This is a magnificent hammer. It has dwarven runes engraved down the handle and the head is unblemished.")
  elif choice.lower() == "examine hammer" and "hammer" not in hero.inventory:
    print("You are not carrying a hammer.")
  elif current_room == 16 and choice.lower() == "get hammer" and chest_open == True and hammer_in_chest == True:
    hero.inventory.append("hammer")
    print("You pick up the hammer and put it in your satchel.")
    hammer_in_chest = False
  elif choice.lower() == "get hammer" and "hammer" in hero.inventory:
    print("You are already carrying the hammer.")
  else:
    print("There is no hammer to pick up.")
  game()

def book():
  global book_in_room
  if choice.lower() == "examine book" and "book" in hero.inventory:
    print("The book is standard sized. The front and back covers are creased and it's title is 'The Secret Passage'.")
  elif choice.lower() == "examine book" and "book" not in hero.inventory:
    print("You do not have a book.")
  elif current_room == 11 and choice.lower() == "get book" and book_in_room == True:
    hero.inventory.append("book")
    print("You pick up the book and put it in your satchel.")
    book_in_room = False
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
  global bookcase_full
  if current_room == 7 and bookcase_full == False:
    print("A large bookcase stands against the eastern wall. It's shelves are full of books, \
except for one space on the middle shelf.")
  elif current_room == 7 and bookcase_full == True:
    print("The large bookcase, now full of books, has slid to the side granting access to a secret passage to the east.")
  else:
    print("There is no bookcase here.")
  game()

def chest():
  global chest_open
  global hammer_in_chest
  if current_room == 16 and chest_open == False:
    print("It is a large metal chest. It has rust running along it's edges and is currently locked.")
  elif current_room == 16 and hammer_in_chest == True and chest_open == True:
    print("The chest contains a Dwarven hammer.")
  elif current_room == 16 and hammer_in_chest == False and chest_open == True:
    print("The large chest lies open and empty.")
  else:
    print("There is no chest here.")
  game()

def stand():
  global horn_on_stand
  if current_room == 19 and horn_on_stand == False:
    print("The ornate marble stand has a flat top, and down the side, an engraving of a man blowing a horn.")
  elif current_room == 19 and horn_on_stand == True:
    print("The ornate stand is now shorter than it was and now has a horn placed upon it.")
  else:
    print("There is no stand in this room.")
  game()

def old_man():
  global has_eaten
  if current_room == 24 and has_eaten == False:
    print("There is an Old Man sitting against the northern wall. His clothes and hair are dirty and he looks very hungry.")
  elif current_room == 24 and has_eaten == True:
    print("The Old Man looks quite content now.")
  else:
    print("There is no Old Man here.")
  game()

def dwarf():
  global has_hammer
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
  choice = input("\nWhat do you want to do? : ")
  if choice.lower() == "health":
    hero.health_points()
  elif choice.lower() == "examine sword":
    print("This is a medium sized sword. The handle is in good condition and the blade is surprisingly sharp.")
    game()
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
    print("You are carrying {items}.".format(items = hero.inventory))
    game()
  elif choice.lower() == "attack" or choice.lower() == "attack monster":
    hero.attack()
  elif choice.lower() == "examine bookcase":
    bookcase()
  elif choice.lower() == "put book in bookcase":
    hero.use_book()
  elif choice.lower() == "examine chest":
    chest()
  elif choice.lower() == "open chest" or choice.lower() == "unlock chest":
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
  elif choice.lower() == "drink potion" or choice.lower() == "use potion":
    hero.use_potion()
  elif choice.lower() == "north" or choice.lower() == "south" or choice.lower() == "east" or choice.lower() == "west":
    hero.movement()
  elif current_room == 7 and bookcase_full == False and choice.lower() == "help":
    print("Maybe you could put something in the bookcase.")
    game()
  elif current_room == 8 and has_hammer == False and choice.lower() == "help":
    print("You could try to find his lost item and give it to him.")
    game()
  elif current_room == 19 and horn_on_stand == False and choice.lower() == "help":
    print("Try to put something on the stand.")
    game()
  elif current_room == 24 and has_eaten == False and choice.lower() == "help":
    print("Give something to him to eat.")
    game()
  elif choice.lower() == "hero":
    print(hero)
    game()
  else:
    print("That can't do that. Try again.")
    game()


# start of game with introduction
print("You are standing in a candle lit room. Behind a table, thumbing through multiple books, \
stands an old man wearing what appears to be a wizard's robe. He looks at you and start's to talk. \
'Welcome brave adventurer, I have a quest for you. I need you to clear this dungeon of the evil that dwells there. \
If you complete this task you will be handsomely rewarded. Good Luck!'\n")
heroes_name = input("Please input your name and press enter to begin. : ") # store adventurers name

hero = Adventurer(heroes_name) # creat the adventurer class
# create the monster classes with random names and health points
monster1 = Monster(random.choice(monster_list), random.randint(10, 25))
monster2 = Monster(random.choice(monster_list), random.randint(10, 25))
#create the end monster with specific name and health points
boss = Monster("Dark Elf Priestess", 50)

# variables used in the game
current_monster = monster1
current_room = 0
choice = ""
bread_in_room = True
key_in_room = True
horn_in_room = True
potion_in_room = True
hammer_in_chest = True
book_in_room = True
bookcase_full = False
chest_open = False
horn_on_stand = False
has_eaten = False
has_hammer = False
monster1_alive = True
monster2_alive = True

print("\nThe old man whispers something and you are suddenly surrounded by a thick black smoke. \
After a few moments the smoke clears and you look around.\n")
# start in room 1
room_1()
