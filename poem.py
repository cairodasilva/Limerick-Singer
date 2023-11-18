import syllables
import pronouncing
import numpy as np
from line import Line
from word_manager import WordManager
from nlpmanager import NlpManager


class Poem:
    def __init__(self,lines,song,nlpmanager):
        
        self.lyric = song
        self.rhyme = "AABBAA" # set rhyme scheme here
        self.lines = []
        self.worder = WordManager()
        self.nlp = nlpmanager
        for line in lines:
            stripped_line = line.strip()
            if len(stripped_line) > 0:
                self.lines.append(Line(stripped_line,self.lyric,self.nlp))

    def getFitness(self):
        self.num_syllables()
        self.get_meter()
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
    #FITNESS STARTS HERE
    def num_syllables(self):
        #gets the number of syllables in each line and then gives a number 
        # based on the average number of syllables it's off on each line
        limerick_syllables = [7,7,5,5,7]
        poem_syl = []
        syl_sum = 0
        index = 0
        for line in self.lines:
            words = line.getText().split()
            syllable_count = sum(syllables.estimate(word) for word in words)
            poem_syl.append(syllable_count)
        if len(limerick_syllables) >= len(poem_syl):
            for i in range(len(poem_syl)):
                diff = abs(limerick_syllables[i]-poem_syl[i])
                print(diff)
                syl_sum += diff
                index+=1
            for syl in limerick_syllables[index:]:
                syl_sum += syl
        else:
            for i in range(len(limerick_syllables)):
                diff = abs(limerick_syllables[i]-poem_syl[i])
                syl_sum += diff
                index += 1
        return syl_sum

                
        
    def get_meter(self):
        meter_scheme = ['0100101','0100101','01001','01001','0100101']
        total_sum = 0
        index = 0
        for line in self.lines:
            line_meter = []
            texts = line.getText().split()
            for word in texts:
                if word == 'untamed':
                    line_meter.append(10)
                else:
                    line_meter.append(pronouncing.stresses(pronouncing.phones_for_word(word)[0]))
            if index < len(meter_scheme):
                scheme_arr = [int(char) for char in meter_scheme[index]]
                print(scheme_arr)
                if len(line_meter) >= len(scheme_arr):
                    for i in range(len(scheme_arr)):
                        total_sum += line_meter[i] != scheme_arr[i]
                else:
                    for i in range(len(line_meter)):
                        total_sum += line_meter[i] != scheme_arr[i]
                total_sum += abs(len(line_meter)- len(scheme_arr))
                index += 1
            else: 
                for meter in line_meter:
                    total_sum += int(meter)
        print(total_sum)

            

    def get_similarity(self):
        #takes out stop words from both poem and song and then gets the 
        # similarity between the two
        pass
    def get_sentiment(self):
        #gets sentiment from poem and valence from song and tells difference 
        # - puts them on the same scale
        pass
    def get_noun_chunk_popularity(self):
        #gets the popularity of every noun chunk
        pass
    def get_num_lines(self):
        return len(self.lines)
   
        
    def syl(self):
        for line in self.lines:
            words = line.getText().split()
            syllable_count = sum(syllables.estimate(word) for word in words)
            print (syllable_count)





        