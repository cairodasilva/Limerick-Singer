import spacy
import numpy as np
from word_manager import WordManager

from collections import Counter


class NlpManager:

    def __init__(self,lyric): #will need index for degradation
        print("new nlp manager")
        self.nlp = spacy.load("en_core_web_md")
        self.worder = WordManager()
        self.lyricer = lyric
        self.noun_dict = self.get_nouns()

            
    def new_noun(self,text):
        noun_dict = self.noun_dict
        nlptext = self.nlp(text)
        old_nouns =[]
        for token in nlptext:
            if token.pos_ =="NOUN" and token.i < len(nlptext) - 1:
                old_nouns.append(token.i)
        if len(old_nouns) > 0:
            replace_index = np.random.choice(old_nouns)
            replace_word = nlptext[replace_index]
            scores = []
            for word in noun_dict.keys():
                noun_vector = self.nlp(word)
                score = replace_word.similarity(noun_vector)
                scores.append(score)
            scores = self.min_max(scores)
            total = sum(scores)
            p = [value / total for value in scores]
            new_noun = np.random.choice(list(noun_dict.keys()),p = p)
            print(new_noun)
            return (new_noun, replace_index)
        else:
            return (-1)

    def get_nouns(self):
        nlpsong = self.nlp(self.lyricer)
        nouns = [token.text
         for token in nlpsong
         if (not token.is_stop and
             not token.is_punct and
             token.pos_ == "NOUN" and token.text != "Verse")]
        nouns = nouns[1:-1]
        noun_dict = Counter(nouns)
        return noun_dict
   
    

    def min_max(self, array):
        min_value = min(array)
        if min_value < 0:
            max_value = max(array)
            scaled_array = [(value - min_value) / (max_value - min_value) for value in array]
            return scaled_array
        return array
        
    





