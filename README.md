ECE2524 Stock Simulator Game
============================

There are two ways to play the game:
RECOMMENDED:
-----------
	Visit http://stocksece2524s13.appspot.com/
	This webpage is running the code contained in this repo on the google webapp engine.
	The main GUI based version of the game runs here.
	It requires a google account to play (you can use your VT account).

ALSO TRY:
---------
	The game will run on the terminal by executing game.py.


HOW TO PLAY:
-----------

**Playing on the webapp engine:**
	1. Visit http://stocksece2524s13.appspot.com/
	2. Click "Load Simulated Data" to generate stocks.
	3. Buy or sell stocks by respectively putting a positive number in the form box for the stock
	and pressing "Update".
	4. Press "Progress" to simulate one day's change in the stocks.
	5. At any time, reload the simulated data to start over.
	6. ???
	7. Profit.

**Playing on the terminal**

	1. Run game.py
	2. 10 stocks are listed in the following format
		[Num]) [Stock], [Number Owned], [Price], [Change]
	3. To use the game, type one of the following:
		* buy [how many] [stock number]
		*sell [how many] [stock number]
		*view
		*done
		*The 'view' command will show a table of the stocks.
		*The 'done' command will finish the day's trading and simulate a new day.

Known Issues:
------------
	There are currently no game objectives
	The webapp engine occasionally breaks if the user mashes inputs
