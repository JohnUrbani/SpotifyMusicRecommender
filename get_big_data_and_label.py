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

ids = { ''''indie':['spotify:playlist:37i9dQZF1DX2Nc3B70tvx0'],
        'indie':['spotify:playlist:37i9dQZF1DXdbXrPNafg9d'],
        'indie':['spotify:playlist:37i9dQZF1DWWEcRhUVtL8n'],
        'rock':['spotify:playlist:37i9dQZF1DWXRqgorJj26U'],
        'rock':['spotify:playlist:37i9dQZF1DX1rVvRgjX59F'],
        'rock':['spotify:playlist:37i9dQZF1DX1spT6G94GFC'],
        'rock':['spotify:playlist:37i9dQZF1DWWwzidNQX6jx'],
        'pop':['spotify:playlist:37i9dQZF1DXcBWIGoYBM5M'],
        'pop':['spotify:playlist:37i9dQZF1DX0kbJZpiYdZl'],
        'pop':['spotify:playlist:37i9dQZF1DWUa8ZRTfalHk'],
        'pop':['spotify:playlist:37i9dQZF1DX2L0iB23Enbq'],
        'pop':['spotify:playlist:37i9dQZF1DXbYM3nMM0oPk'],
        'hiphop':['spotify:playlist:37i9dQZF1DX0XUsuxWHRQd'],
        'hiphop':['spotify:playlist:37i9dQZF1DX6GwdWRQMQpq'],
        'hiphop':['spotify:playlist:37i9dQZF1DX2RxBh64BHjQ'],
        'hiphop':['spotify:playlist:37i9dQZF1DWY4xHQp97fN6'],
        'country':['spotify:playlist:37i9dQZF1DX1lVhptIYRda'],
        'country':['spotify:playlist:37i9dQZF1DWW7RgkOJG32Y'],
        'country':['spotify:playlist:37i9dQZF1DX05oRSrPGj3d'],
        'country':['spotify:playlist:37i9dQZF1DWTkxQvqMy4WW'],
        'country':['spotify:playlist:37i9dQZF1DWYnwbYQ5HnZU'],
        'randb':['spotify:playlist:37i9dQZF1DX4SBhb3fqCJd'],
        'randb':['spotify:playlist:37i9dQZF1DWUzFXarNiofw'],
        'randb':['spotify:playlist:37i9dQZF1DX4y8h9WqDPAE'],
        'randb':['spotify:playlist:37i9dQZF1DWYmmr74INQlb'],
        'randb':['spotify:playlist:37i9dQZF1DWXbttAJcbphz'],
        'randb':['spotify:playlist:37i9dQZF1DX6VDO8a6cQME'],
        'latin':['spotify:playlist:37i9dQZF1DX10zKzsJ2jva'],
        'latin':['spotify:playlist:37i9dQZF1DX1hVRardJ30X'],
        'latin':['spotify:playlist:37i9dQZF1DX4OjfOteYnH8'],
        'latin':['spotify:playlist:37i9dQZF1DWZoF06RIo9el'],
        'latin':['spotify:playlist:37i9dQZF1DX5AVYhCeISA6'],
        'dance':['spotify:playlist:37i9dQZF1DX4dyzvuaRJ0n'],
        'dance':['spotify:playlist:37i9dQZF1DX8tZsk68tuDw'],
        'dance':['spotify:playlist:37i9dQZF1DWZ7eJRBxKzdO'],
        'dance':['spotify:playlist:37i9dQZF1DXa2PvUpywmrr'],
        'folk':['spotify:playlist:37i9dQZF1DXaUDcU6KDCj4'],
        'folk':['spotify:playlist:37i9dQZF1DWYV7OOaGhoH0'],
        'folk':['spotify:playlist:37i9dQZF1DX2taNm7KfjOX']}
'''
        'jazz':['spotify:playlist:37i9dQZF1DWXIuW81skHVz'],
        'jazz':['spotify:playlist:37i9dQZF1DWW2c0C8Vb2IR'],
        'jazz':['spotify:playlist:37i9dQZF1DWUb0uBnlJuTi'],
        'jazz':['spotify:playlist:37i9dQZF1DWTR4ZOXTfd9K'],
        #'jazz':['spotify:playlist:37i9dQZF1DX0SM0LYsmbMT'],
        'classical':['spotify:playlist:37i9dQZF1DWWEJlAGA9gs0'],
        'classical':['spotify:playlist:37i9dQZF1DWV0gynK7G6pD'],
        'classical':['spotify:playlist:37i9dQZF1DX17GkScaAekA'],
        'classical':['spotify:playlist:37i9dQZF1DWVFeEut75IAL'],
        'soul':['spotify:playlist:37i9dQZF1DX0H8hDpv38Ju'],
        'soul':['spotify:playlist:37i9dQZF1DWULEW2RfoSCi'],
        'soul':['spotify:playlist:37i9dQZF1DWTx0xog3gN3q'],
        'soul':['spotify:playlist:37i9dQZF1DXaXDsfv6nvZ5'],
        'soul':['spotify:playlist:37i9dQZF1DWWvhKV4FBciw'],
        'punk':['spotify:playlist:37i9dQZF1DX0KpeLFwA3tO'],
        'punk':['spotify:playlist:37i9dQZF1DX9wa6XirBPv8'],
        'punk':['spotify:playlist:37i9dQZF1DXa9wYJr1oMFq'],
        'punk':['spotify:playlist:37i9dQZF1DXasneILDRM7B'],
        'punk':['spotify:playlist:37i9dQZF1DX3LDIBRoaCDQ'],
        #'kpop':['spotify:playlist:37i9dQZF1DX9tPFwDMOaN1'],
        #'kpop':['spotify:playlist:37i9dQZF1DX4FcAKI5Nhzq'],
        #'kpop':['spotify:playlist:37i9dQZF1DX14fiWYoe7Oh'],
        #'kpop':['spotify:playlist:37i9dQZF1DXe5W6diBL5N4'],
        #'kpop':['spotify:playlist:37i9dQZF1DX0018ciYu6bM'],
        'metal':['spotify:playlist:37i9dQZF1DWTcqUzwhNmKv'],
        'metal':['spotify:playlist:37i9dQZF1DX5J7FIl4q56G'],
        'metal':['spotify:playlist:37i9dQZF1DWXIcbzpLauPS'],
        'metal':['spotify:playlist:37i9dQZF1DXcfZ6moR6J0G'],
        'reggae':['spotify:playlist:37i9dQZF1DWX1DwkjCqoyw'],
        'reggae':['spotify:playlist:37i9dQZF1DX9MrAJRR2Zxk'],
        'reggae':['spotify:playlist:37i9dQZF1DXan38dNVDdl4'],
        'reggae':['spotify:playlist:37i9dQZF1DWSiyIBdVQrkk'],
        'reggae':['spotify:playlist:37i9dQZF1DX7GUbRHVEX42']}
        

csv_columns = ["name","artists","danceability","energy","key","loudness","mode","speechiness","acousticness","instrumentalness","liveness","valence","tempo","type","audio_features","id","uri","track_href","analysis_url","duration_ms","time_signature","target"]
csv_file = "big_data_categorized.csv"
with open(csv_file, 'w+', newline='') as csvfile:
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
                    song_urls.append(response['items'][i].get("track").get("id"))

            client_credentials_manager = SpotifyClientCredentials()
            sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
            sp.trace = True
            
            for i in range(len(song_urls)):
                tids = song_urls[i]

                start = time.time()
                features = sp.audio_features(tids)
                delta = time.time() - start
                
                features[0]['target'] = genre
                features[0]['name'] = sp.track(tids)['name']
                features[0]['artists'] = sp.track(tids)['artists'][0]['name']
                dict_data = features
                for data in dict_data:
                    writer.writerow(data)