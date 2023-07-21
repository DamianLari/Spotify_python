import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

class spot:
    def __init__(self):
        self.sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        self.save_artist_infos('spotify:artist:5QXLMdpKeByOo5ypH9gT13')
        self.display_albums('spotify:artist:5QXLMdpKeByOo5ypH9gT13')
        self.display_top_tracks(3,'spotify:artist:5QXLMdpKeByOo5ypH9gT13')

    def save_artist_infos(self, artist_uri):
        results = self.sp.artist(artist_uri)
    
        with open("artist_infos.json", "w") as json_file:
            json.dump(results, json_file, indent=4)
            
    def display_albums(self, artist_uri):
        results = self.sp.artist_albums(artist_uri, album_type='album')
        albums = results['items']
        while results['next']:
            results = self.sp.next(results)
            albums.extend(results['items'])
        for album in albums:
            print(album['name'])
        return albums
    
    def display_top_tracks(self, nb_tracks,artist_uri):
        results = self.sp.artist_top_tracks(artist_uri)
        albums_list = []
        for track in results['tracks'][:nb_tracks]:
            print("<{}> de l'album <{}>".format(track['name'], track['album']['name']))
            albums_list.append(track['album'])
            
        with open("albums_infos.json", "w") as json_file:
            json.dump(albums_list, json_file, indent=4)
        
spot = spot()