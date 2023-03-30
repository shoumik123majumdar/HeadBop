import os
from Spotipy import Spotipy

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
SCOPE = "user-read-playback-state playlist-modify-public user-top-read"

sp = Spotipy(CLIENT_ID,CLIENT_SECRET,SCOPE)

sp.get_top()


"""
spotify:playlist:6Bd5sDUNS3BGqMjRhuMO95
"""
