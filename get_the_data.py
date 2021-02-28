from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
import json
import spotipy
import time
import sys
import json 
import csv

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

pl_id = 'spotify:playlist:37i9dQZEVXbNG2KDcFcKOF'
offset = 0

song_urls = []

while True:
    response = sp.playlist_items(pl_id,
                                 offset=offset,
                                 fields='items.track.id,total',
                                 additional_types=['track'])
    
    if len(response['items']) == 0:
        break
        
    pprint(response['items'])
    offset = offset + len(response['items'])
    print(offset, "/", response['total'])

    for i in range(len(response['items'])):
        song_urls.append(response['items'][i].get("track").get("id"))

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = True

csv_columns = ["name","artists","danceability","energy","key","loudness","mode","speechiness","acousticness","instrumentalness","liveness","valence","tempo","type","audio_features","id","uri","track_href","analysis_url","duration_ms","time_signature"]
csv_file = "data.csv"
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()

    #song_urls = ["3zJxVJVwUIm03NLj7M3Him"]

    for i in range(len(song_urls)):
        tids = song_urls[i]
        #print(tids)

        start = time.time()
        features = sp.audio_features(tids)
        delta = time.time() - start
        #print(json.dumps(features, indent=4))
        #print("features retrieved in %.2f seconds" % (delta,))
        
        #print(sp.track(tids))
        
        features[0]['name'] = sp.track(tids)['name']
        features[0]['artists'] = sp.track(tids)['artists'][0]['name']#['external_urls']['spotify']
        dict_data = features
        for data in dict_data:
            writer.writerow(data)