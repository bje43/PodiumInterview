from textblob import TextBlob
from ReviewAnalysisStrategies.ReviewAnalyzerBase import ReviewAnalyzerBase


class PatternReviewAnalyzer(ReviewAnalyzerBase):

    def get_review_score(self,review_text):
        analysis = TextBlob(str(review_text))
        return analysis.sentiment.polarity