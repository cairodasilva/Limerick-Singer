import pronouncing
import spacy
import numpy as np
class Line:
    
    def __init__(self,line): #will need index for degradation
        nlp = spacy.load("en_core_web_sm")
        self.line = nlp(line)

    def getText(self):
        return self.line.text
    
    def mutate(self):
        mutation = np.random.randint(0,3)
        print(mutation)
        match mutation:
            case 0: #change rhyme word to closer to theme
                print("I am changing a rhyme word")
            case 1: #change noun to syn
                print("I am changing a verb")
            case 2: #change verb to synoynm
                print ("I am changing a noun")
        return
            
    
    