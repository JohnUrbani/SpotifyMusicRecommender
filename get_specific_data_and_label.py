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

ids = { 'ajazz':['spotify:playlist:37i9dQZF1DXbITWG1ZJKYt'],
        'bjazz':['spotify:playlist:37i9dQZF1DWV7EzJMK2FUI'],
        'cjazz':['spotify:playlist:37i9dQZF1DX0SM0LYsmbMT'],
        'djazz':['spotify:playlist:37i9dQZF1DXdziGPHNE40t'],
        'ejazz':['spotify:playlist:37i9dQZF1DWTALrdBtcXjw'],
        'ablues':['spotify:playlist:37i9dQZF1DXd9rSDyQguIk'],
        'bblues':['spotify:playlist:37i9dQZF1DX4rGCw5bMNp1'],
        'cblues':['spotify:playlist:37i9dQZF1DX9cTwPMorHcH'],
        'dblues':['spotify:playlist:37i9dQZF1DX0QNpebF7rcL'],
        'asoul':['spotify:playlist:73sIU7MIIIrSh664eygyjm'],
        'bsoul':['spotify:playlist:37i9dQZF1DWWvhKV4FBciw'],
        'csoul':['spotify:playlist:37i9dQZF1DWULEW2RfoSCi'],
        'dsoul':['spotify:playlist:7Gw1Cnqll2rS761ZLKfaQ3'],
        'esoul':['spotify:playlist:37i9dQZF1DWTx0xog3gN3q']}
        

csv_columns = ["name","artists","danceability","energy","key","loudness","mode","speechiness","acousticness","instrumentalness","liveness","valence","tempo","type","audio_features","id","uri","track_href","analysis_url","duration_ms","time_signature","target"]
csv_file = "specific_data_categorized.csv"
with open(csv_file, 'w+', newline='', encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()

    for genre, pl_id_set in ids.items():
        offset = 0
        song_urls = []

        for pl_id in pl_id_set:
            print(genre, pl_id)
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
                    #try:
                    song_urls.append(response['items'][i].get("track").get("id"))
                    #except:
                    #    print(i)

            client_credentials_manager = SpotifyClientCredentials()
            sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
            sp.trace = True
            
            for i in range(len(song_urls)):
                tids = song_urls[i]

                start = time.time()
                features = sp.audio_features(tids)
                delta = time.time() - start
                
                try:
                    features[0]['target'] = genre
                    features[0]['name'] = sp.track(tids)['name']
                    features[0]['artists'] = sp.track(tids)['artists'][0]['name']
                    dict_data = features
                    for data in dict_data:
                        try:
                            writer.writerow(data)
                        except:
                            print(data)
                except:
                    print('Bad playlist')