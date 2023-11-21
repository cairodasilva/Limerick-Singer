
import numpy as np
from word_manager import WordManager

from nlpmanager import NlpManager
class Line:

    def __init__(self, line, song, nlpmanager):
        
        self.nlp = nlpmanager
        self.line = line.split()
        self.worder = WordManager()


    def getText(self):
        return ' '.join(self.line)
    
    def mutate(self,array = [0,1,2,1,2]):
        mutation = np.random.choice(array)
        match mutation:
            case 0: #change rhyme word to closer to theme
                self.change_rhyme_word()
              
            case 1: #change noun to noun from lyric list
                self.swap_noun()
              
            case 2:
                self.swap_verb()
              
    

        return self
            
    def change_rhyme_word(self,end_word = -1):
       
        if end_word == -1:
            end_word =  self.line[-1]
        scores = []
        rhyme_words = self.worder.find_rhyme_word(end_word)
        if len(rhyme_words) == 0:
            print("no ryhmes for "+ end_word)
            return end_word
        scores = rhyme_words.values()
        total = sum(scores)
        if(total == 0):
            return end_word
        p = [value / total for value in scores]
        new_word =  np.random.choice(list(rhyme_words.keys()), p =p)
        self.replace_word(len(self.line)-1,new_word)
        return new_word
    
    def replace_word(self, index, new_word):
        #print("swapping ", self.line[index], " with ", new_word)
        new_line =  self.line[:index]  + [new_word]  + self.line[index + 1:]
        self.line = new_line
        return self.line

    def min_max(self, array):
        min_value = min(array)
        if min_value < 0:
            max_value = max(array)
            scaled_array = [(value - min_value) / (max_value - min_value) for value in array]
            return scaled_array
        return array
        
    def get_end_word(self):
        return self.line[-1]

    def swap_noun(self):
        new_noun_tuple = self.nlp.new_noun(self.getText())
        if new_noun_tuple != -1:
            noun = new_noun_tuple[0]
            index = new_noun_tuple[1]
            self.replace_word(index,noun)
        else:
            self.mutate([0,2])
        return self.line

    def swap_verb(self):
        new_verb_tuple = self.nlp.new_verb(self.getText())
        if new_verb_tuple != -1:
            verb = new_verb_tuple[0]
            index = new_verb_tuple[1]
            self.replace_word(index,verb)
        else:
            self.mutate([0,1])
        return self.line



def main():
    line = Line("and my house its burning down")
    print(line.getText())
    line.change_rhyme_word()
    print(line.getText())
    line.swap_noun()
    print(line.getText())
  


if __name__ == "__main__":
    main()

