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

	def __init__(self, name, start_date):
		self.name = name.upper()
		try:
			self.stockDate = dt.date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10]))
		except ValueError:
			print "Error: bad date"
		except IndexError:
			print "Error: dates must be iso format"
		
		got_price = 0
		attempts = 0
		while not got_price and attempts < 5:
			try:
				self.price = float(ystock.get_historical_prices(self.name, 
										self.stockDate.isoformat(),
										self.stockDate.isoformat() )[1][4])
			except:
				self.stockDate = self.stockDate + self.one_day
				attempts += 1
			else:
				got_price = 1
		
		if self.price == 0:
			print "Unable to find stock name"
			
	def simulate(self):
		#This function will read the next days' stock closing price from yahoo
		self.stockDate = self.stockDate + self.one_day
		self.prev_price = self.price
		got_price = 0
		if not (self.name == ''): 
			got_price = 0
			attempts = 0
			while not got_price and attempts < 5:
				try:
					self.price = float(ystock.get_historical_prices(self.name, 
											self.stockDate.isoformat(),
											self.stockDate.isoformat() )[1][4])
				except:
					self.stockDate = self.stockDate + self.one_day
					attempts += 1
				else:
					got_price = 1

		#keep track of change between days
		self.change = self.price - self.prev_price

	def buy(self, amount):
		self.owned += amount
		return self.price*amount

	def sell(self, amount):
		self.owned -= amount
		return self.price*amount
