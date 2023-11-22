"""@author Cairo Dasilva, CSCI 3725, M7
This class creates song lyrics using the lyricsgenius API"""
from lyricsgenius import Genius

class SongManager:
    def __init__(self, title="Sunset For the Dead", artist="Tommy Newport"):
        print("init")
        self.title = title
        self.artist = artist
        self.genius = Genius("sgc_vVn5Mvy0s0ejFc2keVpZnvK1I0YI9_pyWwNLTNwrqiRGjiBdkTKzY1jgKu-I")
        self.lyrics = ''

    def make_song_lyrics(self):
        """searches for the song and gets song lyrics"""
        self.lyrics = self.genius.search_song(self.artist, self.title).lyrics

        return self.lyrics

    def get_song_lyrics(self):
        """returns the song lyrics"""
        if self.lyrics == '':
            return self.make_song_lyrics()
        return self.lyrics
 


    