import jsonpickle
import tweepy
import pandas as pd
import os
os.chdir('week-04')
from twitter_keys import api_key, api_secret

# create authentication function (from class notes)
def auth(key, secret):
  auth = tweepy.AppAuthHandler(key, secret)
  api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
  # Print error and exit if there is an authentication error
  if (not api):
      print ("Can't Authenticate")
      sys.exit(-1)
  else:
      return api

api = auth(api_key, api_secret)

# tweet parsing function (from class notes)
def parse_tweet(tweet):
  p = pd.Series()
  if tweet.coordinates != None:
    p['lat'] = tweet.coordinates['coordinates'][0]
    p['lon'] = tweet.coordinates['coordinates'][1]
  else:
    p['lat'] = None
    p['lon'] = None
  p['location'] = tweet.user.location
  p['id'] = tweet.id_str
  p['content'] = tweet.text
  p['user'] = tweet.user.screen_name
  p['user_id'] = tweet.user.id_str
  p['time'] = str(tweet.created_at)
  return p

# tweet scraping function (from class notes)
def get_tweets(
    geo,
    out_file,
    search_term = '',
    tweet_per_query = 100,
    tweet_max = 150,
    since_id = None,
    max_id = -1,
    write = False
  ):
  tweet_count = 0
  all_tweets = pd.DataFrame()
  while tweet_count < tweet_max:
    try:
      if (max_id <= 0):
        if (not since_id):
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo
          )
        else:
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            since_id = since_id
          )
      else:
        if (not since_id):
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            max_id = str(max_id - 1)
          )
        else:
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            max_id = str(max_id - 1),
            since_id = since_id
          )
      if (not new_tweets):
        print("No more tweets found")
        break
      for tweet in new_tweets:
        all_tweets = all_tweets.append(parse_tweet(tweet), ignore_index = True)
      max_id = new_tweets[-1].id
      tweet_count += len(new_tweets)
    except tweepy.TweepError as e:
      # Just exit if any error
      print("Error : " + str(e))
      break
  print (f"Downloaded {tweet_count} tweets.")
  if write == True:
      all_tweets.to_json(out_file)
  return all_tweets

# Set a Lat Lon
latlng = '42.359416,-71.093993' # Eric's office (ish)
# Set a search distance
radius = '5mi'
# See tweepy API reference for format specifications
geocode_query = latlng + ',' + radius
# set output file location (use only one)
# file_name = 'data/tweets.json'
file_name = 'data/tweets_search.json'
# set threshold number of Tweets. Note that it's possible
# to get more than one
t_max = 2000
# use only for the second part
search = "dogs"

get_tweets(
  geo = geocode_query,
  tweet_max = t_max,
  write = True,
  out_file = file_name,
  search_term = search)

df_noedits = pd.read_json('data/tweets.json')
dfsearch_noedits = pd.read_json('data/tweets_search.json')

# clean the dataset, more notes on this in class notes from weeks 3+4
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
# use only one of these at a time:
# df = df_noedits
df = dfsearch_noedits


df.drop_duplicates(subset = 'content', keep = False, inplace = True)

# create lists of alternate location names
boston = df[(df['location'].str.lower().str.contains("boston")) | (df['location'].str.contains("BOS"))]['location']
abuja =  df[df['location'].str.lower().str.contains("abuja")]['location']
allston = df[df['location'].str.lower().str.contains("allston")]['location']
atlanta = df[df['location'].str.lower().str.contains("atlanta")]['location']
austin = df[df['location'].str.lower().str.contains("austin")]['location']
brighton = df[df['location'].str.lower().str.contains("brighton, ma")]['location']
bronx = df[df['location'].str.lower().str.contains("bronx")]['location']
brookline = df[df['location'].str.lower().str.contains("brookline")]['location']
brooklyn = df[df['location'].str.lower().str.contains("brooklyn")]['location']
calgary = df[df['location'].str.lower().str.contains("calgary")]['location']
california = df[(df['location'].str.lower().str.contains("california")) & (~ df['location'].str.contains("San"))]['location']
cambridge = df[df['location'].str.lower().str.contains("cambridge")]['location']
charleston = df[(df['location'].str.lower().str.contains("charleston")) & (~df['location'].str.contains("WV"))]['location']
chicago = df[(df['location'].str.lower().str.contains("chicago")) | (df['location'].str.contains("Chicaglo"))]['location']
connecticut = df[(df['location'].str.lower().str.contains("connecticut")) | (df['location'] == "CT")]['location']
dorchester = df[df['location'].str.lower().str.contains("dorchester")]['location']
florida = df[(df['location']=="Florida") | (df['location']=="Florida, USA")]['location']
glasgow = df[df['location'].str.lower().str.contains("glasgow")]['location']
hogwarts = df[df['location'].str.lower().str.contains("hogwarts")]['location']
kansas = df[df['location'].str.lower().str.contains("kansas") & (~df['location'].str.contains("City"))]['location']
london = df[df['location'].str.lower().str.contains("london")]['location']
ma = df[(df['location'].str.strip()=="Massachusetts") | (df['location']=="Massachusetts, USA") | (df['location']=="MA")]['location']
malden = df[df['location'].str.lower().str.contains("malden")]['location']
medford = df[df['location'].str.lower().str.contains("medford")]['location']
mexico = df[df['location'].str.lower().str.contains("méxico")]['location']
miami = df[df['location'].str.lower().str.contains("miami")]['location']
neverland = df[df['location'].str.lower().str.contains("neverland")]['location']
newhampshire = df[df['location'].str.lower().str.contains("new hampshire")]['location']
nyc = df[(df['location'].str.lower().str.contains("new york") & (~df['location'].str.contains("Bronx")) & (~df['location'].str.contains("Brooklyn")) & (~df['location'].str.contains("Ithaca"))) | (df['location']=="ny") | (df['location']=="nyc") | (df['location']=="The Big Apple")]['location']
omaha = df[df['location'].str.lower().str.contains("omaha")]['location']
ontario = df[df['location'].str.lower().str.contains("ontario")]['location']
paris = df[df['location'].str.lower().str.contains("paris")]['location']
philadelphia = df[df['location'].str.lower().str.contains("philly")]['location']
pittsburgh = df[df['location'].str.lower().str.contains("pittsburgh")]['location']
rochester = df[df['location'].str.lower().str.contains("rochester")]['location']
sandiego = df[df['location'].str.lower().str.contains("san diego")]['location']
bayarea = df[df['location'].str.lower().str.contains("bay area")]['location']
seattle = df[df['location'].str.lower().str.contains("seattle")]['location']
somerville = df[df['location'].str.lower().str.contains("somerville")]['location']
texas = df[df['location'].str.contains("texas or something")]['location']
toronto = df[df['location']=="Toronto"]['location']
tucson = df[df['location'].str.lower().str.contains("tucson")]['location']
us = df[(df['location'].str.strip()=="United States") | (df['location']=="United States 😊")]
vancouver = df[df['location'].str.lower().str.contains("vancouver")]['location']
virginia = df[(df['location']=="Virginia") | (df['location']=="Virginia, USA")]['location']
dc = df[df['location'].str.lower().str.contains("washington")]['location']
watertown = df[df['location'].str.lower().str.contains("watertown")]['location']
everett = df[df['location'].str.lower().str.contains("everett")]['location']

# replace location names in dataframe
df['location'].replace(boston, 'Boston, MA', inplace = True)
df['location'].replace(abuja, 'Abuja, Nigeria', inplace = True)
df['location'].replace(allston, 'Allston, MA', inplace = True)
df['location'].replace(atlanta, 'Atlanta, GA', inplace = True)
df['location'].replace(austin, 'Austin, TX', inplace = True)
df['location'].replace(brighton, 'Brighton, MA', inplace = True)
df['location'].replace(bronx, 'Bronx, NY', inplace = True)
df['location'].replace(brookline, 'Brookline, MA', inplace = True)
df['location'].replace(brooklyn, 'Brooklyn, NY', inplace = True)
df['location'].replace(calgary, 'Calgary, Canada', inplace = True)
df['location'].replace(california, 'California, USA', inplace = True)
df['location'].replace(cambridge, 'Cambridge, MA', inplace = True)
df['location'].replace(charleston, 'Charleston, SC', inplace = True)
df['location'].replace(chicago, 'Chicago, IL', inplace = True)
df['location'].replace(connecticut, 'Connecticut, USA', inplace = True)
df['location'].replace(dorchester, 'Dorchester, MA', inplace = True)
df['location'].replace(florida, 'Florida, USA', inplace = True)
df['location'].replace(glasgow, 'Glasgow, Scotland', inplace = True)
df['location'].replace(hogwarts, 'Hogwarts, Scotland', inplace = True)
df['location'].replace(kansas, 'Kansas, USA', inplace = True)
df['location'].replace(london, 'London, England', inplace = True)
df['location'].replace(ma, 'Massachusetts, USA', inplace = True)
df['location'].replace(malden, 'Malden, MA', inplace = True)
df['location'].replace(medford, 'Medford, MA', inplace = True)
df['location'].replace(mexico, 'México', inplace = True)
df['location'].replace(miami, 'Miami, FL', inplace = True)
df['location'].replace(neverland, 'Neverland', inplace = True)
df['location'].replace(newhampshire, 'New Hampshire, USA', inplace = True)
df['location'].replace(nyc, 'New York City', inplace = True)
df['location'].replace(omaha, 'Omaha, NE', inplace = True)
df['location'].replace(ontario, 'Ontario, Canada', inplace = True)
df['location'].replace(paris, 'Paris, France', inplace = True)
df['location'].replace(philadelphia, 'Philadelphia, PA', inplace = True)
df['location'].replace(pittsburgh, 'Pittsburgh, PA', inplace = True)
df['location'].replace(rochester, 'Rochester, NY', inplace = True)
df['location'].replace(sandiego, 'San Diego, CA', inplace = True)
df['location'].replace(bayarea, 'Bay Area, CA', inplace = True)
df['location'].replace(seattle, 'Seattle, WA', inplace = True)
df['location'].replace(somerville, 'Somerville, MA', inplace = True)
df['location'].replace(texas, 'Texas, USA', inplace = True)
df['location'].replace(toronto, 'Toronto, Canada', inplace = True)
df['location'].replace(tucson, 'Tucson, AZ', inplace = True)
df['location'].replace(us, 'United States', inplace = True)
df['location'].replace(vancouver, 'Vancouver, Canada', inplace = True)
df['location'].replace(virginia, 'Virginia, USA', inplace = True)
df['location'].replace(dc, 'Washington DC', inplace = True)
df['location'].replace(watertown, 'Watertown, MA', inplace = True)
df['location'].replace(everett, 'Everett, MA', inplace = True)

# create a pie chart
loc_tweets = df[df['location'] != '']
count_tweets = loc_tweets.groupby('location')['id'].count()
df_count_tweets = count_tweets.to_frame()
df_count_tweets.columns = ['count']
df_count_tweets

df_count_tweets.sort_index()

# get colors from iWantHue
colors = ["#697dc6","#5faf4c","#7969de","#b5b246",
          "#cc54bc","#4bad89","#d84577","#4eacd7",
          "#cf4e33","#894ea8","#cf8c42","#d58cc9",
          "#737632","#9f4b75","#c36960"]

plt.pie(df_count_tweets['count'], labels=df_count_tweets.index.get_values(), shadow=False, colors=colors)

# create scatterplot
tweets_geo = df[df['lon'].notnull() & df['lat'].notnull()]
plt.scatter(tweets_geo['lon'], tweets_geo['lat'], s = 25)

# export CSV (use only one at a time)
# df.to_csv('data/twitter_data_2000tweets.csv', sep=',', encoding='utf-8')
df.to_csv('data/twitter_data_2000search.csv', sep=',', encoding='utf-8')
