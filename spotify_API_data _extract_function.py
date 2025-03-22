import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime


def lambda_handler(event, context):
    cilent_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')

    client_credentials_manager = SpotifyClientCredentials(client_id=cilent_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    playlists = sp.user_playlists('spotify')

    playlist_URI = "3cEYpjA9oz9GiPac4AsH4n"
    playlist_URI

    spotify_data = sp.playlist_tracks(playlist_URI)

    cilent = boto3.client('s3')

    filename = "spotify_raw_" + str(datetime.now()) + ".json"

    cilent.put_object(
        Bucket="spotify-etl-project-siddhi",
        Key="raw_data/to_processed/" + filename,
        Body=json.dumps(spotify_data)
        )