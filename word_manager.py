import pronouncing
import requests
class WordManager:
    def __init__(self):
        self.key = "https://api.datamuse.com/words"

    def find_rhyme_word(self, word):
        rhyme_words = []
        rhyme_scores = []
        params = {"rel_rhy": word}
        response = requests.get(self.key, params=params)
        rhyme_dict = {}
        rhyme_dict = {word['word'] : word['score'] if 'score' in word else 0 for word in response.json()}
        return rhyme_dict
    def rhyme_test(self,word1,word2):
        return word2 in self.find_rhyme_word(word1)

    def tester(self,word):
        print(self.find_rhyme_word(word))
        print(pronouncing.rhymes(word))

def main():
    worder = WordManager()
   # print(worder.find_rhyme_word("Cairo"))
    print(worder.rhyme_test("heart","cairo"))

if __name__ == "__main__":
    main()
