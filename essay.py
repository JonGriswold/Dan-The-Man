import re
import Paragraph
import word
import sentence

class Essay:
	#This should be the top level class

	paragraphs = []


	def __init__(self, plain_text_essay):

		no_return_essay = re.sub(r"\n", "", plain_text_essay)
		self.paragraphs = re.split(r"\t", no_return_essay)

		self.paragraphs.remove('')

	def unplagarize(self):
		for x in xrange(0,len(self.paragraphs)):
			self.paragraphs[x] = (Paragraph.Paragraph(self.paragraphs[x])).unplagarize()

	def __str__(self):
		full_essay = "\t" + self.paragraphs[0]
		for x in xrange(1,len(self.paragraphs)):
			full_essay = full_essay + "\n\t" + self.paragraphs[x]
		return full_essay

def main():
	totally_not_plagarized = Essay("\tThe quick brown fox jumped over the lazy dog.\n\tIt was a designated fox.") #pass in unedited essay string

	totally_not_plagarized.unplagarize()

	print totally_not_plagarized

if __name__ == "__main__":
	main()