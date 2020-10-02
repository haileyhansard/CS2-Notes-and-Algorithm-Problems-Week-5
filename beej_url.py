import urllib.request
import datetime

"""
Import the urllib.request from python.
Retrieve data from cache using the URL to look up the data.
"""
#they key is the data we have, the value is the data we want to get
# so the key is the URL (because we are going to look up by the URL), and the value is the data we get back

#PLAN:
#check cache for url
# if yes return from cache
#if no go get and cache the data and return it
class CacheEntry:
    def __init__(self, data):
        self.data = data
        self.timestamp = datetime.datetime.now().timestamp()

cache = {}

while True:
    url = input("Enter a URL: ")

    if url =='':
        continue

    if url not in cache:
        resp = urllib.request.urlopen(url)
        data = resp.read()
        cache[url] = CacheEntry(data) #we built out a class to use here CacheEntry
        resp.close()
        print("CACHE MISS")
    else:
        print("CACHE HIT")

    #print(data[:75])
    print(cache[url].timestamp())
    print(cache[url][:75])