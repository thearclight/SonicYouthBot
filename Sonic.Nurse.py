import lyricsgenius
genius = lyricsgenius.Genius("X")
#artist = genius.search_artist("Sonic Youth", max_songs=1, sort="title")
#print(artist.songs)
#print(artist.to_json)
#artist.save_lyrics()

#artist = genius.search_artists('Sonic Youth')
#print(artist)

artist = genius.search_artist('29872', artist_id=29872, per_page=50)
for song in artist.songs:
    print(song.title)

    

r = requests.get('')
html = r.text
soup =Beautifulsoup(html, 'html.parser')

consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
consumer_secret = "X"
access_token = "X"
access_token_secret = "X"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

api.update_status('status=tweet')

from lyricsgenius import API, PublicAPI, Genius
    api = API(token)
    public = PublicAPI()
    genius = Genius(token)

genius = lyricsgenius.Genius("x")

r = request.get ('')
for item_number in range (1,100)