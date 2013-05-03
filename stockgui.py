import cgi
import datetime
import urllib
import webapp2

from google.appengine.ext import db
from google.appengine.api import users

TEST = ["test1", "test2"]
COMPANY = ["", "", "", "", "", "", "", "", "", ""]
OWNED = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
PRICE = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
DELTA = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
TOTAL = 100
DAY = 1

#Company company

MAIN_PAGE_HTML = """\
	<head>
    	<link type="text/css" rel="stylesheet" href="/stylesheets/main.css" />
	</head>
	<body>
		<p><em><strong>World Wide Stock Exchange</strong></em></p>
		<p><em><strong>User: %s</strong></em></p>
	</body>
	<body>
		<table align="left" border="1" cellpadding="1" cellspacing="1" id="testID">
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
				<input name="buy%s" type="submit" value="Update" />
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
				<p>You have: $%s</p>
				<p>Day: %s</p>
				<p><input name="progress" type="submit" value="Progress" /></p>
		</form>
		<form action="/loadReal" method="post">
			<input name="loadReal" type="submit" value="Load Real Data" />
		</form>
		<form action="/loadFake" method="get">
			<p><input name="loadFake" type="submit" value="Load Simulated Data" /></p>
		</form>
	</body>
"""

class Company(db.Model):
	
	name = db.StringProperty()
	owned = db.IntegerProperty()
	price = db.IntegerProperty()
	change = db.IntegerProperty()

	def buy():
		self.redirect('/?' + "test")# + company + str(amount))
	


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
			self.response.write(FINISH % (str(TOTAL), str(DAY)))
			self.response.write('</html>')
		else:
			self.redirect(users.create_login_url(self.request.uri))


class LoadReal(webapp2.RequestHandler):

    def post(self):
		self.redirect('/?' + "real")


class LoadSimulated(webapp2.RequestHandler):

    def get(self):
		self.redirect('/?' + "fake")

class Progress(webapp2.RequestHandler):

    def post(self):
		global DAY
		global COMPANY
		global OWNED
		global PRICE
		global DELTA
		global TOTAL
		DAY += 1
		#update all lists
		self.redirect('/?' + "progress")

class handle0(webapp2.RequestHandler):

	def post(self):
		amount = self.request.get('amount0')
		OWNED[0] += int(amount)
		self.redirect('/?' + "handle1")	

class handle1(webapp2.RequestHandler):

	def post(self):
		amount = self.request.get('amount1')
		OWNED[1] += int(amount)
		self.redirect('/?' + "handle2")

class handle2(webapp2.RequestHandler):

	def post(self):
		amount = self.request.get('amount2')
		OWNED[2] += int(amount)
		self.redirect('/?' + "handle3")

class handle3(webapp2.RequestHandler):

	def post(self):
		amount = self.request.get('amount3')
		OWNED[3] += int(amount)
		self.redirect('/?' + "handle4")

class handle4(webapp2.RequestHandler):

	def post(self):
		amount = self.request.get('amount4')
		OWNED[4] += int(amount)
		self.redirect('/?' + "handle5")

class handle5(webapp2.RequestHandler):

	def post(self):
		amount = self.request.get('amount5')
		OWNED[5] += int(amount)
		self.redirect('/?' + "handle6")

class handle6(webapp2.RequestHandler):

	def post(self):
		amount = self.request.get('amount6')
		OWNED[6] += int(amount)
		self.redirect('/?' + "handle7")

class handle7(webapp2.RequestHandler):

	def post(self):
		amount = self.request.get('amount7')
		OWNED[7] += int(amount)
		self.redirect('/?' + "handle8")

class handle8(webapp2.RequestHandler):

	def post(self):
		amount = self.request.get('amount8')
		OWNED[8] += int(amount)
		self.redirect('/?' + "handle9")

class handle9(webapp2.RequestHandler):

	def post(self):
		amount = self.request.get('amount9')
		OWNED[9] += int(amount)
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
