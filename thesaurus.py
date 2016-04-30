import urllib2, json

class WordWrapper:

    def __init__(self, wt, s):
        self.word_type = wt
        self.synonyms = s

    def get_word_type(self):
        return self.word_type

    def get_synonyms(self):
        return self.synonyms


class Thesaurus:

    def __init__(self):
        self.key = "JGpg2lxzPT1Zt6FOsuNo"

    def lookup_word(self, w):
        try:
            self.url = "http://thesaurus.altervista.org/thesaurus/v1?word=" + w + "&language=en_US&key=" + self.key + "&output=json"
            response = urllib2.urlopen(self.url)
            json_dump = response.read()
            json_dict = json.loads(json_dump.decode("UTF-8"))
            word_type = json_dict['response'][0]['list']['category']
            word_type = word_type.replace("(", "")
            word_type = word_type.replace(")", "")
            synonyms = json_dict['response'][0]['list']['synonyms']
            synonyms = synonyms.split("|")

            return WordWrapper(word_type, synonyms)
        except Exception as e:
            print str(e)


def main():

    theo = Thesaurus()
    result = theo.lookup_word("quick")
    print "Word Type: " + result.get_word_type()
    print "Synonyms: " + str(result.get_synonyms())

if __name__ == "__main__":
    main()
