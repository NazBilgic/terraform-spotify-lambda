import os
import requests
from base64 import b64encode

# Environment variables (set in Lambda or via Terraform)
CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
CLIENT_SECRET = os.environ['SPOTIFY_CLIENT_SECRET']
REFRESH_TOKEN = os.environ['SPOTIFY_REFRESH_TOKEN']
PLAYLIST_ID = os.environ['SPOTIFY_PLAYLIST_ID']

def get_access_token():
    token_url = "https://accounts.spotify.com/api/token"
    auth_header = b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN
    }

    response = requests.post(token_url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()['access_token']

def add_tracks_to_playlist(access_token):
    url = f"https://api.spotify.com/v1/playlists/{PLAYLIST_ID}/tracks"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Example song URIs (replace with your own)
    tracks = {
    "uris": [
        "spotify:track:2IQz2JtlZ4GjMuXcusYF2i",  # Song 1
        "spotify:track:1HbcclMpw0q2WDWpdGCKdS",  # Song 2
        "spotify:track:3IAVf2B5Omk3gy9JwDE42f",  # Song 3
        "spotify:track:3rmo8F54jFF8OgYsqTxm5d",  # Song 4
        "spotify:track:3di5hcvxxciiqwMH1jarhY"   # Song 5
    ]
}

        

    response = requests.post(url, headers=headers, json=tracks)
    response.raise_for_status()
    print("✅ Tracks added successfully!")

def lambda_handler(event, context):
    try:
        access_token = get_access_token()
        add_tracks_to_playlist(access_token)
        return {
            "statusCode": 200,
            "body": "Playlist updated successfully."
        }
    except Exception as e:
        print("❌ Error:", str(e))
        return {
            "statusCode": 500,
            "body": str(e)
        }
