
import numpy as np
from line import Line
import pronouncing
class Poem:
    def __init__(self,lines):
        self.rhyme = 0 # set rhyme scheme here
        self.lines = []
        for line in lines:
            self.lines.append(Line(line))
    def getFitness(self):
        return np.random.rand()

    def getLines(self):
        lines = []
        for line in self.lines:
            lines.append(line.getText())
        return lines






    