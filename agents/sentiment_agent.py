from textblob import TextBlob

class SentimentAgent:

    def analyze(self, query):

        polarity = TextBlob(query).sentiment.polarity

        if polarity > 0.2:
            return "positive"

        elif polarity < -0.2:
            return "negative"

        return "neutral"
