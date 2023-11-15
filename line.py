import pronouncing
import spacy
import numpy as np
from word_manager import WordManager
from lyric_manager import LyricManager

class Line:

    def __init__(self,line,lyric = LyricManager()): #will need index for degradation
        self.nlp = spacy.load("en_core_web_md")
        self.line = self.nlp(line)
        self.worder = WordManager()
        self.lyricer = LyricManager()

    def getText(self):
        return self.line.text
    
    def mutate(self):
        mutation = np.random.choice([0,1])
        match mutation:
            case 0: #change rhyme word to closer to theme
                self.change_rhyme_word()
                #print("I am changing a rhyme word")

            case 1: #change noun to noun from lyric list
                self.swap_noun()
               # print("I am changing a noun")

            
        
        return self
            
    def change_rhyme_word(self,end_word = -1):
        print("changing rhyme word")
        if end_word == -1:
            end_word =  self.line[-1].text
        scores = []
        rhyme_words = self.worder.find_rhyme_word(end_word)
        if len(rhyme_words) == 0:
            print("no ryhmes for "+ end_word)
            return end_word
        scores = rhyme_words.values()
        total = sum(scores)
        p = [value / total for value in scores]
        new_word =  np.random.choice(list(rhyme_words.keys()), p =p)
        self.replace_word(len(self.line)-1,new_word)
        return new_word
    
    def replace_word(self, index, new_word):
        print("swapping " + new_word + " with " + self.line[index].text)
        new_line =  self.line[:index].text + " " + new_word + " " + self.line[index + 1:].text
        self.line = self.nlp(new_line)
        return self.line.text

    def min_max(self, array):
        min_value = min(array)
        if min_value < 0:
            max_value = max(array)
            scaled_array = [(value - min_value) / (max_value - min_value) for value in array]
            return scaled_array
        return array
        
    def get_end_word(self):
        return self.line[-1].text

    def swap_noun(self):
        
        noun_dict = self.lyricer.get_noun_dict()
        old_nouns = []
        for token in self.line:
            if token.pos_ =="NOUN" and token.i < len(self.line) - 1:

                print(token.pos_)
                print(token.text)
                print(token.lemma)
                old_nouns.append(token.i)
        if len(old_nouns) > 0:
            replace_index = np.random.choice(old_nouns)
            replace_word = self.line[replace_index]
            scores = []
            for word in noun_dict.keys():
                noun_vector = self.nlp(word)
                score = replace_word.similarity(noun_vector)
                scores.append(score)
            scores = self.min_max(scores)
            total = sum(scores)
            p = [value / total for value in scores]
            new_noun = np.random.choice(list(noun_dict.keys()),p = p)
            self.replace_word(replace_index,new_noun)
        return self.line.text
  



def main():
    line = Line("and my house its burning down")
    print(line.mutate().getText())
  


if __name__ == "__main__":
    main()

