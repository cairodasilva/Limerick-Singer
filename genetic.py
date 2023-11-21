from line import Line
import datetime
from poem import Poem
import numpy as np
import os
from song_manager import SongManager
from nlpmanager import NlpManager
from spotify import Spotify
import pyttsx3
class genetic:
    def __init__(self, iterations = 4, name = '', artist=''):
        self.iterations = iterations
        self.inspiring_set = []
        self.poems = []
        if name != '' or artist != '':
            self.name = name
            self.artist = artist
        else:
            self.name = "all falls down"
            self.artist = "kanye west"
        self.song = SongManager(self.artist,self.name).make_song_lyrics()
        self.spot = Spotify(self.name,self.artist)
        self.nlp = NlpManager(self.song)
        self.valence = self.spot.get_valence()
    
    def create_poems(self):
        dir = "./inspiring_set"
        for file in os.listdir(dir):
            with open(dir + "/" + file, "r") as f:
                poem_lines = f.readlines()
                new_poem = Poem(poem_lines,self.song,self.nlp,self.valence)
                self.poems.append(new_poem)
   

    def crossover(self,poem1,poem2):
        num_lines = 6
        pivot = np.random.randint(0,num_lines-1)
        first_poem = poem2
        second_poem = poem1
        if poem1.getFitness() > poem2.getFitness():
            first_poem = poem1
            second_poem = poem2
        section1 = first_poem.getLines()[:pivot]
     
        section2 = second_poem.getLines()[pivot:]
        
        new_poem = Poem(section1 + section2,self.song,self.nlp,self.valence)
        new_poem.normalize_rhymes()
        return new_poem


    def genetic_algo(self):
        next_generation = []
        fitnesses =[]
        sum_fitness = 0
        for poem in self.poems:
                fitness = poem.getFitness()
                fitnesses.append(fitness)
                sum_fitness +=  fitness
        fitnessnp = np.array(fitnesses)
        p = fitnessnp / sum_fitness
        for _ in range(len(self.poems)):
            poem1,poem2 = np.random.choice(self.poems,p = p,size = 2,
            replace = False)
            new_poem = self.crossover(poem1,poem2)
            new_poem.mutate()
            new_poem.normalize_rhymes()
            next_generation.append(new_poem)
        old_gen = self.fittest_half(self.poems)
        new_gen = self.fittest_half(next_generation)
        self.poems = new_gen + old_gen

    def fittest_half(self,generation):
        sorted_poems = sorted(generation, key = lambda x : x.getFitness())
        return sorted_poems[:int(len(generation)/2)]

    def genetic_algo_runner(self):
        for i in range(self.iterations):
            print(f"Running genetic algorithm for generation {i + 1}")
            self.genetic_algo() 
    def print_poems(self):
        for poem in self.poems:
            print(poem.getText())
    def get_fittest(self):
        sorted_poems = sorted(self.poems, key = lambda x : x.getFitness())
        top_poem =  (sorted_poems[0].getText())
        fitness = sorted_poems[0].getFitness()
        split_poem  = ('\n'.join(top_poem))
        print (split_poem)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = f"./previous_poems/poem_{timestamp}.txt"
        with open(filepath, "w") as f:
            f.write(str(split_poem) + '\n' + '\n' )
            f.write(f"Fitness = {fitness}" + '\n' + '\n')
            f.write(f"song  = {self.name} by {self.artist}" + '\n' + '\n')
            f.write(f"Generations = {self.iterations}")
        return top_poem
    def say(self,text):
        engine = pyttsx3.init()  
        engine.setProperty('rate', 150)  # setting up new voice rate
        engine.setProperty('volume', 0.8) 
        for item in text:
            engine.say(item)
            engine.runAndWait()
    
    def reperform_poem(self, file):
        dir = f"./previous_poems/{file}"
        with open(dir , "r") as f:
            poem_lines = f.readlines()
        engine = pyttsx3.init()  
        engine.setProperty('rate', 150)  # setting up new voice rate
        engine.setProperty('volume', 0.8) 
        for line in poem_lines:
            engine.say(line)
            engine.runAndWait()
        return
def main():
    generations = int(input(
    "How many generations would you like to run this algorithm for? "))
    name = str(input(
    "What song do you want to base your poem off of? "))
    artist = str(input(
    "Which artist is that song made by?"))
    runner = genetic(generations,name,artist)   
    runner.create_poems()
    runner.genetic_algo_runner()
    poem = runner.get_fittest()
    runner.say(poem)
    #runner.reperform_poem("poem_20231120_203758.txt")
    
    
    

if __name__ == "__main__":
    main()
