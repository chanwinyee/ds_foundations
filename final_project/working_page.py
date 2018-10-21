# !pip install requests
# !pip3 install requests
import requests
import json
import urllib
# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# %matplotlib inline

data = []
page_number = 1
#should_request == True
#for i in range(3):

def get_bike_data():
    url = 'https://bikeindex.org:443/api/v3/search?'
    parameters = {'page:':str(page_number),
              'per_page':100,
              'location':'IP',
              'distance':25,
              'stolenness':'stolen'}
    qry = urllib.parse.urlencode(parameters).replace('%3A', '')
    s = requests.Session() #Create a Session object -  <requests.sessions.Session object at 0x1016c0198>
    req = requests.Request(method='GET', url=url) #<Request [GET]>
    prep = req.prepare() #<PreparedRequest [GET]>
    prep.url = url + qry #https://bikeindex.org:443/api/v3/search?page=2&per_page=100&location=IP&distance=25&stolenness=stolen
    result = s.send(prep) #<Response [200]>
    result.raise_for_status()

    if result.status_code == 200:
        #ADD TO MY DATA
        data.extend(result.json()['bikes'])

while len(result['bikes']) > 0:
    page_number = page_number + 1
    if len(result['bikes']) == 0:
        break


# dat = []
# for i in range(3):
#
#     url = 'https://bikeindex.org:443/api/v3/search?'
#     parameters = {'page:':str(i+1),
#               'per_page':100,
#               'location':'IP',
#               'distance':25,
#               'stolenness':'stolen'}
#     qry = urllib.parse.urlencode(parameters).replace('%3A', '')
#     s = requests.Session() #Create a Session object -  <requests.sessions.Session object at 0x1016c0198>
#     req = requests.Request(method='GET', url=url) #<Request [GET]>
#     prep = req.prepare() #<PreparedRequest [GET]>
#     prep.url = url + qry #https://bikeindex.org:443/api/v3/search?page=2&per_page=100&location=IP&distance=25&stolenness=stolen
#     result = s.send(prep) #<Response [200]>
#     result.raise_for_status()
#
#     if result.status_code == 200:
#         #ADD TO MY DATA
#         dat.extend(result.json()['bikes'])
