import pronouncing
import numpy as np
class Line:
    def __init__(self,line,theme): #will need index for degradation
        self.theme = theme
        self.line = line #use spacy to turn this into nlp line
    
    def mutate_line(self):
        mutation = np.random.choice(0,3)
        match mutation:
            case 0: #change rhyme word to closer to theme
                pass
            case 1: #change noun to syn
                pass
            case 2: #change verb to synoynm
                pass
            case 3: #change part of speech to closer word to theme
                pass
    pass

    def change_rhyme(self):
        stop_word = word #use spacy to get last word
        part_of_speech = word.pos_ #get broad part of speech
        rhymes = pronouncing.rhymes(word)
        same_pos = []
        for word in rhymes:
            if part_of_speech == word(partofspeech): #same part of speech or add right part of speech
                same_pos.append(word)
        swap_word = np.random.choice(same_pos, p = similarity(x and self.theme))  #use spacy similarity
        replace --> word with swap_word #use spacy
        pass
    

    def change_noun(self):
        nouns = []
        usuable_nouns =[]
        for token in self.line:
            pos = token.pos
            if pos == noun parts:
                nouns.append(token index)
        if nouns.empty():
            return
        mutated_noun = np.random.choice(nouns) #pick least related ones
        syns = get_synonyms(mutated_noun) #use spacy synonyms?
        if syns.empty():
            return
        for synonym in syns:
            pos = mutated_noun.pos
            if(pos is same as synonym.pos or change synoynm pos):
                usuable_nouns.append(synonym)
        replace mutated_noun with random choice of usable_nouns #or do highest similarity

        return

        def change_verb(self):
        #here we choose a verb and then find the type of verb
        # then find synoynms for that verb and conjugate them to the right tense
        # swap out verbs
        










        

        
