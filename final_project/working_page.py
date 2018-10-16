import requests
import json
import urllib

url = 'https://bikeindex.org:443/api/v3/search'
qry = urllib.urlencode(params).replace('%3A', ':')

s = requests.Session()
req = requests.Request(method='GET', url=url)
prep = req.prepare()
prep.url = url + qry
r = s.send(prep)

parameters = {'page:':'2', 'per_page':100, 'location':'IP', 'distance':25, 'stolenness':'stolen'}

response = requests.get('https://bikeindex.org:443/api/v3/search?', params=parameters)

#print(response.content)
print(response.url)
#print(response)


# keep going up by one
#response.content is length 0, then stop
