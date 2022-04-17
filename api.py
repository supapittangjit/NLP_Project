import facebook  # sudo pip install facebook-sdk
import itertools
import json
import re
import requests

access_token = "XXX"
user = 'leehsienloong'

graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'posts', limit=100)

Jstr = json.dumps(posts)
JDict = json.loads(Jstr)

count = 0
for i in JDict['data']:
    allID = i['id']
    try:
        allComments = i['comments']

        for a in allComments['data']:
            count += 1
            print(a['message'])

    except (UnicodeEncodeError):
        pass


print(count)
