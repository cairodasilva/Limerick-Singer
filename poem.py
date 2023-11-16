
import numpy as np
from line import Line

from word_manager import WordManager
from nlpmanager import NlpManager


class Poem:
    def __init__(self,lines,song):
        
        self.lyric = song
        self.rhyme = "AABBAA" # set rhyme scheme here
        self.lines = []
        self.worder = WordManager()
        self.nlp = NlpManager(self.lyric)
        for line in lines:
            stripped_line = line.strip()
            if len(stripped_line) > 0:
                self.lines.append(Line(stripped_line,self.lyric,self.nlp))

    def getFitness(self):
        return np.random.rand()

    def getLines(self):
        lines = []
        for line in self.lines:
            lines.append(line.getText())
        return lines

    def mutate(self):
        lines = self.lines
        choice = np.random.randint(1,4) #choose between mutating 1 and 3 lines
        mutated_lines = np.random.choice(lines, size = choice, replace = False)
        for line in mutated_lines:
            print(line.getText())
            line = line.mutate()
            print(line.getText())
        return self
    def getText(self):
        poem = []
        for line in self.lines:
            poem.append(line.getText())
        return poem
    def normalize_rhymes(self):
        index = 0
        rhyme_dict =  {}
        for line in self.lines:
            end_word = line.get_end_word()
            rhyme_scheme = self.rhyme[index]
            if rhyme_scheme not in rhyme_dict:
                rhyme_dict[rhyme_scheme] = end_word
            else: 
                word1 = rhyme_dict[rhyme_scheme]
                if not self.worder.rhyme_test(word1,end_word):
                    line.change_rhyme_word(word1)
            index += 1

    







    