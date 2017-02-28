from __future__ import unicode_literals
from django.db import models
import random

# Create your models here.
class GoldGame(object):
	def __init__(self, click):
		self.click = click
		print 'GoldGame'
	# Function to return activity string from the dictionary bldgLegend to be placed into the list activity
	def getResponse(self, num):

		bldgLegend = {"farm": "Earned " + str(num) + " golds from the farm", "cave": "Earned " + str(num) + " golds from the cave", "house": "Earned " + str(num) + " golds from the house", "casino+": "Entered a casino and won " + str(num) + " golds...Yay!", "casino-" : "Entered a casino and lost " + str(num) + " golds...Ouch!"}

		bldgResponse = bldgLegend[self.click]

		return bldgResponse

	# Function to generate a random number for the game when envoked
	def randomGold(self):
		randFarm = random.randrange(9, 21)
		randCave = random.randrange(4, 11)
		randHouse = random.randrange(1, 6)
		randCasino = random.randrange(-51, 51)

		if self.click == "farm":
			return randFarm
		elif self.click == "cave":
			return randCave
		elif self.click == "house":
			return randHouse
		elif self.click == "casino":
			return randCasino

	# Function to determine whether a positive or negative result for casino activity should be generated
	def checkCasino(self, random):
		if random < 0:
			self.click = "casino-"
			response = self.getResponse(random)
		elif random >= 0:
			self.click = "casino+"
			response = self.getResponse(random)
		print self.click, random
		return response

	# Function to get the activity string
	def getActivity(self, random):
		if self.click =="casino":
			act = self.checkCasino(random)
		elif self.click == "farm":
			act = self.getResponse(random)
		elif self.click == "cave":
			act = self.getResponse(random)
		elif self.click == "house":
			act = self.getResponse(random)
		return act
