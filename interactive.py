from youtubeAPI import *

def showMenu():
    print('0. exit')
    print('1. Find by genre')


def returnByGenre():
    userGenre = input('Input genre: ')
    userLimit = int(input('Input limit: '))
    songs = findByGenre(userGenre, userLimit)
    if songs != None:
        for song in songs:
            print(song)