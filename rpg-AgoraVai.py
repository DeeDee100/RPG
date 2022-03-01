from random import randint

class Char:
	def __init__(self, name, classe):
		self.name = name
		self.health = 10
		self.classe = classe
	
	def attack(self, enemy):
		damage = min()