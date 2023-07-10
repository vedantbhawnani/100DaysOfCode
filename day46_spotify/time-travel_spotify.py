import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser


# date = input("What date do you wanna travel back to? (YYYY-MM-DD format pls)")
date = '2017-08-12'

r = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
data = r.text

soup = BeautifulSoup(data, 'html.parser')

title = soup.find_all('div', class_='o-chart-results-list-row-container')
songs = [song.find('h3').text.strip() for song in title]
artists = [song.find('h3').find_next('span').text.strip() for song in title]

CLIENT_ID = '0c593ec13877404ea5c070e424aeb177'
CLIENT_SECRET = 'e1b6493ec0034c14bd2d90df288b76ca'
redirect = "http://example.com"
spotify_user = '4h6ngku32qb8449c7jw4857q0'


# spotify_url = f'https://accounts.spotify.com/authorize?{CLIENT_ID}&response_type=code&redirect_url=http%3A%2F%2Fexample.com&scope=playlist-modify-playlist%20playlist-modify-private'
# r = requests.get(spotify_url)

OAuth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=redirect, scope="playlist-modify-private")
token = OAuth.get_cached_token()  


spotify_token = token['access_token']
print(spotify_token)

playlist_id = '1KjqRb13GRuBBDwZ4Hr02n'
daily_mix_1_id = '37i9dQZF1E37z16TnyYL1z'

query = "https://api.spotify.com/v1/playlists/{}/tracks".format(daily_mix_1_id)

spoti_response = requests.get(query, headers= {
    "Content-Type":"application/json",
    "Authorization" : "Bearer {}".format(spotify_token)
})

sp = spotipy.Spotify(auth=spotify_token)
spoti_data = spoti_response.json()

# to get tracks from daily mix 1
# tracks_uri = [item['track']['uri'] for item in spoti_data['items']]
# print(tracks_uri)

# SEARCH USING GET REQUESTS
# spoti_search = f'https://api.spotify.com/v1/search?q=track:24%20Hours&type=track'

# r = requests.get(spoti_search, headers= {
#     "Content-Type":"application/json",
#     "Authorization" : "Bearer {}".format(spotify_token)
# })

# data = r.json()
# print(data)

user = sp.current_user()

song_uri = []

for name in songs:
    song = sp.search(name, 1,0,'track')
    tracks_items = song['tracks']['items']    
    song_link = tracks_items[0]['uri']
    song_uri.append(song_link.split("/")[-1:])
    
    spoti_add_to_playlist = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks?uris={song_link}'
    r = requests.post(spoti_add_to_playlist, headers= {
    "Content-Type":"application/json",
    "Authorization" : "Bearer {}".format(spotify_token)
    })
