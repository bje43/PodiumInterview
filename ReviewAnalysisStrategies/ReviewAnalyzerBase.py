import abc
import bisect

class ReviewAnalyzerBase(object):

    __metaclass__ = abc.ABCMeta

    def analyze_reviews(self, review_list):
        analyzed_reviews = []
        for review in review_list:
            review_score = self.get_review_score(review.review_text)
            review.set_positivity_score(review_score)
            bisect.insort(analyzed_reviews,review)
        return analyzed_reviews

    @abc.abstractmethod
    def get_review_score(self,review_text):
        """Given a review and return the score for that review """
        return