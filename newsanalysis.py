from all_imports import *


def get_sentiment_score(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    return sentiment_score


def sentiment_score(title, description):

    sentiment_score_title = get_sentiment_score(title)
    sentiment_score_para = get_sentiment_score(description)
    sentiment_score_overall = (sentiment_score_title + sentiment_score_para) / 2

    def categorize_sentiment(score):
        if score > 0:
            return 'Positive'
        elif score < 0:
            return 'Negative'
        else:
            return 'Neutral'

    sentiment_title = categorize_sentiment(sentiment_score_title)
    sentiment_para = categorize_sentiment(sentiment_score_para)
    sentiment_overall = categorize_sentiment(sentiment_score_overall)

    return round(sentiment_score_title, 2), round(sentiment_score_para, 2), round(sentiment_score_overall, 2), sentiment_title, sentiment_para, sentiment_overall
