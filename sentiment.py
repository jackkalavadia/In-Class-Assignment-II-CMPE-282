import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    sentiment = SentimentIntensityAnalyzer().polarity_scores(text)
    if sentiment['compound'] >= 0.05:
        return 'Positive'
    elif sentiment['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def get_sentiment_scores(text):
    sentiment = SentimentIntensityAnalyzer().polarity_scores(text)
    return sentiment

def analyze_multiple_sentiments(text_list):
    sentiment_list = []
    for text in text_list:
        sentiment = analyze_sentiment(text)
        sentiment_list.append((text, sentiment))
    return sentiment_list

text = input("Enter a text string: ")
sentiment = analyze_sentiment(text)
print("Sentiment: ", sentiment)

text_list = [
    "I love this product!",
    "This product is okay, but nothing special.",
    "I hate this product."
]

multiple_sentiments = analyze_multiple_sentiments(text_list)
print("Sentiments: ", multiple_sentiments)
