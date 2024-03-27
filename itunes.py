import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+sys.argv[1])
# print(json.dumps(response.json(), indent=4))

o = response.json()
for song in o['results']:
    print(song['trackName'])