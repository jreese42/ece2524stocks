#!/usr/bin/env python

import random as rand
from trends import *
import time
class Stock:
	"""Stock class used in generating and simulating fake stocks"""
	scale = 1
	price = 0
	change = 0
	owned = 0
	trend_current = rand.randint(1,5)
	trend_prev = 1
	trend_status = 0
	trend_exit = 4
	trend_steady_state = 0
	prev_price = 0
	
	trend_die = {1: trend_steady,
		     2: trend_gen_rise,
		     3: trend_gen_fall,
		     4: trend_gr_rise,
		     5: trend_gr_fall}

	rand.seed(time.time())
	with open("name_prefix") as f:
		name1 = f.read().splitlines()
	with open("name_suffix") as f:
		name2 = f.read().splitlines()

	def __init__(self, scale_val = 1):
		self.scale = scale_val
		self.name = self.name1[rand.randint(0,len(self.name1)-1)] + " " + self.name2[rand.randint(0,len(self.name2)-1)]
		self.price = 10*scale_val
		self.trend = rand.randint(1,5)

	def simulate(self):
		#This function will simulate one day's change in a stock
		self.prev_price = self.price

		if (self.trend_status < self.trend_exit): #if in the middle of a trend already, continue
			self.trend_die[self.trend_current](self) #execute a trend to simulate one day
			self.trend_status += 1
		elif (self.trend_status == self.trend_exit): #if at and of trend, pick new trend and simulate
			#Reroll for a new trend
			prev = self.trend_current
			self.trend_status = 0
			while (self.trend_current == prev):
				self.trend_current = rand.randint(1,5)
			self.trend_steady_state = self.price
			#Execute the newly rolled trend
			self.trend_die[self.trend_current](self)

		#keep track of change between days
		self.change = self.price - self.prev_price

	def buy(self, amount):
		self.owned += amount
		return self.price*amount

	def sell(self, amount):
		self.owned -= 1
		return self.price*amount
