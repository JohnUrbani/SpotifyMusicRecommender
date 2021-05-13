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

ids = { 'mellow':['spotify:playlist:2OO2mRD8RxanW6eJrI1mri'],
        'hip-hop-chill':['spotify:playlist:0C3G1zXDt47aNR9B0Wi2XF'],
        'electric-night':['spotify:playlist:0nKaimQqqtLBzXhqa9EI22'],
        'party':['spotify:playlist:5KKYWuqg1p9iPpgEiU7EEB'],
        'moving':['spotify:playlist:0KLSjRLWqlYcgAc4vuL34C'],
        'upbeat-summer':['spotify:playlist:2zto0Nkpz6ehIp0GaMcbzT'],
        }
        

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
                    try:
                        song_urls.append(response['items'][i].get("track").get("id"))
                    except:
                        print(i)

            client_credentials_manager = SpotifyClientCredentials()
            sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
            sp.trace = True
            
            for i in range(len(song_urls)):
                tids = song_urls[i]
                try:
                    start = time.time()
                    features = sp.audio_features(tids)
                    delta = time.time() - start
                
                
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