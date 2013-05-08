from stock import *
from historic_stock import *
import random as rand
import time

stocks = []
alreadyUsed = []

def initStock(real):

	#clear lists upon init
	stocks[:] = []
	alreadyUsed[:] = []

	if (real == True):
		alreadyUsed.append("")
		for num in range(10):
			stocks.append(Historical_Stock(alreadyUsed))
			stocks[num].simulate()
			alreadyUsed.append(stocks[num].name)
	else:
		for num in range(10):
			stocks.append(Stock(rand.randint(1,10)))
			stocks[num].simulate()
