from facepy import GraphAPI
import json

page_id = "100000822072127"
access_token = "EAAEblY8Q9B0BABDE1sIQaKqoRMZCrksO1ynzh2D88QF1fhOsX56ZBQFkBdyUHgyWj5AZA4ZC3h2CMDXaIZC7rpndgK7GbZBYxwwRY7Q3uZAu5u9h2ZAOgN4dyi6hghKALvZAVmRDyMAxkrZBEGXbrzAOhSmriqEATiJzpziYtpfhbvzQZDZD"

graph = GraphAPI(access_token)


data = graph.get(page_id + "/feed", page=True, retry=3,
                 limit=100, fields='message,likes')


i = 0
for p in data:
    print('Downloading posts', i)
    with open('facepydata/content%i.json' % i, 'w') as outfile:
        json.dump(p, outfile, indent=4)
    i += 1
