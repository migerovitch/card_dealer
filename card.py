suits = ("Diamonds", "Clubs", "Hearts", "Spades")
values = ("Ace", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")

class Card:
	"""
	A class for holding the information of a single Card
	@param(number) - the suit of the card
	@param(number) - the value of the card
	"""
    def __init__(self, suit, value):
        self.suit = suit;
        self.value = value