
# Spotify Recommendation App

This is a Flask application that provides music recommendations using the Spotify API.

## Setup:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/spotify-recommendation-app.git
   cd spotify-recommendation-app
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   ```
   On macOS and Linux:
   ```bash
   source venv/bin/activate
   ```
   On Windows:
   ```bash
   venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your config.yaml file in the config folder with the following content:
   ```yaml
   spotify:
     CLIENT_ID: 'your_client_id'
     CLIENT_SECRET: 'your_client_secret'
     USER: 'your_user_id'
     REDIRECT_URL: 'http://localhost:8000/callback'
     SCOPE: 'playlist-modify-public playlist-modify-private'
     PLAYLIST: 'your_playlist_id'
   ```

   Note:
   - Make sure that the config.yaml file is in the same folder as the script `simple_recommendation_app.py` or adjust the script to point to the correct path of `config.yaml`.
   - Do not change the `SCOPE` value in the config.yaml file as it must be set as specified.
   - If `localhost:8000` does not work, you may need to change it to `localhost:5000`.

## Running the app:

1. To run the Flask app, use the following command:
   ```bash
   python app/simple_recommendation_app.py
   ```

2. Make sure you are logged into Spotify in your web browser.

3. Open your web browser and navigate to:
   ```http
   http://127.0.0.1:8000/get_music_recommendations?seed_artists=artist_id
   ```
   to get music recommendations.

   You can also use `seed_tracks` and `seed_genres` as parameters to get recommendations based on tracks and genres. Example:
   ```http
   http://127.0.0.1:8000/get_music_recommendations?seed_artists=artist_id&seed_tracks=track_id&seed_genres=genre
   ```

## Changing Playlist Name and Description

   ```python
   playlist_id = 'your_playlist_id'
   sp.user_playlist_change_details(user='your_user_id', playlist_id=playlist_id, name='New Playlist Name', description='New Playlist Description')
   ```

Replace `'New Playlist Name'` and `'New Playlist Description'` with your wanted name and description of playlist.

## Folder structure:

spotify-recommendation-app/
├── app/
│   └── simple_recommendation_app.py
├── config/
│   └── config.yaml
├── requirements.txt
├── README.txt