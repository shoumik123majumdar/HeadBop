import os
from Spotipy import Spotipy


CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
SCOPE = "user-read-playback-state playlist-modify-public user-top-read"

sp = Spotipy(CLIENT_ID,CLIENT_SECRET,SCOPE)

sp.get_current_user_top_artists(10)

def get_bops():
    return 0

# Helper Method
def check_if_playlist_exists(name = "HeadBop+"):
    playlists = sp.get_current_user_playlists()
    for playlist_name in playlists:
        if(playlist_name == name):
            return True
    return False

if get_bops()>7:
    current_track = sp.get_current_track()
    if check_if_playlist_exists():
        sp.add_to_playlist(name="HeadBop+", song_id=current_track)
    else:
        sp.create_playlist(name="HeadBop+")
        sp.add_to_playlist(name="HeadBop+", song_id=current_track)


"""
"""
