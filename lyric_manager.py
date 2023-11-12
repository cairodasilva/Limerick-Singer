from lyricsgenius import Genius
from collections import Counter
import spacy 
class LyricManager:
    def __init__(self, title="Sunset For the Dead", artist="Tommy Newport"):
        self.nlp = spacy.load('en_core_web_sm') 
        self.title = title
        self.artist = artist
        self.genius = Genius("sgc_vVn5Mvy0s0ejFc2keVpZnvK1I0YI9_pyWwNLTNwrqiRGjiBdkTKzY1jgKu-I")
        self.lyrics = self.get_song_lyics()
        self.nlpsong = self.nlp(self.lyrics)
        self.noundict = self.get_nouns()

    def print_songs(self):
        artist = self.genius.search_artist("Childish Gambino", max_songs=3, sort="title")
        print(artist.songs)

    def get_song_lyics(self):
        song = self.genius.search_song(self.artist, self.title)
        #print(song.lyrics)
        return song.lyrics

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
    


        
def main():
    genius = LyricManager()
    #print(genius.remove_stop_words())
    genius.get_nouns()
    print(genius.get_noun_dict())

    
if __name__ == "__main__":
    main()

    