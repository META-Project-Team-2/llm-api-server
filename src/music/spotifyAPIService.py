import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import *

class SpotifyAPIService:
    def __init__(self) -> None:
        client_id = SPOTIFY_CLIENT_ID
        client_secret = SPOTIFY_CLIENT_SECRET

        self.manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        self.client = spotipy.Spotify(client_credentials_manager=self.manager)

    