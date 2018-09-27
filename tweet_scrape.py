import tweepy
from tweepy import OAuthHandler
import json
import os
import sys
import pandas as pd
from json_parse import write_json_tweets
def load_api():
    consumer_key=''
    consumer_secret=''
    access_token=''
    access_secret=''

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return tweepy.API(auth)


def tweet_search(api, query, max_tweets):
    searched_tweets = []
    while len(searched_tweets) < max_tweets:
        remaining_tweets = max_tweets - len(searched_tweets)
        try:
            new_tweets = api.search(q=query, count=remaining_tweets,tweet_mode='extended',language='English')
            print('found',len(new_tweets),'tweets')
            if not new_tweets:
                print('no tweets found')
                break
            searched_tweets.extend(new_tweets)
        except tweepy.TweepError:
            print('exception raised, waiting 15 minutes')
            time.sleep(15*60)
            break
    return searched_tweets



def write_tweets(filename,tweets):
    with open ("tweets.txt","a") as e:
        for tweet in tweets:
            tj=tweet._json
            e.write(tj['full_text'])
            e.write('\n')



def get_search_query():
    with open("words.txt") as f:
        query=f.read()
    queries=[]
    for x in query.split(','):
        queries.append(x)
    return queries




def main():
    exitcount = 0

    max_tweets=5
    q=get_search_query()
    for search_phrase in q:

        print('Search phrase =', search_phrase)
        api = load_api()


        tweets= tweet_search(api, search_phrase, max_tweets)
        if tweets:
            write_tweets(filename,tweets)
            write_json_tweets(filename,tweets)

            exitcount = 0
        else:
            exitcount += 1
            if exitcount == 3:
                if search_phrase == search_phrases[-1]:
                    sys.exit('Maximum number of empty tweet strings reached - exiting')
                else:
                    print('Maximum number of empty tweet strings reached - breaking')
                    break


if __name__ == "__main__":
    main()
