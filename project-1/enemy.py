import RPi.GPIO as gpio
import time
import random

class goblinClass:
	hp = 3,
	attack = 1,
	defence = 1,
	name = "Goblin"

class zombieClass:
	hp = 3,
	attack = 2,
	defence = 0,
	name = "Zombie"

class skeletonClass:
	hp = 6,
	attack = 1,
	defence = 2,
	name = "Skeleton"

goblin = goblinClass()
zombie = zombieClass()
skeleton = skeletonClass()

enemies = [goblin, zombie, skeleton]
randomEnemy = rand.randint(0, len(enemies))

def chooseEnemy():
	randomEnemy = random.randint(0, len(enemies))
	printEnemy()

def printEnemy():
	print(randomEnemy)