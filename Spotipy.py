import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://localhost:8888/callback",
                                                scope="user-read-playback-state playlist-modify-public user-top-read"))

USER_ID = sp.current_user()['id']

# TODO: Convert this code into a class

#  Helper Method
def get_artists(list):
    returnable = ""
    if(len(list)==1):
        return str(list[0])
    elif(len(list)==2):
        return str(list[0]) + " and " + str(list[1])
    else:
        for i in range(len(list)-1):
            returnable+= str(list[i]) +", "
        returnable += "and " + str(list[len(list)-1])
        return returnable


def get_current_track(print=False):
    response = sp.current_playback()
    if response != None:
        device_name = response['device']['name']
        song_name = response['item']['name']
        artists = get_artists([artist['name'] for artist in response['item']['artists']])
        album_name = response['item']['album']['name']
        if print: print(f'The song currently playing from your {device_name} is {song_name} by {artists} from the album: {album_name}')
        return response['item']['id']
    else:
        return False


def create_playlist(name,description=""):
    sp.user_playlist_create(USER_ID,public = True,description=description,name=name)


def get_playlist_id(playlist_name):
    list = sp.user_playlists(USER_ID)['items']
    for item in list:
        if item['name'] == playlist_name:
            return item['id']


#  See if you can prevent duplicates
def add_to_playlist(playlist_name,song_id = [get_current_track()]):
    playlist_id = get_playlist_id(playlist_name)
    sp.playlist_add_items(playlist_id,song_id)


def get_current_user_top(track_limit=5, artist_limit=5):
    if get_current_track():
        track_response = sp.current_user_top_tracks(limit = track_limit)
        list_tracks = [track['name'] for track in track_response['items']]

        artist_response = sp.current_user_top_artists(limit = artist_limit)
        list_artists = [artist['name'] for artist in artist_response['items']]

        return list_tracks,list_artists
    else:
        return False



print(get_current_user_top(25,25))


"""
spotify:playlist:6Bd5sDUNS3BGqMjRhuMO95
"""
