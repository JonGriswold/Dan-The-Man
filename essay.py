import re

class Essay:
	#This should be the top level class

	paragraphs = []


	def __init__(self, plainTextEssay):

		noReturnEssay = re.sub(r"\n", "", plainTextEssay)
		self.paragraphs = re.split(r"\t", noReturnEssay)

		self.paragraphs.remove('')

	def __str__(self):
		fullEssay = "\t" + self.paragraphs[0]
		for x in xrange(1,len(self.paragraphs)):
			fullEssay = fullEssay + "\n\t" + self.paragraphs[x]
		return fullEssay

def main():
	totallyNotPlagarized = Essay("\tThe quick brown fox jumped over the lazy dog.\n\tIt was a designated fox.") #pass in unedited essay string

	print totallyNotPlagarized

if __name__ == "__main__":
	main()