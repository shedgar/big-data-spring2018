import jsonpickle
import tweepy
import pandas as pd

import os
os.chdir('week-04')

from twitterkeys import api_key, api_secret
auth = tweepy.AppAuthHandler(api_key, api_secret)
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

def auth(key, secret):
    auth = tweepy.AppAuthHandler(key, secret)
    api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
    if (not api):
        print("Can't Authenticate")
        sys.exit(-1)
    else:
        return api

# HUGE block of code for the scraper in class notes



# notes for pset
for i in range(0,168,24):
    j = range(0,168,1)[i-5]
    if (j > i):
        df['hour'].replace(range(i, i+19, 1), range(5, 24, 1), inplace = True)
        df['hour'].replace()
    else:
        df['hour'].replace(range(j, i+19, 1), range(0,24,1), inplace = True)
