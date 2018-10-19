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
    consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    access_key = 'XXXXXXXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    access_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
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
time.sleep(1000)  # 1 sec

if __name__ == "__main__":
    main()
