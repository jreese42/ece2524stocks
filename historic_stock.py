#!/usr/bin/env python

import csv
import sys
import random as rand
import time

class Historical_Stock:
	"""Stock class used in generating and simulating historical stocks"""
	scale = 1
	price = 0
	change = 0
	owned = 0
	prev_price = 0
	price_array = []
	index_in_price_array = 0
	name = ""
<<<<<<< HEAD
	company = ""
=======
>>>>>>> brian_dev
	
	rand.seed(time.time())

	def __init__(self, alreadyUsed):

		while (self.name in alreadyUsed):
			temp = rand.randint(1, 14)	

			#Fill price_array with the various costs
			if (temp == 1):
				self.price_array = fillArray('AAME')
				self.name = "Atlantic American Coorporation"
			elif (temp == 2):
				self.price_array = fillArray('AMAT')
				self.name = "Applied Materials, Inc."
			elif (temp == 3):
				self.price_array = fillArray('BA')
				self.name = "Boeing"
			elif (temp == 4):
				self.price_array = fillArray('CF')
				self.name = "CF Indistries Holdings"
			elif (temp == 5):
				self.price_array = fillArray('GE')
				self.name = "General Electric"
			elif (temp == 6):
				self.price_array = fillArray('GOOG')
				self.name = "Google"
			elif (temp == 7):
				self.price_array = fillArray('GRT')
				self.name = "Glimcher Realty Trust"
			elif (temp == 8):
				self.price_array = fillArray('MSFT')
				self.name = "Microsoft"
			elif (temp == 9):
				self.price_array = fillArray('NTAP')
				self.name = "NetApp"
			elif (temp == 10):
				self.price_array = fillArray('SNE')
				self.name = "Sony"
			elif (temp == 11):
				self.price_array = fillArray('SPG')
				self.name = "Simon Property Group"
			elif (temp == 12):
				self.price_array = fillArray('VZ')
				self.name = "Verizon"
			elif (temp == 13):
				self.price_array = fillArray('WDC')
				self.name = "Western Digital Corp."
			elif (temp == 14):
				self.price_array = fillArray('YHOO')
				self.name = "Yahoo! Inc."

		self.price = self.price_array[self.index_in_price_array] #set price equal to first element in the price array
<<<<<<< HEAD
		self.price = float('%.2f' % self.price)
=======
>>>>>>> brian_dev

	def simulate(self):
		self.prev_price = self.price
		self.index_in_price_array += 1  #increment the index
		self.index_in_price_array %= len(self.price_array) #make sure the index doesn't roll over
		self.price = self.price_array[self.index_in_price_array] #set the new price equal to the corresponding element in the array
<<<<<<< HEAD
		self.price = float('%.2f' % self.price)

		#keep track of the day-to-day change
		self.change = self.price - self.prev_price
=======

		#keep track of the day-to-day change
		self.change = float(self.price) - float(self.prev_price)
>>>>>>> brian_dev

	def buy(self, amount):
		self.owned += amount
		return self.price * amount

	def sell(self, amount):
		self.owned -= amount
		return self.price * amount


def fillArray(ticker):
	temp_arr = []
	csvPath = 'stock_histories/' + ticker + '_historical_data.csv'
	f = open(csvPath)
	reader = csv.reader(f)
	for row in reader:
		if (row[1] != 'Open'):
			temp_arr.append(row[1])

	return temp_arr
