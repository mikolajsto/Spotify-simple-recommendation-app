Spotify Recommendation App

This is a Flask application that provides music recommendations using the Spotify API.

Setup:

1. Clone the repository:
   git clone https://github.com/your-username/spotify-recommendation-app.git
   cd spotify-recommendation-app

2. Create a virtual environment and activate it:
   python -m venv venv
   On macOS and Linux:
       source venv/bin/activate
   On Windows:
       venv\Scripts\activate

3. Install the dependencies:
   pip install -r requirements.txt

4. Set up your config.yaml file in the config folder with the following content:
   spotify:
     CLIENT_ID: 'your_client_id'
     CLIENT_SECRET: 'your_client_secret'
     USER: 'your_user_id'
     REDIRECT_URL: 'http://localhost:8000/callback'
     SCOPE: 'playlist-modify-public playlist-modify-private'
     PLAYLIST: 'your_playlist_id'

Running the app:

To run the Flask app, use the following command:
   python app/simple_recommendation_app.py

Open your web browser and navigate to:
   http://127.0.0.1:8000/get_music_recommendations?seed_artists=artist_id
to get music recommendations.

Folder structure:

spotify-recommendation-app/
├── app/
│   └── simple_recommendation_app.py
├── config/
│   └── config.yaml
├── requirements.txt
├── README.txt