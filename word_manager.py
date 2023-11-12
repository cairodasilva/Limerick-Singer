
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
        
def main():
    worder = WordManager()
    print(worder.find_rhyme_word("Cairo"))

if __name__ == "__main__":
    main()
