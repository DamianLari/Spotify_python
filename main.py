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

#in the terminal: export SPOTIPY_CLIENT_ID=''
#in the terminal: export SPOTIPY_CLIENT_SECRET=''
#in the terminal: export SPOTIPY_REDIRECT_URI='http://google.com/'
#python3 main.py afp320c0rsf8ufvcrhk1gnos2 (or may be 5c2b3aaf425643ea)



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
