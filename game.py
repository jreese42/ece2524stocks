#!/usr/bin/env python

from stock import *
import sys
import random as rand
import time

stocks = []
cash = 100
rand.seed(time.time())

def show_stocks():
	'''Prints out a formatted table of stock information'''
	sys.stdout.write("\n\n") #Print out table header
	sys.stdout.write("Num  |  Name                               |  Owned     |  Price     |  Change\n")
	sys.stdout.write("-"*5 + "|" + "-"*37 + "|" + "-"*12 + "|" + "-"*12 + "|" + "-"*9 + "\n")
	for i,stock in enumerate(stocks): #print stock info for each stock
		string = ""
		string += (str(i+1) + ")") #Stock number
		while (len(string) < 5): #Pad with spaces
			string += " "
		string += ("|  " + stock.name ) #Stock name
		while (len(string) < 43): #Pad with spaces
			string += " "
		string += ("|  " + str(stock.owned)) #Number of stock owned
		while (len(string) < 56): #Pad with spaces
			string += " "
		string += ("|  $" + str(stock.price)) #Stock Price
		while (len(string) < 69): #Pad with spaces
			string += " "
		string += "|  "
		if (stock.change < 0): #Change from previous day
			string += "-"
		else:
			string += "+"
		string += "$" + str(abs(stock.change))
		print string

def sim_stocks():
	'''Simulates one day by calling simulate on each stock'''
	for stock in stocks:
		stock.simulate()

def trade_stocks(cash):
	'''Opens stocks for trade by terminal'''
	while(1):
		print "\nYou have $" + str(cash) + "!"
		user_input = raw_input("Buy, sell, view, done, or exit: ")
		split_input = user_input.split()
		try: #try to use the input to make sure it's valid
			split_input[0]
		except IndexError:
			split_input = ['']
			sys.stdout.write("Input Error: You need to type something.\n")
		if (split_input[0] == 'buy'): #If user inputs buy
			try:
				#Call buy method on stock if enough cash
				if (cash >= (int(split_input[1])*stocks[int(split_input[2])-1].price)):
					cash -= stocks[int(split_input[2])-1].buy(int(split_input[1]))
					show_stocks()
				else:
					print "You don't have enough money for that!"

			except:
				print "Input Error: Try something else"
				print "Format: buy [number] [stock]"		  
		elif (split_input[0] == 'sell'): #If user inputs sell
				try:
					#Call sell method on stock if enough stocks owned
					own = stocks[int(split_input[2])-1].owned
					if (own >= int(split_input[1])):
						cash += stocks[int(split_input[2])-1].sell(int(split_input[1]))
						show_stocks()
					else:
						print "You don't own those stocks!"
				except:
					print "Input Error: Try something else"
					print "Format: sell [number] [stock]"
		elif (split_input[0] == "view"):
			show_stocks() #Print stock table when requested
		elif (split_input[0] == "done"):
			break #Exit the method when 'done'
		elif (split_input[0] == "exit"):
			quit()
		else:
			print "Please input only buy, sell, view, done, or exit.\nType buy or sell with no arguments to see usage."
	return cash #This is used to keep track of the global cash variable

#initialize the game
for num in range(10): #Create stocks
	stocks.append( Stock(num+1) )
try:
	while(1): #One 'day' is a simulation and a trading session
		sim_stocks()
		show_stocks()
		cash = trade_stocks(cash)
except:
	print "\nThanks for playing!\n"
	quit()
