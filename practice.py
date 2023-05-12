import requests

api_key="1dcc1fda-34a0-4a5a-a5f1-4c6be58450ce"
word = "potato"
url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"

res = requests.get(url)

definitions = res.json()

for  definition in definitions :
    print(definition)
