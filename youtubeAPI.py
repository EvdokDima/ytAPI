import random

from ytmusicapi import YTMusic

ytmusic = YTMusic()

def findByGenre(userGenre: str, limit: int):
    catalog = ytmusic.get_mood_categories()
    for genreIndex in range(len(catalog['Genres'])):
        if catalog['Genres'][genreIndex]['title'] == userGenre:
            songs = ytmusic.get_mood_playlists(catalog['Genres'][genreIndex]['params'])
            titles = []
            item = 0
            while item in range(limit if limit <= len(songs) else len(songs)):
                song = ytmusic.get_watch_playlist(playlistId=songs[random.randint(0, len(songs) - 1)]['playlistId'], limit=1)
                if song['tracks'][0]['title'] not in titles:
                    titles.append(song['tracks'][0]['title'])
                    item += 1
            return titles
