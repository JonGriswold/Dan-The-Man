import re
import Paragraph
import word
import essay

class Sentence:
	#This is a class that contains a single sentence

	words = []


	def __init__(self, plain_text_sentence):

		self.words = re.split(r"\s", no_return_sentence)

		self.words.remove('')

	def unplagarize(self)
		for x in xrange(0,len(self.sentences) - 1):
			sentences[x] = Sentence(sentences[x])

		full_paragraph = self.sentences[0]
		for x in xrange(1,len(self.sentences)):
			full_paragraph = full_paragraph + " " + self.sentences[x]
		return full_paragraph

	def __str__(self):
		full_sentence = self.words[0]
		for x in xrange(1,len(self.words)):
			full_sentence = full_sentence + " " + self.words[x]
		return full_sentence