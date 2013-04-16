#!/usr/bin/env python

from stock import *
import sys
import random as rand
import time

stocks = []
cash = 100
rand.seed(time.time())

def show_stocks():
	for i,stock in enumerate(stocks):
		sys.stdout.write(str(i+1) + ") ")
		stock.show()

def sim_stocks():
	for stock in stocks:
		stock.simulate()

def trade_stocks(cash):
	while(1):
		print "\nYou have $" + str(cash) + "!"
		user_input = raw_input("Buy, sell, or done: ")
		split_input = user_input.split()
		if (split_input[0] == 'buy'):
			try:
				cash -= stocks[int(split_input[2])-1].buy(int(split_input[1]))
			except:
				print "Input Error: Try something else"
				print "Format: buy [number] [stock]"		  
		elif (split_input[0] == 'sell'):
			try:
				cash += stocks[int(split_input[2])-1].sell(int(split_input[1]))
			except:
				print "Input Error: Try something else"
				print "Format: sell [number] [stock]"
		elif (split_input[0] == "done"):
			break
		else:
			print "das wrong bro"
	return cash

#initialize the game
for num in range(10):
	stocks.append( Stock(num+1) )
while(1):
	sim_stocks()
	show_stocks()
	cash = trade_stocks(cash)
