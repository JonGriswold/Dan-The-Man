import re
import Paragraph
import word
import essay

class Sentence:
	#This is a class that contains a single sentence

	words = []
	endPunctuation = ""
	fanboys = []
	markers = []
	commas = []
	add_commas = []


	def __init__(self, plain_text_sentence, punctuation_mark):

		self.words = re.split(r"\s", plain_text_sentence)
		self.endPunctuation = punctuation_mark

		self.words.remove('')

	def unplagarize(self):
		#this also records which words are markers for restructing
		#synonym()
		#restructure()
		#add_commas()

		full_sentence = self.words[0]
		for x in xrange(1,len(self.words)):
			#check if a comma needs to be added
			full_sentence = full_sentence + " " + self.words[x]
			full_sentence = full_sentence + self.endPunctuation
		return full_sentence

	def synonym(self):
		for x in xrange(0,len(self.words)):
			if self.words[x][len(self.words[x])] == ",":
				self.commas.append(x)
			#75% synonym usage so that the sentence will make sense
			if random.randint(1,4) != 3:
				self.words[x] = Word(re.sub(r",","",self.words[x])).get_synonym
			if Word(self.words[x]).get_word_type == word.Word_Type.fanboys:
				self.fanboys.append(x)
			if Word(self.words[x]).get_word_type == word.Word_Type.marker:
				self.markers.append(x)

	def restructure(self):
		tempWords = self.words
		for x in xrange(0,len(self.fanboys)):
			if self.fanboys[x]-1 in commas:
				if self.fanboys[x]+1 in markers:
					y = self.markers[x]
					z = 0
					while y < len(self.words):		
						tempWords[z] = self.words[self.markers[x]+z]
						y += 1
						z += 1
					self.add_commas.append(z)
					z += 1
					tempWords[z] = words[self.fanboys[x]]
					y = 0
					z += 1
					while y < (self.commas[x]+1):		
						tempWords[z] = self.words[y]
						y += 1
						z += 1
				else:
					y = self.fanboys[x]
					z = 0
					while y < len(self.words):		
						tempWords[z] = self.words[self.fanboys[x]+z]
						y += 1
						z += 1
					self.add_commas.append(z)
					z += 1
					y = 0
					while y < (self.commas[x]+1):		
						tempWords[z] = self.words[y]
						y += 1
						z += 1			



	def add_commas(self):
		for x in xrange(0,len(self.commas)):
			if self.commas[x] + 1 not in self.fanboys:
				self.add_commas.append(x)

		for x in xrange(0,len(self.add_commas)):
			self.words[self.add_commas[x]] += ","



	def __str__(self):
		full_sentence = self.words[0]
		for x in xrange(1,len(self.words)):
			#check if a comma needs to be added
			full_sentence = full_sentence + " " + self.words[x]
			full_sentence = full_sentence + self.endPunctuation
		return full_sentence