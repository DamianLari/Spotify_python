import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# get username
username = sys.argv[1]

#afp320c0rsf8ufvcrhk1gnos2?si=5c2b3aaf425643ea

try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# create spotify object
spotifyObject = spotipy.Spotify(auth=token)

type(spotifyObject)

#in the terminal: export SPOTIPY_CLIENT_ID='b5bd8713b35e480082f70cb0d15f8e38'
#in the terminal: export SPOTIPY_CLIENT_SECRET='862acf9137ae4c5f897c6cb04c5e0a2d'
#in the terminal: export SPOTIPY_REDIRECT_URI='http://google.com/'
#python3 main.py afp320c0rsf8ufvcrhk1gnos2 (or may be 5c2b3aaf425643ea)
#https://accounts.spotify.com/fr/authorize?client_id=b5bd8713b35e480082f70cb0d15f8e38&response_type=code&redirect_uri=http%3A%2F%2Fgoogle.com%2F


from spotipy.oauth2 import SpotifyClientCredentials

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])