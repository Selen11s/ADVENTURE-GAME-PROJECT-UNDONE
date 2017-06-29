import sys
import os
import random

#WEAPONS 

weaponsforsale ={"Sword: 40"}


# Classes
class Player:
	def __init__(self, name):
		self.name = name
		self.maxhealth = 100 
		self.health = self.maxhealth
		self.attack = 10
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
				attack == 6
			elif self.currentweapon == "Sword":
				attack == 12
			elif self.current.weapon == "Axe":
				attack == 9
				
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
	print "Welcome to the ROPA GOGA!"
	print "Press 1) to Enter the Game"
	print "Press 2) to Load"
	print "Press 3) to Quit the Game"
	decision = raw_input()
	if decision == "1":
		gamestart()
	elif decision == "2":
		pass
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
	print "Name %s" % PLAYERNAME.name
	print "Health %i/%i" % (PLAYERNAME.health, PLAYERNAME.maxhealth)
	print "Attack %i" % PLAYERNAME.attack
	print "1) Enter the City"
	print "2) Leave the City"
	print "3) Fight"
	print "4) Exit the Game"
	decision = raw_input(" ==> ")
	if decision == "1":
		city()
	elif decision == "2":
		awayfromcity()
	elif decision == "3":
		arena()
	elif decision == "4":
		sys.exit()
		
		
def inventory():
	
	

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

# SHOP  --------------------------------

def shop():
	os.system('clear')
	print "Welcome to the Town Shop!"
	print "What are you going to buy?"
	print "1) Sword"
	print "2) Potions"
	print "3) Axe"
	decision = raw_input (" ==> ")
	
	if decision in weaponsforsale:
		if PLAYERNAME.gold >= weaponsforsale[decision]:
			os.system('clear')
		PLAYERNAME.gold -= weaponsforsale[decision]
		PLAYERNAME.weap.append(decision)
		print "You have bought %s" % decision
		shop()
	else:
		os.system('clear')
		print "You dont have enough money!"
		decision = raw_input(" ==> ")
		shop()
	

	
	

main()
