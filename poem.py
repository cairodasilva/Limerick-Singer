import syllables
import pronouncing
import numpy as np
from line import Line
from word_manager import WordManager
from nlpmanager import NlpManager
from spotify import Spotify


class Poem:
    def __init__(self,lines,song,nlpmanager,valence):
        self.valence = valence
        self.lyric = song
        self.rhyme = "AABBAA" # set rhyme scheme here
        self.lines = []
        self.worder = WordManager()
        self.nlp = nlpmanager
        for line in lines:
            stripped_line = line.strip()
            if len(stripped_line) > 0:
                self.lines.append(Line(stripped_line,self.lyric,self.nlp))

  

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
            line = line.mutate()
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

    def getFitness(self):
       
        meter_coeff = 1
        similar_coeff = 1
        syllables_coeff = 1
        sentiment_coeff = 1

        meter = (self.get_meter()) #want lowest
        similar = 1 - (self.get_similarity()) #want highest can do 1- ans
        syllables = self.num_syllables() #want to lowest
        sentiment =  self.get_sentiment() #want lowest
        print ("meter fitness= " , meter_coeff*meter)
        print ("similar fitness= " , similar_coeff*similar)
        print ("sentiment fitness= " , sentiment_coeff*sentiment)
        print ("syllables fitness= " , syllables_coeff*syllables)
        return (meter_coeff*meter + similar_coeff*similar
         + sentiment_coeff*sentiment + syllables_coeff*syllables)

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
                phone = (pronouncing.phones_for_word(word))
                if phone == []:
                    line_meter.append(10)
                else:
                    line_meter.append(pronouncing.stresses(pronouncing.phones_for_word(word)[0]))
        
            if index < len(meter_scheme):
                scheme_arr = [int(char) for char in meter_scheme[index]]
                expanded_line = [int(digit) for number in line_meter for digit in str(number)]
                print(scheme_arr)
                print(expanded_line)
                if len(expanded_line) >= len(scheme_arr):
                    for i in range(len(scheme_arr)):
                        print (expanded_line[i] != scheme_arr[i])
                        total_sum += expanded_line[i] != scheme_arr[i]
                        print(total_sum)
                else:
                    print("we got here")
                    for i in range(len(line_meter)):
                        total_sum += line_meter[i] != scheme_arr[i]
                total_sum += abs(len(expanded_line)- len(scheme_arr))
                index += 1
            
        return(total_sum)
        

    def get_similarity(self):
        #takes out stop words from both poem and song and then gets the 
        # similarity between the two
        song = self.lyric
        poem = " ".join(self.getText())
        sim =  self.nlp.poem_song_similarity(poem,song)
        return sim
        
    def get_sentiment(self):
        valence = self.valence
        poem = " ".join(self.getText())
        sentiment = self.nlp.get_sentiment(poem)
        sentiment_scaled = (sentiment + 1)/2
        return abs(valence-sentiment_scaled)
        

    def get_num_lines(self):
        return len(self.lines)
   
        
   





        