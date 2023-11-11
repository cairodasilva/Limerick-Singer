import pronouncing
import spacy
import numpy as np
class Line:
    
    def __init__(self,line): #will need index for degradation
        nlp = spacy.load("en_core_web_sm")
        self.line = nlp(line)
    def getText(self):
        return self.line.text
    
    