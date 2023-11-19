from lyricsgenius import Genius

class SongManager:
    def __init__(self, title="Sunset For the Dead", artist="Tommy Newport"):
        print("init")
        self.title = title
        self.artist = artist
        self.genius = Genius("sgc_vVn5Mvy0s0ejFc2keVpZnvK1I0YI9_pyWwNLTNwrqiRGjiBdkTKzY1jgKu-I")
        self.lyrics = ''

    def make_song_lyrics(self):
        self.lyrics = self.genius.search_song(self.artist, self.title).lyrics

        return self.lyrics

    def get_song_lyrics(self):
        if self.lyrics == '':
            return self.make_song_lyrics()
        return self.lyrics
 


    