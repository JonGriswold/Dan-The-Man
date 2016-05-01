import urllib2, json, random, word

class WordWrapper:

    def __init__(self, wt, s):
        self.word_type = wt
        self.synonyms = s

    def get_word_type(self):
        return self.word_type

    # returns a list of synonyms
    def get_synonyms(self):
        return self.synonyms

    # returns a random synonym from the list
    def get_synonym(self):
        RANDOM = 1
        if RANDOM == 1:
            return self.synonyms[random.randint(0, len(self.synonyms) - 1)]
        else:
            return self.synonyms[0]

class Thesaurus:

    def __init__(self):
        self.key = "JGpg2lxzPT1Zt6FOsuNo"
        self.key2 = "e41fb970752270a0b4f0af04581e9233"

    def lookup_word(self, w):
        try:
            self.url = "http://thesaurus.altervista.org/thesaurus/v1?word=" + w + "&language=en_US&key=" + self.key + "&output=json"
            response = urllib2.urlopen(self.url)
            json_dump = response.read()
            #print json_dump
            json_dict = json.loads(json_dump.decode("UTF-8"))
            json_list = json_dict['response']

            word_type = json_dict['response'][0]['list']['category']
            word_type = word_type.replace("(", "")
            word_type = word_type.replace(")", "")

            new_synonyms = []

            for ls in json_list:
                synonyms = ls['list']['synonyms']
                synonyms = synonyms.split("|")

                count = 0
                for syn in synonyms:
                    if count == 3: break
                    if "antonym" in syn:
                        new_synonyms.append(w)
                    else:
                        new_synonyms.append(syn.replace(" (similar term)", "").replace(" (related term)", ""))
                    count += 1

            return WordWrapper(word_type, new_synonyms)
        except Exception as e:
            print str(e)
            return WordWrapper("other", [w])

def main():

    theo = Thesaurus()
    result = theo.lookup_word("love")
    print "Word Type: " + result.get_word_type()
    print "Synonyms: " + str(result.get_synonyms())

if __name__ == "__main__":
    main()
