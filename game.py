import sys
import os
import random
import pickle

#WEAPONS

weaponsforsale ={"Sword":30,"Axe":15,"Potion":5}


# Classes
class Player:
	def __init__(self, name):
		self.name = name
		self.maxhealth = 100
		self.health = self.maxhealth
		self.attack = 5
		self.study = 10
		self.maxstudy = 120
		self.movement = 100
		self.weapon = ["Pocket Knife"]
		self.currentweapon = ["Pocket Knife"]
		self.gold = 40


		@property
		def attack(self):
			attack = self.attack
			if self.currentweapon == "Pocket Knife":
				self.attack == 6
			if self.currentweapon == "Sword":
				self.attack == 12
			if self.current.weapon == "Axe":
				self.attack == 9

			return attack

class Warrior:
	def __init__(self,name):
		self.name = name
		self.maxhealth = 100
		self.health = self.maxhealth
		self.attack = randint(5,10)

class Mage:
	def __init__(self,name):
		self.name = name
		self.maxhealth = 120
		self.health = self.maxhealth
		self.attack = randint(2,8)
# ----------------------------------------------
def main():
	print "Welcome to the Adventure Bandcom!"
	print "Press 1) to Enter the Game"
	print "Press 2) to Load"
	print "Press 3) to Quit the Game"
	decision = raw_input()
	if decision == "1":
		gamestart()
	elif decision == "2":
		if os.path.exists("savefile") == True:
			os.system('clear')
			with open('savefile', 'rb') as f:
				global PLAYERNAME
				PLAYERNAME = pickle.load(f)
			print "Game loaded"
			gamestart1()
		else:
			"There's not a saved file in your computer"
			main()
	elif decision == "3":
		sys.exit()
	else:
		main()

def gamestart():
	os.system('clear')
	print "Hello to the game! What is your name?"
	decision = raw_input(" ==> ")
	global PLAYERNAME
	PLAYERNAME = Player(decision)
	gamestart1()

def gamestart1():
	os.system('clear')
	print "Name %s" % PLAYERNAME.name
	print "Health %i/%i" % (PLAYERNAME.health, PLAYERNAME.maxhealth)
	print "Attack %i" % PLAYERNAME.attack
	print "Weapons: %s" % PLAYERNAME.currentweapon
	print "Gold: %s" % PLAYERNAME.gold
	print "1) Enter the City"
	print "2) Leave the City"
	print "3) Fight"
	print "4) Exit the Game"
	print "5) Inventory"
	print "6) Save"
	decision = raw_input(" ==> ")
	if decision == "1":
		city()

	elif decision == "2":
		awayfromcity()
	
	elif decision == "3":
		arena()
	
	elif decision == "4":
		sys.exit()

	elif decision == "5":
		inventory()
	
	elif decision == "6":
		os.system('clear')
		with open('savefile', 'wb') as f:
			pickle.dump(PLAYERNAME, f)
			print "Game has been saved!"
			decision = raw_input (" ==> ")
			gamestart1()
		
# CITY			

def city():
	print "Welcome to the City!"
	print "What would you like to do?"
	print " 1)Shop"
	print " 2)Buy a Book"
	print " 3)Buy a Horse"
	decision = raw_input(" ==> ")
	if decision == "1":
		shop()
	elif decision == "2":
		bookstore()
	elif decision == "3":
		horsebuyer()
		
def inventory():
	print "What would you like to do?"
	print "1) Equip Weapon"
	print "2) Go Back"
	decision = raw_input (" ==> ")
	if decision == "1" or "equip" or "one" or "equip weapon":
		equipment()
	elif decision == "back" "2" "goback" "go back":
		city()
		
def equipment():
	print "What would you like to equip?"
	for weapon in PLAYERNAME.weapon:
		print weapon
		print "Type B or Back to go back"
		decision = raw_input (" ==> ")
		if	decision == PLAYERNAME.current.weapon:
			equipment()
		elif decision == "b" or "back" or "Back":
			inventory()
		elif decision in PLAYERNAME.weapon:
			print "You have equipped %s" % decision
			decision = raw_input (" ==> ")
			equipment()
		else:
			print "You dont have %s in your inventory" % decision
			
		


# SHOP  --------------------------------

def shop():
	os.system('clear')
	print "Welcome to the Town Shop!"
	print "What are you going to buy?"
	print "1) Sword"
	print "2) Potion"
	print "3) Axe"
	print "4) Back"
	decision = raw_input (" ==> ")
	
	if decision in weaponsforsale:
		if PLAYERNAME.gold >= weaponsforsale[decision]:
			os.system('clear')
			PLAYERNAME.gold -= weaponsforsale[decision]
			PLAYERNAME.weapon.append(decision)
			print "You have bought %s" % decision
			decision = raw_input (" ==> ")
			gamestart1()
		else:
			os.system('clear')
			print "You don't have enough gold!"
			shop()
	elif decision == "back" or "b" or "ba" or "bac":
		gamestart1()
	
	else:
		print "This item doesn't exist!"
		shop()
			
		
		
		

	

main()
