import random as rand
def trend_steady(self):
	self.trend_exit = 3
	if (self.price >= self.trend_steady_state + 2*self.scale):
		#Case: upper steady bound
		self.price = self.price + rand.randint(-2*self.scale,-self.scale)
		self.price = float('%.2f' % self.price)
	elif (self.price <= self.trend_steady_state - 2*self.scale):
		#Case: lower steady bound
		self.price = self.price + rand.randint(self.scale, 2*self.scale)
		self.price = float('%.2f' % self.price)
	else:
		#Case: within steady bound
		self.price = self.price + rand.randint(-2*self.scale, 2*self.scale)
		self.price = float('%.2f' % self.price)
	#ensure stock does not go negative
	if (self.price < 1):
		self.price = 1
def trend_gen_rise(self):
	self.trend_exit = 4
	self.price = self.price + rand.randint(-self.scale, 3*self.scale)
	self.price = float('%.2f' % self.price)
	#ensure stock does not go negative
	if (self.price < 1):
		self.price = 1
def trend_gen_fall(self):
	self.trend_exit = 4
	self.price = self.price + rand.randint(-3*self.scale, self.scale)
	self.price = float('%.2f' % self.price)
	#ensure stock does not go negative
	if (self.price < 1):
		self.price = 1
def trend_gr_rise(self):
	self.trend_exit = 1
	self.price = self.price + rand.randint(4*self.scale, 10*self.scale)
	self.price = float('%.2f' % self.price)
	#ensure stock does not go negative
	if (self.price < 1):
		self.price = 1
def trend_gr_fall(self):
	self.trend_exit = 1
	self.price = self.price + rand.randint(-10*self.scale, -4*self.scale)
	self.price = float('%.2f' + self.price)
	#ensure stock does not go negative
	if (self.price < 1):
		self.price = 1
