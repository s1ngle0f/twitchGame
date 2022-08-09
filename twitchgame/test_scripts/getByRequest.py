import time

import grequests

url = 'https://www.twitch.tv/'
channel = 'buster'
url += channel

data = grequests.get(url)
print(data.text) 