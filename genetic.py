from line import Line
from poem import Poem
import numpy as np
import os
class genetic:
    def __init__(self, iterations=0):
        self.iterations = iterations
        self.inspiring_set = []
        self.poems = []
    def create_poems(self):
        dir = "./inspiring_set"
        for file in os.listdir(dir):
            with open(dir + "/" + file, "r") as f:
                poem_lines = f.readlines()
                new_poem = Poem(poem_lines)
                self.poems.append(new_poem)

    def crossover(self,poem1,poem2):
        num_lines = 6
        pivot = np.random.randint(0,5)
        first_poem = poem2
        second_poem = poem1
        if poem1.getFitness() > poem2.getFitness():
            first_poem = poem1
            second_poem = poem2
        section1 = first_poem.getLines()[:pivot]
     
        section2 = second_poem.getLines()[pivot:]
        
        new_poem = Poem(section1 + section2)
        return new_poem


    def genetic_algo(self):
        next_generation = []
        fitnesses =[]
        sum_fitness = 0
        for _ in range(len(self.poems)-1):
            for poem in self.poems:
                fitness = poem.getFitness()
                fitnesses.append(fitness)
                sum_fitness +=  fitness
            fitnessnp = np.array(fitnesses)
            p = fitnessnp / sum_fitness
            poem1,poem2 = np.random.choice(self.poems,p = p,size = 2,
            replace = False)
            new_poem = self.crossover(poem1,poem2)
            new_poem.mutate()
            next_generation.append(new_poem)

"""
    def create_inspiring(self):
        # iterate through all nature poems and get the most fit ones and then 
        #add to inpiring set
        pass
        
    
        
    def parse_files(self):
        #runs through nature poems and adds them to inspiring set
        pass

    def get_fittest_half(self, generation):
        sorted_poems = sorted(generation,key = lambda x: x.get_fitness())
        return sorted_poems[int(len(generation)/2)]

    def genetic_algo(self):
        next_generation = []
        fitnesses =[]
        sum_fitness = 0
        for _ in range(len(self.poems)):
            for poem in self.poems():
                fitness = poem.getFitness()
                fitnesses.append(fitness)
                sum_fitness +=  fitness
            fitnesses = fitnesses / sum_fitness
            poem1,poem2 = np.random.choice(self.poems,p = fitnesses,size = 2,
            replace = False)
            new_poem = self.crossover(poem1,poem2)
            new_poem.mutate()
            next_generation.append(new_poem)

        self.poems = (self.get_fittest_half(self.poems) + \
             self.get_fittest_half(next_generation))
        
    def run_genetic_algo(self):
        for i in range(self.iterations):
            print(f"Running genetic algorithm for generation {i + 1}")
            self.genetic_algo() 

            


         """
def main():
    runner = genetic(0)
    runner.create_poems()
    runner.genetic_algo()
        




if __name__ == "__main__":
    main()


