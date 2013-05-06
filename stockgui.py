import cgi
import re
import datetime
import urllib
import webapp2
import webGame

from google.appengine.ext import db
from google.appengine.api import users

COMPANY = ["", "", "", "", "", "", "", "", "", ""]
OWNED = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
PRICE = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
DELTA = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
TOTAL = 100
STOCKVALUE = 0;
DAY = 1
MESSAGE = ""
ERRORCODE = 0
STARTED = False
FIRSTSHOWING = True

MAIN_PAGE_HTML = """\
	<head>
    	<link type="text/css" rel="stylesheet" href="/stylesheets/main.css" />
		<link type="image/x-icon" rel="icon" href="/static/favicon.ico" />
	</head>
	<body>
		<table id = "head">
			<tr>
				<th scope="col">
					<font size="5px"><p>Stock Exchange!</p></font>
					<font size="3px"><p>User: %s</p></font></th>
			</tr>
		</table>

		<table align="left" border="1" cellpadding="1" cellspacing="1" id="stock-table">
			<colgroup>
				<col class="columns"/>
			</colgroup>
			<thead>
				<tr>
					<th scope="col">
						Update Stocks</th>
					<th scope="col">
						Company</th>
					<th scope="col">
						Owned</th>
					<th scope="col">
						Price</th>
					<th scope="col">
						Changed</th>
				</tr>
			</thead>
			<tbody>
"""

TABLE = """\
	<tr>
		<td>
			<form action="/handle%s" method="post">
				<input name="buy%s" type="submit" value="Update"/>
				<input name="amount%s" maxlength="10" size="6"/>
			</form>
		<td>
			%s</td>
		<td>
			%s</td>
		<td>
			$%s</td>
		<td>
			$%s</td>
	</tr>
</form>
"""

FINISH = """\
		</tbody>
	</table>
		<p>&nbsp;</p>
	</body>
	<body>
		<form action="/progress" method="post">
				<p>Your Wallet: $%s</p>
				<p>Your Stock Value: $%s</p>
				<p>Day: %s</p>
				<p><input name="progress" type="submit" value="Progress" />
				<input name="progressDays" maxlength="3" size="3" value="1"/>day(s)</p>
		</form>
		<form action="/loadReal" method="get">
			<input name="loadReal" type="submit" value="Load Real Data" />
		</form>
		<form action="/loadFake" method="get">
			<p><input name="loadFake" type="submit" value="Load Simulated Data" /></p>
		</form>
		<font size="3px">Messages:</font>
		<div id="alert">
			<p style="padding: 0px 8px; COLOR: red;">%s</p>
		</div>
	</body>
"""

def buy(self, amount, num):
	global TOTAL
	if (float(amount)*float(webGame.stocks[num].price) > float(TOTAL)):
		return -1
	elif ((amount*-1) > webGame.stocks[num].owned):
		return -2
	else:
		TOTAL -= float(amount)*float(webGame.stocks[num].price)
		return 1

def update():
	global STOCKVALUE
	global FIRSTSHOWING
	STOCKVALUE = 0
	for i in range (10):
		COMPANY[i] = webGame.stocks[i].name
		OWNED[i] = webGame.stocks[i].owned
		PRICE[i] = webGame.stocks[i].price
		if (FIRSTSHOWING == False):
			DELTA[i] = webGame.stocks[i].change
		STOCKVALUE += float(OWNED[i])*float(PRICE[i])

def stockTrade(self, stock):
	global MESSAGE
	global ERRORCODE
	MESSAGE = ""
	textfieldName = 'amount' + str(stock)
	textfieldAmount = self.request.get(textfieldName)
	
	if (STARTED == 1):
		if (textfieldAmount == ""):
			MESSAGE = "Enter a stock amount first."
		elif "." in textfieldAmount:
			MESSAGE = "Enter stocks in whole shares only."
		elif not re.compile("\d+").search(textfieldAmount):
			MESSAGE = "Enter stocks as integer values only."
		else:
			amount = int(textfieldAmount)
			ERRORCODE = buy(self, amount, stock)
			if (ERRORCODE == -1):
				MESSAGE = "You don't have enough money for that!"
			elif (ERRORCODE == -2):
				MESSAGE = "You don't have that many stocks!"
			else:
				webGame.stocks[stock].owned += amount
			
			update()
	else:
		MESSAGE = "Load stock data first."

class Company(db.Model):

	name = db.StringProperty()
	owned = db.IntegerProperty()
	price = db.IntegerProperty()
	change = db.IntegerProperty()





class MainPage(webapp2.RequestHandler):

    def get(self):
		i = 0
		user = users.get_current_user()
		if user:
			self.response.write('<html>')
			self.response.write(MAIN_PAGE_HTML % user.nickname())
			while (i < 10):
				if ((i%2) == 0):
					button = "sell"
				else:
					button = "buy"
				self.response.write(TABLE % (str(i), str(i), str(i), COMPANY[i], str(OWNED[i]), str(PRICE[i]), str(DELTA[i])))
				i = i+1
			self.response.write(FINISH % (str(TOTAL), str(STOCKVALUE), str(DAY), MESSAGE))
			self.response.write('</html>')
		else:
			self.redirect(users.create_login_url(self.request.uri))


class LoadReal(webapp2.RequestHandler):

    def get(self):
		global TOTAL
		global DAY
		global MESSAGE
		global ERRORCODE
		global STARTED
		global FIRSTSHOWING
		STARTED = True
		FIRSTSHOWING = True
		webGame.initStock(True)
		update()
		TOTAL = 100
		DAY = 1
		MESSAGE = ""
		ERRORCODE = 0

		self.redirect('/?' + "real")


class LoadSimulated(webapp2.RequestHandler):

    def get(self):
		global TOTAL
		global DAY
		global MESSAGE
		global ERRORCODE
		global STARTED
		global FIRSTSHOWING
		STARTED = True
		FIRSTSHOWING = True
		webGame.initStock(False)
		update()
		TOTAL = 100
		DAY = 1
		MESSAGE = ""
		ERRORCODE = 0

		self.redirect('/?' + "simulated")

class Progress(webapp2.RequestHandler):

    def post(self):
		global DAY
		global COMPANY
		global OWNED
		global PRICE
		global DELTA
		global TOTAL
		global MESSAGE
		global FIRSTSHOWING
		if (STARTED == True):
			for days in range(int(self.request.get('progressDays'))):
				DAY += 1
				FIRSTSHOWING = False
				for i in range(10):
					webGame.stocks[i].simulate()
				update()
		else:
			MESSAGE = "Please load stock data."
		self.redirect('/?' + "progress")

class handle0(webapp2.RequestHandler):

	def post(self):
		stockTrade(self, 0)
		self.redirect('/?' + "handle1")	

class handle1(webapp2.RequestHandler):

	def post(self):
		stockTrade(self, 1)
		self.redirect('/?' + "handle2")

class handle2(webapp2.RequestHandler):

	def post(self):
		stockTrade(self, 2)
		self.redirect('/?' + "handle3")

class handle3(webapp2.RequestHandler):

	def post(self):
		stockTrade(self, 3)
		self.redirect('/?' + "handle4")

class handle4(webapp2.RequestHandler):

	def post(self):
		stockTrade(self, 4)
		self.redirect('/?' + "handle5")

class handle5(webapp2.RequestHandler):

	def post(self):
		stockTrade(self, 5)
		self.redirect('/?' + "handle6")

class handle6(webapp2.RequestHandler):

	def post(self):
		stockTrade(self, 6)
		self.redirect('/?' + "handle7")

class handle7(webapp2.RequestHandler):

	def post(self):
		stockTrade(self, 7)
		self.redirect('/?' + "handle8")

class handle8(webapp2.RequestHandler):

	def post(self):
		stockTrade(self, 8)
		self.redirect('/?' + "handle9")

class handle9(webapp2.RequestHandler):

	def post(self):
		stockTrade(self, 9)
		self.redirect('/?' + "handle10")

app = webapp2.WSGIApplication([('/', MainPage),
                              ('/progress', Progress),
			      			  ('/loadReal', LoadReal),
			      			  ('/loadFake', LoadSimulated),
			      			  ('/handle0', handle0),
			      			  ('/handle1', handle1),
			      			  ('/handle2', handle2),
			      			  ('/handle3', handle3),
			      			  ('/handle4', handle4),
			      			  ('/handle5', handle5),
			      			  ('/handle6', handle6),
			      			  ('/handle7', handle7),
			      			  ('/handle8', handle8),
							  ('/handle9', handle9)],
                              debug=True)
