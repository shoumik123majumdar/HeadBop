import spotipy
from spotipy.oauth2 import SpotifyOAuth


class Spotipy():
    def __init__(self, CLIENT_ID, CLIENT_SECRET,SCOPE):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                            client_secret=CLIENT_SECRET,
                                                            redirect_uri="http://localhost:8888/callback",
                                                            scope=SCOPE))
        self.USER_ID = self.sp.current_user()['id']

    #  Helper Method
    def get_artists(self, list):
        returnable = ""
        if (len(list) == 1):
            return str(list[0])
        elif (len(list) == 2):
            return str(list[0]) + " and " + str(list[1])
        else:
            for i in range(len(list) - 1):
                returnable += str(list[i]) + ", "
            returnable += "and " + str(list[len(list) - 1])
            return returnable

    def get_current_track(self, printable=False):
        response = self.sp.current_playback()
        if response != None:
            device_name = response['device']['name']
            song_name = response['item']['name']
            artists = self.get_artists([artist['name'] for artist in response['item']['artists']])
            album_name = response['item']['album']['name']
            if printable: print(
                f'The song currently playing from your {device_name} is {song_name} by {artists} from the album: {album_name}')
            return response['item']['id']
        else:
            if printable: print(
                "Nothing is currently playing"
            )
            return False

    def create_playlist(self, name, description=""):
        self.sp.user_playlist_create(self.USER_ID, public=True, description=description, name=name)

    def get_playlist_id(self, playlist_name):
        list = self.sp.user_playlists(self.USER_ID)['items']
        for item in list:
            if item['name'] == playlist_name:
                return item['id']

    #  See if you can prevent duplicates
    def add_to_playlist(self, playlist_name, song_id=None):
        playlist_id = self.get_playlist_id(playlist_name)
        if song_id is None:
            song_id = [self.get_current_track()]
        self.sp.playlist_add_items(playlist_id, song_id)

    def get_current_user_top(self, track_limit=5, artist_limit=5):
        if self.get_current_track():
            track_response = self.sp.current_user_top_tracks(limit=track_limit)
            list_tracks = [track['name'] for track in track_response['items']]

            artist_response = self.sp.current_user_top_artists(limit=artist_limit)
            list_artists = [artist['name'] for artist in artist_response['items']]

            return list_tracks, list_artists
        else:
            return False


"""
spotify:playlist:6Bd5sDUNS3BGqMjRhuMO95
"""
