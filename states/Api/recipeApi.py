import requests
import json

def getRecipeData(engr):
    url = "https://recipe-puppy.p.rapidapi.com/"
    querystring = {"p":"1","i":engr}
    headers = {
        'x-rapidapi-host': "recipe-puppy.p.rapidapi.com",
        'x-rapidapi-key': "5f741dfc09mshb754eb12fbdb275p1e7cf0jsnd5f97d5fff94"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    resp = response.json()
    return resp['results']

def satisfyQuery(eng):
    recipeData = getRecipeData(eng)
    recipes=[]
    for recipe in recipeData:
        recDic = {
        'title':recipe['title'],
        'ingredients':recipe['ingredients'],
        'url':recipe['href']
        }
        recipes.append(recDic)
    return recipes[0:2]