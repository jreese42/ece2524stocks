#!/usr/bin/env python

from stock import *
import sys
import random as rand
import time

stocks = []
cash = 100
rand.seed(time.time())

def show_stocks():
	sys.stdout.write("\n\n") #Table header
	sys.stdout.write("Num  |  Name                               |  Owned     |  Price     |  Change\n")
	sys.stdout.write("-"*5 + "|" + "-"*37 + "|" + "-"*12 + "|" + "-"*12 + "|" + "-"*9 + "\n")
	for i,stock in enumerate(stocks):
		string = ""
		string += (str(i+1) + ")")
		while (len(string) < 5):
			string += " "
		string += ("|  " + stock.name )
		while (len(string) < 43):
			string += " "
		string += ("|  " + str(stock.owned))
		while (len(string) < 56):
			string += " "
		string += ("|  $" + str(stock.price))
		while (len(string) < 69):
			string += " "
		string += "|  "
		if (stock.change < 0):
			string += "-"
		else:
			string += "+"
		string += "$" + str(abs(stock.change))
		print string

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
				if (cash >= (int(split_input[1])*stocks[int(split_input[2])-1].price)):
					cash -= stocks[int(split_input[2])-1].buy(int(split_input[1]))
				else:
					print "You don't have enough money for that!"

			except:
				print "Input Error: Try something else"
				print "Format: buy [number] [stock]"		  
		elif (split_input[0] == 'sell'):
				try:
					own = stocks[int(split_input[2])-1].owned
					if (own >= int(split_input[1])):
						cash += stocks[int(split_input[2])-1].sell(int(split_input[1]))
					else:
						print "You don't own those stocks!"
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
