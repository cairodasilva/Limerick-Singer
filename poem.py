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
        self.rhyme = "AABBA" # set rhyme scheme here
        self.lines = []
        self.worder = WordManager()
        self.nlp = nlpmanager
        for line in lines:
            stripped_line = line.strip()
            if len(stripped_line) > 0:
                self.lines.append(Line(stripped_line,self.lyric,self.nlp))
        self.fitness = -1
  

    def getLines(self):
        lines = []
        for line in self.lines:
            lines.append(line.getText())
        return lines

    def mutate(self):
        lines = self.lines
        choice = np.random.choice([2,3,4,5]) #choose between mutating 1 and 3 lines
        mutated_lines = np.random.choice(lines, size = choice, replace = False)
        for line in mutated_lines: 
            mutations = np.random.randint(3) + 1
            for _ in range (1):
                line = line.mutate()
        self.updateFitness()
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
        if self.fitness != -1:
            return self.fitness
        return self.updateFitness()


    def updateFitness(self):
       
        meter_coeff = 1/100
        similar_coeff = 2
        sentiment_coeff = 1

        meter = (self.get_meter()) #want lowest
        similar = 1 - (self.get_similarity()) #want highest can do 1- ans
        sentiment =  self.get_sentiment() #want lowest
        # print ("meter fitness= " , meter_coeff*meter)
        # print ("similar fitness= " , similar_coeff*similar)
        # print ("sentiment fitness= " , sentiment_coeff*sentiment)
        # print ("syllables fitness= " , syllables_coeff*syllables)
        # print ("total fitness = ",meter_coeff*meter + similar_coeff*similar
        #  + sentiment_coeff*sentiment )
        return (meter_coeff*meter + similar_coeff*similar
         + sentiment_coeff*sentiment )



                
        
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
                if len(expanded_line) >= len(scheme_arr):
                    for i in range(len(scheme_arr)):
                        total_sum += expanded_line[i] != scheme_arr[i]
                else:
                  
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
   
        
   





        