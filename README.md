# Spotify Recommendation App

![Logo](./images/simple_recommendation_app_logo.png)

This is a **Flask** application that provides music recommendations using the **Spotify API**.

##### Setup:

#### 1. Clone the repository:

   git clone https://github.com/mikolajsto/Spotify-simple-recommendation-app.git
   cd spotify-recommendation-app

#### 2. Create a virtual environment and activate it:

   python -m venv venv

   ***On macOS and Linux:***

   source venv/bin/activate

   ***On Windows:***

   venv\Scripts\activate

#### 3. Install the dependencies:

   pip install -r requirements.txt

#### 4. Set up your [config.yaml file](./app/config.yaml) with the following content:

   spotify:
     CLIENT_ID: 'your_client_id'
     CLIENT_SECRET: 'your_client_secret'
     USER: 'your_user_id'
     REDIRECT_URL: 'http://localhost:8000/callback'
     SCOPE: 'playlist-modify-public playlist-modify-private'
     PLAYLIST: 'your_playlist_id'

   Note:
   - Make sure that the config.yaml file is in the same folder as the script `simple_recommendation_app.py` or adjust the script to point to the correct path of `config.yaml`.
   - Do not change the `SCOPE` value in the config.yaml file as it must be set as specified.
   - If `localhost:8000` does not work, you may need to change it to `localhost:5000`.

## Running the app:

#### 1. To run the Flask app, use the following command:

   python app/simple_recommendation_app.py

#### 2. Make sure you are logged into Spotify in your web browser.

#### 3. Open your web browser and navigate to:

   http://127.0.0.1:8000/get_music_recommendations?seed_artists=artist_id

   to get music recommendations.

   You can also use `seed_tracks` and `seed_genres` as parameters to get recommendations based on tracks and genres. Example:

   http://127.0.0.1:8000/get_music_recommendations?seed_artists=artist_id&seed_tracks=track_id&seed_genres=genre

[**Changing Playlist Name and Description**](./app/simple_recommendation_app.py#L88)

   playlist = sp.user_playlist_create(user_id, 'New Playlist Name', public=False, description='New Playlist Description')

Replace `'New Playlist Name'` and `'New Playlist Description'` with your wanted name and description of playlist.

#### 📁 Folder structure:

```plaintext
spotify-recommendation-app/
├── app/
│   ├── simple_recommendation_app.py
│   └── config.yaml
├── images/
│   └── simple_recommendation_app_logo.png
├── project-description/
│   ├── Spotify_prosty_rekomender_muzyczny_PL.pdf
│   └── Spotify_Recommendation_App_EN.pdf
├── requirements.txt
└── README.md
```

_*Logo was created by DALL-E_