"""@author Cairo Dasilva, CSCI 3725, M7
This class manages the spotify aspect of the poem"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
class Spotify:
    def __init__(self, song,artist):
        client_id = '92cb50f05d5c46eebc01c9b73ca1c802'
        client_secret = '3dfb3a8fdc404a88876990df9e89ab61'
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials
        (client_id=client_id, client_secret=client_secret))
        query = f'{song} artist:{artist}'
        results = self.sp.search(q=query, type='track', limit=1)
        if results['tracks']['items']:
            self.track_id = results['tracks']['items'][0]['id']
        else:
            print(f'No results found for "{song}" by "{artist}"')



    def get_valence(self):  
            """gets the valance of the song that's inputted""" 
            track_id = self.track_id
            track_features = self.sp.audio_features([track_id])
            valence = track_features[0]['valence']
            return valence
