
import numpy as np
from line import Line
from lyric_manager import LyricManager


class Poem:
    def __init__(self,lines,song=LyricManager()):
        self.lyric = song
        self.rhyme = 0 # set rhyme scheme here
        self.lines = []
        for line in lines:
            self.lines.append(Line(line,self.lyric))

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
        print(str(choice) + "lines")
        mutated_lines = np.random.choice(lines, size = choice, replace = False)
        for line in mutated_lines:
            line = line.mutate()






    