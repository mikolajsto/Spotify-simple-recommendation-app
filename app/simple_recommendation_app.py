from flask import Flask, jsonify, make_response, request, redirect, url_for
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import yaml
import os
import sys

app = Flask(__name__)

def load_config():
    base_dir = os.getcwd()
    config_path = os.path.join(base_dir, 'config.yaml')
    
    try:
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
        if 'spotify' not in config or 'CLIENT_ID' not in config['spotify'] or 'CLIENT_SECRET' not in config['spotify']:
            print("Error: 'CLIENT_ID' or 'CLIENT_SECRET' not found in the 'spotify' section of the config.yaml file")
            return None
        return config['spotify']
    except FileNotFoundError:
        print(f"Error: 'config.yaml' file not found in {base_dir}. Please check the file location.")
        return None
    except yaml.YAMLError as e:
        print(f"Error loading YAML configuration: {e}")
        return None

try:
    config = load_config()
    print("Configuration loaded:", config)
except Exception as e:
    print(f"Unexpected error while loading configuration: {e}")
    config = None

if config:
    sp_oauth = SpotifyOAuth(
        client_id=config['CLIENT_ID'],
        client_secret=config['CLIENT_SECRET'],
        redirect_uri=config['REDIRECT_URL'],
        scope=config['SCOPE']  # Ensure that the permissions are correctly set
    )
    sp = None
else:
    sp_oauth = None
    sp = None

@app.route('/get_music_recommendations')
def get_music_data():
    global sp_oauth, sp
    if sp_oauth is None:
        return make_response(jsonify({'error': 'Spotify OAuth client was not initialized'}), 500)
    
    token_info = sp_oauth.get_cached_token()
    if not token_info:
        print("No cached token, redirecting to Spotify authorization")
        return redirect(sp_oauth.get_authorize_url())
    
    if not sp:
        sp = spotipy.Spotify(auth=token_info['access_token'])
    
    seed_artists = request.args.getlist('seed_artists')
    seed_tracks = request.args.getlist('seed_tracks')
    
    if not seed_artists and not seed_tracks:
        return make_response(jsonify({'error': 'No initial artists or tracks provided'}), 400)

    print(f"Received seed artists: {seed_artists}")  # Debugging
    print(f"Received seed tracks: {seed_tracks}")    # Debugging

    try:
        rr = sp.recommendations(seed_artists=seed_artists, seed_tracks=seed_tracks, seed_genres=[], limit=10)
        
        songs_list = [song['name'] for song in rr['tracks']]
        artist_list = [artist['album']['artists'][0]['name'] for artist in rr['tracks']]
        pairs = list(zip(artist_list, songs_list))

        first_track = rr['tracks'][0]
        response_data = {
            'Artist_track_pairs': pairs,
            'first_track_album_art': first_track['album']['images'][0]['url'],
            'first_track_album_name': first_track['album']['name'],
            'first_track_artist_name': first_track['album']['artists'][0]['name']
        }

        #user_id = config['USER']
        user_id = sp.current_user()['id']
        track_ids = [track['id'] for track in rr['tracks']]
        playlist = sp.user_playlist_create(user_id, 'New Playlist Name', public=False, description='New Playlist Description')
        sp.user_playlist_add_tracks(user_id, playlist['id'], track_ids)

        response_data['playlist_id'] = playlist['id']

        return make_response(jsonify(response_data), 200)
    except Exception as e:
        return make_response(jsonify({'error': 'Failed to retrieve data', 'details': str(e)}), 500)

@app.route('/callback')
def callback():
    global sp_oauth, sp
    if sp_oauth is None:
        return make_response(jsonify({'error': 'Spotify OAuth client was not initialized'}), 500)

    print("Callback route hit")  # Debugging
    code = request.args.get('code')
    if not code:
        print("No authorization code found in request")  # Debugging
        return make_response(jsonify({'error': 'No authorization code in the request'}), 400)
    
    print(f"Authorization code received: {code}")  # Debugging

    try:
        token_info = sp_oauth.get_access_token(code)
        print(f"Access token received: {token_info}")  # Debugging
        sp = spotipy.Spotify(auth=token_info['access_token'])
        return redirect(url_for('get_music_data'))
    except Exception as e:
        print(f"Error during token exchange: {e}")  # Debugging
        return make_response(jsonify({'error': 'Failed to obtain token', 'details': str(e)}), 500)

if __name__ == '__main__':
    try:
        app.run(debug=True, port=8000)  # Use port 8000
    except Exception as e:
        print(f"Błąd uruchamiania aplikacji Flask: {e}")
        sys.exit(1)
