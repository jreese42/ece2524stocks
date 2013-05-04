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
	
	rand.seed(time.time())
	#Set up for random name generator
	with open("name_prefix") as f:
		name1 = f.read().splitlines()
	with open("name_suffix") as f:
		name2 = f.read().splitlines()

	def __init__(self):
		temp = rand.randint(1, 14)

		#Fill price_array with the various costs
		if (temp == 1):
			self.price_array = fillArray('AAME')
		elif (temp == 2):
			self.price_array = fillArray('AMAT')
		elif (temp == 3):
			self.price_array = fillArray('BA')
		elif (temp == 4):
			self.price_array = fillArray('CF')
		elif (temp == 5):
			self.price_array = fillArray('GE')
		elif (temp == 6):
			self.price_array = fillArray('GOOG')
		elif (temp == 7):
			self.price_array = fillArray('GRT')
		elif (temp == 8):
			self.price_array = fillArray('MSFT')
		elif (temp == 9):
			self.price_array = fillArray('NTAP')
		elif (temp == 10):
			self.price_array = fillArray('SNE')
		elif (temp == 11):
			self.price_array = fillArray('SPG')
		elif (temp == 12):
			self.price_array = fillArray('VZ')
		elif (temp == 13):
			self.price_array = fillArray('WDC')
		elif (temp == 14):
			self.price_array = fillArray('YHOO')

		self.name = self.name1[rand.randint(0,len(self.name1)-1)] + " " + self.name2[rand.randint(0,len(self.name2)-1)]
		self.price = self.price_array[self.index_in_price_array] #set price equal to first element in the price array


	def simulate(self):
		self.prev_price = self.price
		self.index_in_array += 1  #increment the index 
		self.price = self.price_array[self.index_in_array] #set the new price equal to the corresponding element in the array

		#keep track of the day-to-day change
		self.change = self.price - self.prev_price

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
