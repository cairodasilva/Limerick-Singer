import pronouncing
import spacy
import numpy as np
from word_manager import WordManager
class Line:

    def __init__(self,line): #will need index for degradation
        self.nlp = spacy.load("en_core_web_sm")
        self.line = self.nlp(line)
        self.worder = WordManager()

    def getText(self):
        return self.line.text
    
    def mutate(self):
        mutation = np.random.randint(0,3)
        print(mutation)
        match mutation:
            case 0: #change rhyme word to closer to theme
                print("I am changing a rhyme word")
            case 1: #change noun to syn
                print("I am changing a verb")
            case 2: #change verb to synoynm
                print ("I am changing a noun")
        return self.line
            
    def change_rhyme_word(self):
        end_word =  self.line[-1].text
        rhyme_words = self.worder.find_rhyme_word(end_word)
        scores = list(rhyme_words.values())
        total = sum(scores)
        p = [value / total for value in scores]
        new_word =  np.random.choice(list(rhyme_words.keys()), p =p)
        self.replace_word(len(self.line)-1,new_word)
        return new_word
    
    def replace_word(self, index, new_word):
        new_line =  self.line[:index].text + " " + new_word + " " + self.line[index + 1:].text
        self.line = self.nlp(new_line)
        return self.line.text

def main():
    line = Line("Hi my name is Cairo")
    line.change_rhyme_word()


if __name__ == "__main__":
    main()
