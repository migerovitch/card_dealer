from enum import Enum

class Card:
	"""
	A class for holding the information of a single Card
	@param(Suit) - the suit of the card
	@param(Value) - the value of the card
	"""
    def __init__(self, suit, value):
        self.suit = suit;
        self.value = value

class Suit(Enum):
    DIAMONDS = 0
    CLUBS = 1
    HEARTS = 2
    SPADES = 3

class Value(Enum):
    ACE = 0
    TWO = 1
    THREE = 2
    FOUR = 3
    FIVE = 4
    SIX = 5
    SEVEN = 6
    EIGHT = 7
    NINE = 8
    TEN = 9
    JACK = 10
    QUEEN = 11
    KING = 12
