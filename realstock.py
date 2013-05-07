#!/usr/bin/env python

import random as rand
from trends import *
import ystockquote as ystock
import datetime as dt

class realStock:
	"""Stock class used to pull historic data from yahoo stocks with ystockquote and datetime"""
	price = 0
	change = 0
	owned = 0
	prev_price = 0
	one_day = dt.timedelta(days=1) #used to move days forward
	stockDate = dt.date.today()

	def __init__(self, name, start_year, start_month, start_day):
		self.name = name.upper()
		try:
			self.stockDate = dt.date(start_year, start_month, start_day)
		except ValueError:
			print "Error: bad date"
		
		try:
			self.price = float(ystock.get_historical_prices(self.name, 
									self.stockDate.isoformat(),
									self.stockDate.isoformat() )[1][4])
		except IOError:
			name = ''
	def next_day(self):
		#This function will read the next days' stock closing price from yahoo
		self.stockDate = self.stockDate + self.one_day
		self.prev_price = self.price
		if not (self.name == ''): 
			self.price = float(ystock.get_historical_prices(self.name,
									self.stockDate.isoformat(), 
									self.stockDate.isoformat() )[1][4])

		#keep track of change between days
		self.change = self.price - self.prev_price

	def buy(self, amount):
		self.owned += amount
		return self.price*amount

	def sell(self, amount):
		self.owned -= amount
		return self.price*amount
