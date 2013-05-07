ECE2524 Stock Simulator Game
============================

**There are two ways to play the game:**

RECOMMENDED:
-----------
	Visit http://stocksece2524s13.appspot.com/
	This webpage is running the code contained in this repo on the google webapp engine.
	The main GUI based version of the game runs here.
	It requires a google account to play (you can use your VT account).



LESS RECOMMENDED:
----------------
	The game will run on the terminal by executing game.py (do this by typing "./game.py" in the terminal).
	This is an older version of the game and does not include historical data.
	It was mostly used for testing, but will demonstrate the game's functionality.



HOW TO PLAY:
-----------

**Playing on the webapp engine:**

	1. Visit http://stocksece2524s13.appspot.com/
	2. Click "Load Simulated Data" to generate simulated stocks. Alternately, click "Load Real Data" to load historical data.
	3. Buy or sell stocks by respectively putting a positive number or a negative number in the form box for the stock
	and pressing "Update".
		Example: To buy 5 stocks from a certain company, enter "+5" in the text box and press "Update"
				 To sell 5 stocks from a certain comany (assuming you own at least 5 stocks), etner "-5" in the text box and press "Update"
	4. You can buy and sell stocks as many times as you would like per day.
	5. Press "Progress" to simulate one day's change in the stocks.
	6. At any time, reload the data to start over.
	7. Profit.

**Playing on the terminal:**

	. Run game.py
	2. 10 stocks are listed in the following format
		[Num]) [Stock], [Number Owned], [Price], [Change]
	3. To use the game, type one of the following:
		* buy [how many] [stock number]
		* sell [how many] [stock number]
		* view
		* done
		* exit
		* The 'view' command will show a table of the stocks.
		* The 'done' command will finish the day's trading and simulate a new day.

Still to Come:
--------------
	* Allow users to specify their own historic stocks and stock dates

Known Issues:
------------
	There are currently no game objectives
	The webapp allows players to play together, but not with their own, saved data...yet.
