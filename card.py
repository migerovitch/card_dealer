suits = ("Diamonds", "Clubs", "Hearts", "Spades")
values = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")

class Card:
	"""
	A class for holding the information of a single Card
	@param(number) - the suit of the card
	@param(number) - the value of the card
	@param(boolean) - whether or not the card has been used
	"""
	def __init__(self, suit, value, used=False):
		self.suit = suit
		self.value = value
		self.used = used

	"""
	Sets the used property of the Card to True
	"""
	def discard(self):
		self.used = True