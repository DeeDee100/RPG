import random as rd
import time


def combat(lvl_inimigo):
	pv_inimigo = lvl_inimigo * 10 + 10
	atck_max = lvl_inimigo * 3
	df_inimigo = lvl_inimigo * 3
	enemy_defence_turn = 0
	while pv_inimigo > 0 and char['PV'] > 0:
		print(f"\n \n  Enemy Stats  PV: {pv_inimigo}  || atck_max: {atck_max}")
		action = input("\nDo you wawnt to attack or defend? [attack/defend]")
		if action.lower() == 'attack':
			atck_turn = rd.randint(char['atck_char'], char['atck_char'] * 2)
			damage = atck_turn - enemy_defence_turn
			pv_inimigo -= damage
			print(
				f'\nYou did {atck_turn} damage in the enemy! It has now {pv_inimigo} of health'
			)
			print("\nEnemy's turn!")
		else:
			df_turn = char['df_char'] * 2
			print(f"\nYou choose to defend. Defense = {df_turn}")
			print("\nEnemy's turn!")
			if pv_inimigo <= 0:
				print("\n \n-------Congratz, you won the battle!---\n \n")
				return 1
		enmy_a_or_df = rd.randint(0, 2)
		if enmy_a_or_df != 0:
			enemy_atck = rd.randint(0, atck_max)
			damage = enemy_atck - char['df_char']
			if damage > 0:
				char['PV'] -= damage
				print(
					f" Enemy attacked with {enemy_atck}! You have now {char['PV']} health"
				)
				time.sleep(1)
			else:
				print(f"Enemy attacked with {enemy_atck}! it did 0 damage")
				time.sleep(1)
		else:
			enemy_defence_turn = rd.randint(lvl_inimigo, df_inimigo)
			print('Enemy is defending!')
			time.sleep(1)
	if pv_inimigo <= 0:
		print("\n \n-------Congratz, you won the battle!---\n \n")
		return 1
	else:
		print("\n \n-------------YOU DIED!----------- \n \n")
		return 0



def menu(resposta):
	if resposta.lower() == 'combat':
		return 1
	elif resposta.lower() == 'bar':
		return 2
	else:
		print("Sorry, i can't uderstand. Can you repeat?")
		return 0

def bar():
	print("\n Welcome to the Bar!")
	a = input("Do you want to sleep?[Y/N] ")
	if a.lower() =='y':
		char['PV'] = char['pv_max']
		print("PV restaured")
	else:
		print("Okey, see ya later")

""" 
def merchant():
	print("\n \n Welcome to the merchant\n\n")
	sword_atck1 = rd.randint(char["lvl"],char['atck_char'] * 2)
	sword_price1 = int(sword_atck1 / 2)
	sword_atck2 = rd.randint(char["lvl"],char['atck_char'] * 2)
	sword_price2 = int(sword_atck2 / 2)
	satff_atck1 = rd.randint(char["lvl"],char['atck_char'] * 2)
	staff_price1 = rd.randint(1, int(satff_atck1/2))
	satff_atck2 = rd.randint(char["lvl"],char['atck_char'] * 2)
	staff_price2 = rd.randint(1, int(satff_atck2/2))
	armour1 = rd.randint(char["lvl"],char['df_char'] * 2)
	armour1_price = int(armour1 / 2)
	armour2 = rd.randint(char["lvl"],char['df_char'] * 2)
	armour2_price = int(armour2 / 2)

	print(f"\nHere is my stock:\nArmour1:DF:{armour1} Price: {armour1_price}  |  Armour2 DF:{armour2} Price:{armour2_price}")
	print(f"\nSword1:{sword_atck1} Price: {sword_price1}  |  Sword2:{sword_atck2} Price:{sword_price2}")
	print(f"\nstaff1:{satff_atck1} Price:{staff_price1}  |  Staff2:{satff_atck2} PRice:{staff_price2}")
	purchase = input("Which one would you like to buy ?\n[sword1, sword1, staff1, staff2, armour1 or armour2]: ")
	print(purchase)

 """


#----------------------------------LVL 1------------------
def woods_1():
	print("You walk through the main road on Elantris until see the gate to the woods.\n\
	There, you find some guards watcing the place, then finally enter the florest.")
	print("Not long after, ya find some bandit trying to sneak by. Unfortunally, he sees you too.")
	time.sleep(2)
	combat(1)








var = False
while not var:
	name = input("What's ya name?")
	idade = input("Age?")
	try:
		int(idade)
	except:
		while True:
			print("Ya didn't put a number, please put a valid answer")
			idade = input("Age?")
			try:
				int(idade)
				break
			except:
				pass

	class_choosen = input(
		"[Please choose between the following classes.: Warrior or Mage] ")

	if class_choosen.lower() != 'warrior' and class_choosen.lower() != 'mage':

		while True:
			print("Class invalid!")
			print("Please choose again...")
			class_choosen = input(
				"[Please choose between the following classes.: Warrior or Mage]"
			)
			if class_choosen.lower() == 'mage' or class_choosen.lower(
			) == 'warrior':
				break

	print('\nSo,', name, 'you are a', class_choosen, 'with', idade, 'ages of experience?')
	a = input('Is that correct? \n Y/N  ').upper()

	if a == 'Y':
		print("Great! Let's start our journey then...")
		var = True
	else:
		print("Oh boy...")

char = {
	'nome': name,
	'idade': idade,
	'class': class_choosen,
	'pv_max': 50,
	'PV': 50,
	'PM': 50,
	'df_char': 1,
	'atck_char': 3,
	'lvl': 1,
	'gold': 10
}
"""
print(
	f"\nHello to Elantris {char['nome']}, here the citizens are suffering from a unknown disease that transforms then into zombies.")
print(
	"Are you the one to find the source of this evil and bring peace once again for this kingdon ?"
)
time.sleep(2)
print("\nWell, you will need to start from the basics.")
print(
	f"\n\nHere is your start status:\n50 PV | 50 PM | Attack: 3 | Defense: 1 | Gold: 10\n"
)
print("Let's start the training.\nHere is a training dummy.")
time.sleep(1)
combat(0)
print("Great, you learn fast, let's Explore the city.")

print("Here in the center of Elantris you can go to the Bar, there you can sleep an regenerat PV and PM. ")
print("\nNow, I have a quest for you. Some low bandits are trying to enter the city, you could help the guards with some of them by the florest.")
print("It will be simple for you, I'm sure.You can choose to go now or go to the Bar first")"""

next_move = input(["combat // Bar"])
next = menu(next_move)

if next == 1:
	woods_1()
elif next == 2:
	bar()
else:
	while next == 0:
		next_move = input(["combat or Bar"])
		next = menu(next_move)
		if next == 1:
			print(next)
		elif next == 2:
			bar()

print("------EOF-----------")







"""
---------------for later------------
print("In order to find out what is happening we sent a squad in a mission into the florest\nto find\
the Book of the World.")
print("This book has some of the oldest spells and tales of our people, some rumors say that it also have the answer for this curse.")
print("But the squad never returnded. Can you go look for them ?")
"""
