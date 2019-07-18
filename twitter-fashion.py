import tweepy
import json
import datetime as dt
import time
import os
import sys



def get_authenticated():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    return api

def search_tweets(api):
    #eventually ^ that should take in search variable as an argument
    #search for tweets with the keyword
    search_variable = input("Enter your keyword: ")

    tweet_search = api.search(q=search_variable, count=25, include_entities='false', lang='en')
    #print(tweet_search)

    for tweet in tweet_search:
        tweet.text
        print(tweet.text)


def main():
    #authenticate from Twitter
    api = get_authenticated()

    search_tweets(api)


if __name__ == "__main__":
    main()

