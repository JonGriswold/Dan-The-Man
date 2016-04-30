marker_words = ["Before", "after", "because", "since", "in order to", "although", "though", "whenever", "wherever", "whether", "while", "even though", "even if", "at one point"]

class ClauseType:
	dependent = 0
	independent = 1
	other = 2

class Clause:

	def __init__(self, words):
		self.list_of_words = words
		self.clause_type = other

