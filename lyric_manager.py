
from collections import Counter
import spacy 
from song_manager import SongManager
class LyricManager:
    def __init__(self, lyrics = SongManager().get_song_lyrics()):
       
        self.lyrics = lyrics
       




   
   

    def get_song_lyrics(self):
        return self.lyrics


        
def main():
    genius = LyricManager()
    #print(genius.remove_stop_words())
    genius.get_nouns()
    print(genius.get_noun_dict())
    print(genius.lyrics)
   

    
if __name__ == "__main__":
    main()

    