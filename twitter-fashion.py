import tweepy
import json
import datetime as dt
import time
import os
import sys

consumer_key = '[ENTER YOUR CONSUMER KEY]' 
consumer_secret = '[ENTER YOUR CONSUMER SECRET]'
access_token = '[ENTER YOUR ACCESS TOKEN]'
access_token_secret = '[ENTER YOUR ACCESS TOKEN SECRET]'

def get_authenticated():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    return api

def search_tweets(api):
    search_variable = input("Enter your keyword: ")

    tweet_search = api.search(q=search_variable, count=25, include_entities='false', lang='en')
    
    for tweet in tweet_search:
        tweet.text
        print(tweet.text)


def main():
    #authenticate from Twitter
    api = get_authenticated()

    search_tweets(api)


if __name__ == "__main__":
    main()

