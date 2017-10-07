
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

consumer_key = 'MGDSQ8j3dQYboOittNFGrp4lo'
consumer_secret = 'bVv3gkh3d2PbCbnrQ65DXhhy2uH3XT0c1VXJ29MEuiwDUm27sl'
access_token = '2425664702-MZBjlw7AXstFZuPF0m5lMg4lwUAQwjp67300Z1S'
access_secret = 'ajXytC8FDpvKA5hSeENUwcBw70Yv8VQ0MYHKl4QSMWtwX'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
tApi = tweepy.API(auth)

def print_result(annotations):
    score = annotations.document_sentiment.score
    
    print('Overall Sentiment: score of {} '.format(score))
    return 0

def analyze(movie_review_filename):
    client = language.LanguageServiceClient()
    
    with open(movie_review_filename, 'r') as review_file:
        # Instantiates a plain text document.
        content = review_file.read()

    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    # Print the results
    print_result(annotations)

num = input('Type 1 to sample Twitter, 2 for Google News, or 3 for Reddit')
num = int(num)

if num == 1:
    try:
        f = open("data.txt", 'w')
        #have to make tApi return cast as a string so we can write it
        #sResults = str(tApi.home_timeline())
        tweets = tApi.home_timeline()
        for tweet in tweets:
            f.write(tweet.text)
            print(tweet.text)
    finally:
        f.close()
    analyze('data.txt')





