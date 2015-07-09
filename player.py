class Player:
	"""
	A class for storing information about a player of the card game
	@param(string) - the name of the player
	@out(boolean) - whether or not the player is out of the game
	"""
	def __init__(self, name, out=False):
		self.name = name
		self.out = out
		self.hand = []