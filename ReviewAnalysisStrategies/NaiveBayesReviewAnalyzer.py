from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
from ReviewAnalysisStrategies.ReviewAnalyzerBase import ReviewAnalyzerBase


class NaiveBayesReviewAnalyzer(ReviewAnalyzerBase):

    def __init__(self):
        self.classifier = Blobber(analyzer=NaiveBayesAnalyzer())

    def get_review_score(self, review_text):
        analysis = self.classifier(str(review_text))
        return analysis.sentiment.p_pos




