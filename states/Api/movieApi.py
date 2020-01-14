import requests
import json

def getMovieData(title):
    key='2d3ceeff'
    url='http://www.omdbapi.com/'
    params = {'apikey':key,'t':title} 
    r = requests.get(url=url, params=params)
    
    data=[
        r.json()['Plot'],
        r.json()['Year'],
        r.json()['Language'],
        r.json()['Type'],
        r.json()['Rated'],
        r.json()['Genre'],
        r.json()['Awards'],
        r.json()['imdbRating']
    ]
    return data

def satisfyQuery(title):
    newsData = getMovieData(title)
    filmData = {
        'genre':newsData[5],
        'releaseYear':newsData[1],
        'plot':newsData[0],
        'imdbRating':newsData[7],
        'rated':newsData[4],
        'language':newsData[2],
        'type':newsData[3],
        'awards':newsData[6]
    }
    return filmData