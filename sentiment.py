import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

def sentiment_analysis(text):
    sentiment = SentimentIntensityAnalyzer().polarity_scores(text)
    if sentiment['compound'] >= 0.05:
        return 'Positive'
    elif sentiment['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Test cases
test_texts = [
    'This is an amazing product!',
    'I hate this product',
    'This product is just okay',
]
for text in test_texts:
    print(f'{text}: {sentiment_analysis(text)}')
