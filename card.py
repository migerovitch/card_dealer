suits = ("Diamonds", "Clubs", "Hearts", "Spades")
values = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")

class Card:
	"""
	A class for holding the information of a single Card
	@param(number) - the suit of the card
	@param(number) - the value of the card
	@param(boolean) - whether or not the card has been discarded
	"""
	def __init__(self, suit, value, discarded=False):
		self.suit = suit
		self.value = value
		self.discarded = discarded

	"""
	Sets the discarded property of the Card to True
	"""
	def discard(self):
		self.discarded