from lyricsgenius import Genius

class SongManager:
    def __init__(self, title="Sunset For the Dead", artist="Tommy Newport"):
        self.title = title
        self.artist = artist
        self.genius = Genius("sgc_vVn5Mvy0s0ejFc2keVpZnvK1I0YI9_pyWwNLTNwrqiRGjiBdkTKzY1jgKu-I")
        self.lyrics = self.make_song_lyrics()
        
    def make_song_lyrics(self):
        song = self.genius.search_song(self.artist, self.title)
        return song.lyrics

    def get_song_lyrics(self):
        return self.lyrics
 
        
def main():
    print("songgers")

    
if __name__ == "__main__":
    main()

    