"""@author Cairo Dasilva, CSCI 3725, M7
This class manages one line of one poem"""
import numpy as np
from word_manager import WordManager
from nlpmanager import NlpManager
class Line:

    def __init__(self, line, song, nlpmanager):
        self.nlp = nlpmanager
        self.line = line.split()
        self.worder = WordManager()


    def get_text(self):
        """returns the text of the line array as one sentence"""
        return ' '.join(self.line)
    
    def mutate(self,array = [0,1,2,1,2,1,2]):
        """mutates the line with a higher probability of mutating nouns and verbs"""
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
        """replaces the last word with a word that rhymes with it,
        selects for words that rhyme better"""
        if end_word == -1:
            end_word =  self.line[-1]
        scores = []
        rhyme_words = self.worder.find_rhyme_word(end_word)
        if len(rhyme_words) == 0:
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
        """replaces a word at the index of the line"""
        #print("swapping ", self.line[index], " with ", new_word)
        new_line =  self.line[:index]  + [new_word]  + self.line[index + 1:]
        self.line = new_line
        return self.line

    def min_max(self, array):
        """takes an array of numbers and turns it to a scale from 0 to 1"""
        min_value = min(array)
        if min_value < 0:
            max_value = max(array)
            scaled_array = [(value - min_value) / (max_value - min_value)
             for value in array]
            return scaled_array
        return array
        

    def get_end_word(self):
        """returns the last word in the line"""
        return self.line[-1]

    def swap_noun(self):
        """swaps a noun in the line with one from the song"""
        new_noun_tuple = self.nlp.new_noun(self.get_text())
        if new_noun_tuple != -1:
            noun = new_noun_tuple[0]
            index = new_noun_tuple[1]
            self.replace_word(index,noun)
        else:
            self.mutate([0,2])
        return self.line

    def swap_verb(self):
        """swaps a verb in the line with on from the song """
        new_verb_tuple = self.nlp.new_verb(self.get_text())
        if new_verb_tuple != -1:
            verb = new_verb_tuple[0]
            index = new_verb_tuple[1]
            self.replace_word(index,verb)
        else:
            self.mutate([0,1])
        return self.line




