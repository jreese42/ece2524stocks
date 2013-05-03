from stock import *
import random as rand
import time

stocks = []

def initStock():
	stocks[:] = []
	for num in range(10):
		stocks.append(Stock(num+1))

