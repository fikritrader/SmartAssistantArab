import requests
import json

def getNewsData():
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=us&'
        'apiKey=2f20dc3cb7464a588609919bbab8608d')
    response = requests.get(url)
    data=[]
    for article in response.json()['articles']:
        data.append([article['title'],article['description'],article['url']])
    return data

def satisfyQuery():
    articles=[]
    newsData = getNewsData()
    for i,article in enumerate(newsData):
        arDic = {
        'id':str(i+1),
        'title':article[0],
        'description':article[1],
        'url':article[2]
        }
        articles.append(arDic)
    return articles[0:3]
