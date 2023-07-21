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

#in the terminal: export SPOTIPY_CLIENT_ID='5c2b3aaf425643ea'