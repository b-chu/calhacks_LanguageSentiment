from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

from sentimentNews import news

import six

# Unformatted text
def analyze_text(text):
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    # Print the results
    print_result(annotations)

def print_result(annotations):
	score = annotations.document_sentiment.score
	magnitude = annotations.document_sentiment.magnitude

	print('Overall Sentiment: score of {} with magnitude of {}'.format(score, magnitude))
	return 0

def query(searchTerm)
	results.news(3, searchTerm)
	while(not results.empty())
		analyze_text(results.get())

searchTerm = input('What would you like to search?')
query(searchTerm)

