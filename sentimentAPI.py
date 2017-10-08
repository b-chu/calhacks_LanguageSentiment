#dependencies needed: tweepy, google cloud platform, haxor, gsearch, termcolor
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

from hackernews import HackerNews
hn = HackerNews()

from gsearch.googlesearch import search

import os

import termcolor
from termcolor import colored

from sentimentNews import news

consumer_key = 'MGDSQ8j3dQYboOittNFGrp4lo'
consumer_secret = 'bVv3gkh3d2PbCbnrQ65DXhhy2uH3XT0c1VXJ29MEuiwDUm27sl'
access_token = '2425664702-MZBjlw7AXstFZuPF0m5lMg4lwUAQwjp67300Z1S'
access_secret = 'ajXytC8FDpvKA5hSeENUwcBw70Yv8VQ0MYHKl4QSMWtwX'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
tApi = tweepy.API(auth)

def print_result(annotations):
    score = annotations.document_sentiment.score

    if score > .3:
        print(colored('Overall Sentiment: score of {} '.format(score), 'green'))
        return 0
    if score < -.3:
        print(colored('Overall Sentiment: score of {} '.format(score), 'red'))
        return 0
    print('Overall Sentiment: score of {} '.format(score))
    return 0


def analyze(movie_review_filename):
    client = language.LanguageServiceClient()
    
    with open(movie_review_filename, 'r') as review_file:
        # Instantiates a plain text document.
        content = review_file.read()
            # print(content)
    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    # Print the results
    print_result(annotations)

print('Line 0 is debug, Line 1 is sample Twitter, 2 is Hacker News, 3 is Google Search, and 4 is CNN')
searchTerm = input('What would you like to search?')
#debug
print("DEBUG: ")
try:
    f = open("data.txt", 'w')
    f.write("Awesome spectacular amazing incredible I love life")
finally:
    f.close()
analyze('data.txt')
os.remove('data.txt')
#Twitter
print("TWITTER: ")
try:
    f = open("data.txt", 'w')
    #have to make tApi return cast as a string so we can write it

    tweets = tApi.home_timeline()
    for tweet in tweets:
        f.write(tweet.text)

finally:
    f.close()
analyze('data.txt')
os.remove('data.txt')
#HN
print("HACKER NEWS: ")
try:
    f = open("data.txt", 'w')
    for story_id in hn.top_stories(limit=10):
        f.write(str(hn.get_item(story_id)))
finally:
    f.close()
analyze('data.txt')
os.remove('data.txt')
#Google Search
print("GOOGLE SEARCH FOR {}".format(searchTerm))
try:
    f = open("data.txt", 'w')
    results = search(searchTerm)
    f.write((str(results)))

finally:
    f.close()
analyze('data.txt')
os.remove('data.txt')
#CNN
print("TOP CNN ARTICLES:")
try:
    f = open("data.txt", 'w')
    results = news(3)
    f.write(str(results.get()))

finally:
    f.close()
analyze('data.txt')
os.remove('data.txt')

