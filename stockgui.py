import cgi
import datetime
import urllib
import webapp2

from google.appengine.ext import db
from google.appengine.api import users

TEST = ["test1", "test2"]
BUTTONS = ["Buy", "Buy", "Buy", "Buy", "Buy", "Buy", "Buy", "Buy", "Buy", "Buy"]
#Company company

FINISH = """\
		</tbody>
	</table>
	<p>
		&nbsp;</p>
</body>
<body>
<form action="/progress" method="post">
	<p>
		<input name="progress" type="submit" value="Progress" /></p>
</form>
<form action="/loadReal" method="post">
	<input name="loadReal" type="submit" value="Load Real Data" />
</form>
<form action="/loadFake" method="get">
	<p>
		<input name="loadFake" type="submit" value="Load Simulated Data" /></p>
</form>
</body>
"""

TABLE = """\
	<tr>
		<td>
			<form action="/buy%s" method="post">
				<input name="buy%s" type="submit" value="Buy" />
				<input name="amount%s" value="hi"/>
			</form>
			<form action="/sell%s" method="post">
				<input name="sell%s" type="submit" value="Sell" />
			</form></td>
		<td>
			%s</td>
		<td>
			%s</td>
		<td>
			%s</td>
		<td>
			&nbsp;</td>
	</tr>
</form>
"""

MAIN_PAGE_HTML = """\
	<head>
		<title></title>
	</head>
	<body>
		<p>
			<em><strong>World Wide Stock Exchange</strong></em></p>
	</body>
	<body>
		<table align="left" border="1" cellpadding="1" cellspacing="1" id="testID">
			<thead>
				<tr>
					<th scope="col">
						&nbsp;</th>
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
			self.response.write(MAIN_PAGE_HTML)
			while (i < 10):
				if ((i%2) == 0):
					button = "sell"
				else:
					button = "buy"
				self.response.write(TABLE % (str(i), str(i), str(i), str(i), str(i), user.nickname(), str(TEST[0]), str(TEST[1])))
				i = i+1
			self.response.write(FINISH)
			self.response.write('</html>')
		else:
			self.redirect(users.create_login_url(self.request.uri))


class LoadReal(webapp2.RequestHandler):

    def post(self):
		self.redirect('/?' + "real")


class LoadSimulated(webapp2.RequestHandler):

    def get(self):
		global TEST
		TEST = [0,1]
		self.redirect('/?' + "fake")

class Progress(webapp2.RequestHandler):

    def post(self):
		global TEST
		TEST = [TEST[1]+1, TEST[0]+1]
		self.redirect('/?' + "progress")

class buy0(webapp2.RequestHandler):

	def post(self):
		#comp = Company(parent=user.nickname())
		amount = self.request.get('amount0')
		#comp.buy()#"Company", int(amount))
		self.redirect('/?' + "buy1")	

class buy1(webapp2.RequestHandler):

	def post(self):
		self.redirect('/?' + "buy2")

class buy2(webapp2.RequestHandler):

	def post(self):
		self.redirect('/?' + "buy3")

class buy3(webapp2.RequestHandler):

	def post(self):
		self.redirect('/?' + "buy4")

class buy4(webapp2.RequestHandler):

	def post(self):
		self.redirect('/?' + "buy5")

class buy5(webapp2.RequestHandler):

	def post(self):
		self.redirect('/?' + "buy6")

class buy6(webapp2.RequestHandler):

	def post(self):
		self.redirect('/?' + "buy7")

class buy7(webapp2.RequestHandler):

	def post(self):
		self.redirect('/?' + "buy8")

class buy8(webapp2.RequestHandler):

	def post(self):
		self.redirect('/?' + "buy9")

class buy9(webapp2.RequestHandler):

	def post(self):
		self.redirect('/?' + "buy10")

class sell0(webapp2.RequestHandler):

	def post(self):
		self.redirect('/?' + "sell1")

class sell1(webapp2.RequestHandler):

	def post(self):
		self.redirect('/?' + "sell2")

class sell2(webapp2.RequestHandler):

	def post(self):
		self.redirect('/?' + "sell3")

class sell3(webapp2.RequestHandler):

	def post(self):
		self.redirect('/?' + "sell4")

class sell4(webapp2.RequestHandler):

	def post(self):
		self.redirect('/?' + "sell5")

class sell5(webapp2.RequestHandler):

	def post(self):
		self.redirect('/?' + "sell6")

class sell6(webapp2.RequestHandler):

	def post(self):
		self.redirect('/?' + "sell7")

class sell7(webapp2.RequestHandler):

	def post(self):
		self.redirect('/?' + "sell8")

class sell8(webapp2.RequestHandler):

	def post(self):
		self.redirect('/?' + "sell9")

class sell9(webapp2.RequestHandler):

	def post(self):
		self.redirect('/?' + "sell10")

app = webapp2.WSGIApplication([('/', MainPage),
                              ('/progress', Progress),
			      			  ('/loadReal', LoadReal),
			      			  ('/loadFake', LoadSimulated),
			      			  ('/buy0', buy0),
			      			  ('/buy1', buy1),
			      			  ('/buy2', buy2),
			      			  ('/buy3', buy3),
			      			  ('/buy4', buy4),
			      			  ('/buy5', buy5),
			      			  ('/buy6', buy6),
			      			  ('/buy7', buy7),
			      			  ('/buy8', buy8),
							  ('/buy9', buy9),
			      			  ('/sell0', sell0),
			      			  ('/sell1', sell1),
			      			  ('/sell2', sell2),
			      			  ('/sell3', sell3),
			      			  ('/sell4', sell4),
			      			  ('/sell5', sell5),
			      			  ('/sell6', sell6),
			      			  ('/sell7', sell7),
			      			  ('/sell8', sell8),
							  ('/sell9', sell9)],
                              debug=True)
