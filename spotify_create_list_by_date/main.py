import requests
import bs4
import spotipy
from spotipy.oauth2 import SpotifyOAuth

spot_client_id="65e60c4e50a24088ae7f2f6d8dded1e9"
spot_client_secret="7fd6953ad9be4b6396668d0f75f27c19"
URL = "https://www.billboard.com/charts/hot-100/"
date_input = input("please enter a date like this YYYY-MM-DD\n")
# date_input = "2013-07-14"
URL += date_input

response = requests.get(URL)
data = response.text
soup = bs4.BeautifulSoup(data, "html.parser")
songs_titles = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

# for i in range(0,len(songs_titls)):
#     print(f"{i+1})"+songs_titls[i].getText())
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=spot_client_id,
        client_secret=spot_client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
song_uris=[]
for i in songs_titles:

    result = sp.search(q=f"track:{i.getText()} year:{date_input.split('-')[0]}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{i.getText()} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date_input} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)