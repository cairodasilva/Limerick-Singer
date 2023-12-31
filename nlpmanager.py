"""@author Cairo Dasilva, CSCI 3725, M7
This class manages spacy and all of the nlp"""
import spacy
import numpy as np
from word_manager import WordManager
from textblob import TextBlob
from collections import Counter




class NlpManager:

    def __init__(self,lyric): #will need index for degradation
 
        self.nlp = spacy.load("en_core_web_md")
        self.worder = WordManager()
        self.lyricer = lyric
        self.noun_dict = self.get_nouns()
        self.verb_dict = self.get_verbs()
        self.stop_words = spacy.lang.en.stop_words.STOP_WORDS 
        
    def new_noun(self,text):
        """takes in a line and finds all of the nouns, then picks one and 
        replaces it with a new noun from the song which it selects by similarity"""
        noun_dict = self.noun_dict
        nlptext = self.nlp(text)
        old_nouns =[]
        for token in nlptext:
            if token.pos_ =="NOUN":
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
            if total != 0:
                p = [value / total for value in scores]
                new_noun = np.random.choice(list(noun_dict.keys()),p = p)
            else:  
                new_noun = np.random.choice(list(noun_dict.keys()))
            return (new_noun, replace_index)
        else:
            return (-1)
    def get_similarity(self,text1,text2):
        """returns the similarity between two texts"""
        nlp1 = self.nlp(text1)
        nlp2 = self.nlp(text2)
        return nlp1.similarity(nlp2)

    def get_nouns(self):
        """gets a dictionary of nouns and how often they 
        appear from the inputted song"""
        nlpsong = self.nlp(self.lyricer)
        nouns = [token.text
         for token in nlpsong
         if (not token.is_stop and
             not token.is_punct and
             token.pos_ == "NOUN" and token.text != "Verse" and '[' not
              in token.text and ']' not in token.text)]
        nouns = nouns[1:-1]
        noun_dict = Counter(nouns)
 
        return noun_dict

    def get_verbs(self):
        """makes a dictionary of verbs from the song"""
        verb_dict = {}
        verbs = []
        nlpsong = self.nlp(self.lyricer)
        for token in nlpsong:
            if(not token.is_stop and  not token.is_punct 
            and token.pos_ == "VERB"
            and '[' not in token.text and ']' not in token.text 
            and len(token.text)>2):
                verb_dict[token.text] = token.tag_ 
       
        return verb_dict       

    def new_verb(self,text):
        """finds a verb from the line and gets a new verb from the song to 
        replace it with, it selects based on similarity"""
        old_verbs = []
        scores = []
        nlptext = self.nlp(text)
        for token in nlptext:
            if token.pos_ =="VERB":
                old_verbs.append(token.i)
        if len(old_verbs) > 0:
            replace_index = np.random.choice(old_verbs)
            replace_word = nlptext[replace_index]
            for word in self.verb_dict.keys():
                verb_vector = self.nlp(word)
                score = replace_word.similarity(verb_vector)
                scores.append(score)
            scores = self.min_max(scores)
            total = sum(scores)
            if total != 0:
                p = [value / total for value in scores]
                new_verb = np.random.choice(list(self.verb_dict.keys()),p = p)
            else:  
                new_verb = np.random.choice(list(self.verb_dict.keys()))
            return (new_verb, replace_index)
        else:
            return -1
                
    

    def get_sentiment(self,text):
        """gets the sentiment of a text"""
        testimonial = TextBlob(text)
        return(testimonial.polarity)
        
    

    def min_max(self, array):
        """scales an array of numbers from 0 to 1"""
        min_value = min(array)
        if min_value < 0:
            max_value = max(array)
            scaled_array = [(value - min_value) / (max_value - min_value)
            for value in array]
            return scaled_array
        return array
    def remove_stop_words(self,text):
        """removes stop words from a text"""
        stop_words = spacy.lang.en.stop_words.STOP_WORDS 
        doc = self.nlp(text) 
        filtered_tokens = [token for token in doc if not token.is_stop] 
        return ' '.join([token for token in filtered_tokens])

    def poem_song_similarity(self,poem,song):
        """gets the similarity between a poem and a song"""
        nlppoem = self.nlp(poem)
        nlpsong = self.nlp(song)
        return nlppoem.similarity(nlpsong)




