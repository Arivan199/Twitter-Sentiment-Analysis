import os
import tweepy as tw
import pandas as pd 

#function to authorize the twitter API credentials
def author():
    consumer_key=input("Enter consumer_key")
    consumer_secret=input("Enter consumer_secret_key")
    access_token=input("Enter access_token")
    access_secret=input("Enter access_secret_token")
    auth=tw.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    api=tw.API(auth,wait_on_rate_limit=True)
    return api
#function to get tweets from Twitter through Twitter API
def extractdata(api):
    date="2021-01-01"
    search_word="#FarmersProtest OR #SpeakUpForFarmers OR #iamwithfarmers -filter:retweets"
    #collect tweets
    tweets=tw.Cursor(api.search,q=search_word,lang="en",since=date,tweet_mode="extended").items(2000)
    return tweets

api=author()
tweets=extractdata(api)
tweet,retweets,favourites=([],)*3

for t in tweets:
    tweet.append(t.full_text)
    retweets.append(t.retweet_count)
    favourites.append(t.user.favourites_count)
    
df=pd.DataFrame({'Tweet':tweet,'retweet_counts':retweets,'Like_count':favourites})
df.to_csv("Farmer_dataset.csv")
