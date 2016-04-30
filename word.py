import thesaurus

# global lists
articles = ["the", "a", "an"]

prepositions = ["on", "with", "in"]

fanboys = ["for", "and", "nor", "but", "or", "yet", "so"]

# enum for word types
class WordType:
	article = 0
	noun = 1
	proper_noun = 2
	verb = 3
	adverb = 4
	adjective = 5
	fanboys = 6
	preposition = 7
	other = 8

class Word:
	def __init__(self, word, theo):
		self.word = word
		self.word_type = WordType.other
		self.synonym = word
		self.theo = theo

		self.anal_word(self.word)

	def is_article(self, word):
		return (word in articles)

	def is_preposition(self, word):
		return (word in prepositions)

	def is_fanboys(self, word):
		return (word in fanboys)

	def is_proper_noun(self, word):
		if len(word) > 0:
			return (word[0].is_upper())
		else:
			return false

	def get_word_type(self):
		return self.word_type

	def get_synonym(self):
		return self.synonym

	def anal_word(self, word):
		""" analyze the word, determine its type and suggested synonym """

		# check for designated
		if word.lower() == "brown":
			self.word_type = WordType.article
			self.synonym = "designated"
		else:
			# if the word is special, leave the word alone
			if is_article(word):
				self.word_type = WordType.article
				self.synonym = word
			elif is_proper_noun(word):
				self.word_type = WordType.proper_noun
				self.synonym = word
			elif is_fanboys(word):
				self.word_type = WordType.fanboys
				self.synonym = word
			elif is_preposition(word):
				self.word_type = WordType.preposition
				self.synonym = word
			else:
				# if the word is a noun, verb, or adjective, query the thesaurus service
				res = self.theo.lookup_word(word)
				self.word_type = res.get_word_type()
				self.synonym = res.get_synonym()

def main():

    theo = Thesaurus()

    test = "The quick brown fox jumped over the lazy dog"
    words = test.split(" ")
    new_sentence = []
    

if __name__ == "__main__":
    main()