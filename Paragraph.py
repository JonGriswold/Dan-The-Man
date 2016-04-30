import re
import essay
import word
import sentence

class Paragraph:
	#This is a class that contains a single Paragraph

	sentences = []


	def __init__(self, plain_text_paragraph):

		print re.split(r"([.\!\?][\s\n\r\t])", plain_text_paragraph)

		self.sentences.remove('')

	def unplagarize(self)
		for x in xrange(0,len(self.sentences)/2):
			sentences[x] = Sentence(sentences[x], sentences[x+1])
			x += 1

		full_paragraph = self.sentences[0]
		for x in xrange(1,len(self.sentences)):
			full_paragraph = full_paragraph + " " + self.sentences[x]
		return full_paragraph 
		

	def __str__(self):
		full_paragraph = self.sentences[0]
		for x in xrange(1,len(self.sentences)):
			full_paragraph = full_paragraph + " " + self.sentences[x]
		return full_paragraph