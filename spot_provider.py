import spotipy
import json

class Album:
    def __init__(self,sp):
        self.sp=sp
           
    def get_list(self, artist_uri):
        results = self.sp.artist_albums(artist_uri, album_type='album')
        albums = results['items']
        while results['next']:
            results = self.sp.next(results)
            albums.extend(results['items'])
        return albums