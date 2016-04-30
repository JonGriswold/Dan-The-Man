import thesaurus

# global lists
articles = ["the", "a", "an", "this", "that"]

prepositions = [
    "aboard",
    "about",
    "above",
    "across",
    "after",
    "against",
    "along",
    "amid",
    "among",
    "anti",
    "around",
    "as",
    "at",
    "before",
    "behind",
    "below",
    "beneath",
    "beside",
    "besides",
    "between",
    "beyond",
    "but",
    "by",
    "concerning",
    "considering",
    "despite",
    "down",
    "during",
    "except",
    "excepting",
    "excluding",
    "following",
    "for",
    "from",
    "in",
    "inside",
    "into",
    "like",
    "minus",
    "near",
    "of",
    "off",
    "on",
    "onto",
    "opposite",
    "outside",
    "over",
    "past",
    "per",
    "plus",
    "regarding",
    "round",
    "save",
    "since",
    "than",
    "through",
    "to",
    "toward",
    "towards",
    "under",
    "underneath",
    "unlike",
    "until",
    "up",
    "upon",
    "versus",
    "via",
    "with",
    "within",
    "without"
]

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
		return (word.lower() in articles)

	def is_preposition(self, word):
		return (word.lower() in prepositions)

	def is_fanboys(self, word):
		return (word.lower() in fanboys)

	def is_proper_noun(self, word):
		if len(word) > 0:
			return (word[0].isupper())
		else:
			return false

	def get_word_type(self):
		return self.word_type

	def get_synonym(self):
		return self.synonym

	def get_og_word(self):
		return self.word

	def is_verb(self, word):
		return ("ing" == word[-3:] or "ed" == word[-2:] or "s" == word[-1:])

	def process_verb(self, word):
		temp = ""
		if "ing" == word[-3:]:
			temp = "ing"
		elif "ed" == word[-2:]:
			temp = "ed"
		elif "s" == word[-1:]:
			temp = "s"

		word = word.replace(temp, "")
		self.lookup_helper(word)
		if self.synonym[-1:] == "e" and temp == "ed":
			self.synonym += "d"
		else:
			self.synonym += temp

	def lookup_helper(self, word):
		res = self.theo.lookup_word(word)
		self.word_type = res.get_word_type()
		if self.word_type == "adj":
			self.word_type = WordType.adjective
		elif self.word_type == "adv":
			self.word_type = WordType.adverb
		elif self.word_type == "noun":
			self.word_type = WordType.noun
		elif self.word_type == "verb":
			self.word_type = WordType.verb
		self.synonym = res.get_synonym()

	def anal_word(self, word):
		""" analyze the word, determine its type and suggested synonym """

		# check for designated
		if word.lower() == "brown":
			self.word_type = WordType.article
			self.synonym = "designated"
		else:
			# if the word is special, leave the word alone
			if self.is_article(word):
				self.word_type = WordType.article
				self.synonym = word
			elif self.is_proper_noun(word):
				self.word_type = WordType.proper_noun
				self.synonym = word
			elif self.is_fanboys(word):
				self.word_type = WordType.fanboys
				self.synonym = word
			elif self.is_preposition(word):
				self.word_type = WordType.preposition
				self.synonym = word
			elif self.is_verb(word):
				self.process_verb(word)
			else:
				# if the word is a noun, or adjective, query the thesaurus service
				self.lookup_helper(word)

def main():

    theo = thesaurus.Thesaurus()

    test = "I really like jumping"
    words = test.split(" ")
    new_sentence = ""

    for word in words:
    	w = Word(word, theo)
    	new_sentence += "(" + w.get_og_word() + ", " + w.get_synonym() + ") "

    print new_sentence

if __name__ == "__main__":
    main()