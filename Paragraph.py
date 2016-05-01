import re
import essay
import word
import sentence

class Paragraph:
	#This is a class that contains a single Paragraph

	sentences = []
	final_sentences = []


	def __init__(self, plain_text_paragraph):

		self.sentences = re.split(r"([.\!\?])", "At one point before Trump arrived, about two dozen protesters tried to rush barriers near the hotel. This resulted in a hot time.")
		self.sentences.remove('')
		print self.sentences


	def unplagarize(self):
		for x in xrange(0,len(self.sentences)/2,2):
			self.final_sentences.append(sentence.Sentence(self.sentences[x],self.sentences[x+1]).unplagarize)
		print self.sentences
		print self.final_sentences



		full_paragraph = self.final_sentences[0]
		for x in xrange(1,len(self.final_sentences)):
			full_paragraph = full_paragraph + " " + self.final_sentences[x]
		return full_paragraph 
		

	def __str__(self):
		full_paragraph = self.sentences[0]
		for x in xrange(1,len(self.sentences)):
			full_paragraph = full_paragraph + " " + self.sentences[x]
		return full_paragraph