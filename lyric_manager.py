
from collections import Counter
import spacy 
from song_manager import SongManager
class LyricManager:
    def __init__(self, lyrics = SongManager().get_song_lyrics()):
        self.nlp = spacy.load('en_core_web_sm') 
        self.lyrics = lyrics
        self.nlpsong = self.nlp(lyrics)
        self.noundict = self.get_nouns()


    def remove_stop_words(self):
        filtered_tokens = [token for token in self.nlpsong]
        return ' '.join([token.text for token in filtered_tokens])

    def get_nouns(self):
        nouns = [token.text
         for token in self.nlpsong
         if (not token.is_stop and
             not token.is_punct and
             token.pos_ == "NOUN" and token.text != "Verse")]
        nouns = nouns[1:-1]
        noun_dict = Counter(nouns)
        return noun_dict
        
    def get_noun_dict(self):
        return self.noundict

    def get_song_lyrics(self):
        return self.lyrics


        
def main():
    genius = LyricManager()
    #print(genius.remove_stop_words())
    genius.get_nouns()
    print(genius.get_noun_dict())
   

    
if __name__ == "__main__":
    main()

    