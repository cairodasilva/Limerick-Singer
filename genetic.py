"""@author Cairo Dasilva, CSCI 3725, M7
This class manages the poetry generation and runs the genetic algorithm"""
from line import Line
import datetime
from poem import Poem
import numpy as np
import os
from song_manager import SongManager
from nlpmanager import NlpManager
from spotify import Spotify
import pyttsx3
class Genetic:
    def __init__(self, iterations = 4, name = '', artist=''):
        self.iterations = iterations
        self.inspiring_set = []
        self.poems = []
        if name != '' or artist != '':
            self.name = name
            self.artist = artist
        else:
            self.name = "white ferrari"
            self.artist = "frank ocean"
        print(self.name)
        print(self.artist)
        self.song = SongManager(self.artist,self.name).make_song_lyrics()
        self.spot = Spotify(self.name,self.artist)
        self.nlp = NlpManager(self.song)
        self.valence = self.spot.get_valence()
    
    def create_poems(self):
        """uses the inspiring set poem text files and 
        turns them into poem objects"""
        dir = "./inspiring_set"
        for file in os.listdir(dir):
            with open(dir + "/" + file, "r") as f:
                poem_lines = f.readlines()
                new_poem = Poem(poem_lines,self.song,self.nlp,self.valence)
                self.poems.append(new_poem)
   

    def crossover(self,poem1,poem2):
        """Takes in two poems and cross them over at a random pivot point"""
        num_lines = 6
        pivot = np.random.randint(0,num_lines-1)
        first_poem = poem2
        second_poem = poem1
        if poem1.get_fitness() > poem2.get_fitness():
            first_poem = poem1
            second_poem = poem2
        section1 = first_poem.get_lines()[:pivot]
     
        section2 = second_poem.get_lines()[pivot:]
        
        new_poem = Poem(section1 + section2,self.song,self.nlp,self.valence)
        new_poem.normalize_rhymes()
        return new_poem


    def genetic_algo(self):
        """runs one generation of the genetic algorithm, which first
         selects which poems to cross over and then mutates the new poem  """
        next_generation = []
        fitnesses =[]
        sum_fitness = 0
        for poem in self.poems:
                fitness = poem.get_fitness()
                fitnesses.append(fitness)
                sum_fitness +=  fitness
        fitnessnp = np.array(fitnesses)
        p = fitnessnp / sum_fitness
        for _ in range(len(self.poems)):
            poem1,poem2 = np.random.choice(self.poems,p=p,size = 2,
            replace = False)
            new_poem = self.crossover(poem1,poem2)
            new_poem.mutate()
            new_poem.normalize_rhymes()
            next_generation.append(new_poem)
        old_gen = self.fittest_half(self.poems)
        new_gen = self.fittest_half(next_generation)
        self.poems = new_gen + old_gen

    def fittest_half(self,generation):
        """gets the fittest half of the poems, note that it takes the first half
        because fitter poems have a lower score"""
        sorted_poems = sorted(generation, key = lambda x : x.get_fitness())
        return sorted_poems[:int(len(generation)/2)]

    def genetic_algo_runner(self):
        """iterates over a given number of generations"""
        for i in range(self.iterations):
            print(f"Running genetic algorithm for generation {i + 1}")
            self.genetic_algo() 
    def print_poems(self):
        """prints all of the poems in the current generation"""
        for poem in self.poems:
            print(poem.get_text())
    def get_fittest(self):
        """gets the fittest poem in the current generation and writes it to a 
        new file in previous poems"""
        sorted_poems = sorted(self.poems, key = lambda x : x.get_fitness())
        top_poem =  (sorted_poems[0].get_text())
        fitness = sorted_poems[0].get_fitness()
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
        """says text"""
        engine = pyttsx3.init()  
        engine.setProperty('rate', 150)  # setting up new voice rate
        engine.setProperty('volume', 0.8) 
        for item in text:
            engine.say(item)
            engine.runAndWait()
    
    def reperform_poem(self, file):
        """recites an old poem from previous poems"""
        dir = f"./previous_poems/{file}"
        with open(dir , "r") as f:
            poem_lines = f.readlines()
        engine = pyttsx3.init()  
        engine.setProperty('rate', 140)  # setting up new voice rate
        engine.setProperty('volume', 1) 
        for line in poem_lines:
            if "Fitness" in line:
                break
            engine.say(line)
            engine.runAndWait()
        return

    
    
    


