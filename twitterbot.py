import urllib.request, urllib.parse, urllib.error
import json
import time
import random
import requests
import tweepy, sys, time
import requests


## dd/mm/yyyy format
date = time.strftime("%m/%d/%Y")
url = ('http://api.umd.io/v0/courses/list')
uh = urllib.request.urlopen(url)
print('retrieving', url)
data = uh.read().decode()
info = json.loads(data)
#print(info)
print(len(info))

for x in range(1):
    n = random.randint(1,4596)
    n = int(n)

course_id = info[n]['course_id']
name = info[n]['name']
cotd = 'The course of '+ date + ' is: '
tweets = cotd+course_id+ " " + name
t = tweets.replace("(","").replace(")","").replace("'","").replace(",","")


def tweet():
    consumer_key = '0FkoxnMa4hrz4ap4AaQVbZJVp'
    consumer_secret = 'cy3kKQ5Kn7XsIsF52epal1wEHkX1P9AP54r9CLS2vYapbC1SA2'
    access_key = '827360244720422914-A5IbOcT4Ys2G8l52uOLmWiU5gJnozM4'
    access_secret = 'wyIpTcebRZBg9xndkjZ2AlGPXJA1Ubx2olFHpQ5RxSA9Y'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    mystatustext = str(tweets)
    #responeData = requests.get("http://api.icndb.com/jokes/random/?escape=javascript")
    #mystatustext = str('responeData.json()['value']['joke']')
    api.update_status(status=mystatustext)


def main():
    print('tweeted')
while True:
    tweet()
time.sleep(1440)  # 1 sec

if __name__ == "__main__":
    main()
