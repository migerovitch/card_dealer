from card import Card
import random

class Deck:
	"""
	A class for holding a group of 52 unique cards
	"""
	def __init__(self):
		random.seed()
		cards = []
		for i in range(3):
			for j in range(12):
				cards.insert(Card(i, j))
		self.cards = cards

	"""
	Shuffles the deck randomly
	"""
	def shuffle(self):
		random.shuffle(self.cards)

	"""
	Removes and returns the top n cards from the dec
	@param(number) - the amount of cards to return
	@return(array<number>) - the top n_cards cards
	"""
	def deal(self, n_cards):
		top_cards = []
		for n in range(n_cards)
			top_cards.append(self.cards.pop())
		return top_cards