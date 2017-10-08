from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

from sentimentNews import news

from six import binary_type
from six.moves import input

# Unformatted text
def analyze_text(text):
    client = language.LanguageServiceClient()

    # print(text.encode('utf-8').strip())
    if isinstance(text, binary_type):
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

def query(searchTerm):
	args = list([])
	results = news(3, searchTerm, args)
	while(not results.empty()):
		analyze_text(results.get())

searchTerm = "trump"
query(searchTerm)

