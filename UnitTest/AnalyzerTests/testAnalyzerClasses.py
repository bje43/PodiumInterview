import unittest
from ReviewAnalysisStrategies.NaiveBayesReviewAnalyzer import NaiveBayesReviewAnalyzer
from ReviewAnalysisStrategies.PatternReviewAnalyzer import PatternReviewAnalyzer
from ReviewObjects.Review import Review


class TestNaiveBayesAnalyzerMethods(unittest.TestCase):

    def setUp(self):
        self.setup_test_case_dict()
        self.setup_analyzers()

    def setup_test_case_dict(self):

        self.test_case_dict = {
            "This is a terrible sentence": [0.206725642747127, -1.0],
            "This is a great sentence": [0.5537884560899597, 0.8],
            "12345": [0.5, 0.0],
            "": [.5, 0.0]
        }

    def setup_analyzers(self):
        self.analyzers = []
        self.analyzers.append(NaiveBayesReviewAnalyzer())
        self.analyzers.append(PatternReviewAnalyzer())

    def test_get_review_score_gen(self):

        for i in range(len(self.analyzers)):
            analyzer = self.analyzers[i]
            self.get_review_score_specific(analyzer,i)

    def get_review_score_specific(self, analyzer, index):
        for case in self.test_case_dict:
            assumed_score = self.test_case_dict[case][index]
            actual_score = analyzer.get_review_score(case)
            self.assertTrue(assumed_score == actual_score)

    def test_analyze_reviews(self):
        analyzer = self.analyzers[0]
        review_list = analyzer.analyze_reviews([])
        self.assertTrue(review_list == [])

        for i in range(len(self.analyzers)):
            review_list = self.make_reviews_from_score_dict()
            analyzer = self.analyzers[i]
            analyzed_reviews = analyzer.analyze_reviews(review_list)
            self.verify_analyzed_review_scores(analyzed_reviews,i)

        review_list = []
        for case in self.test_case_dict:
            review = Review(case, 0)
            review_list.append(review)

    def make_reviews_from_score_dict(self):
        review_list = []
        for case in self.test_case_dict:
            review = Review(case, 0)
            review_list.append(review)
        return review_list

    def verify_analyzed_review_scores(self, analyzed_reviews, index):
        prev_score = float('inf')
        for review in analyzed_reviews:
            actual_score = review.positivity_score
            assumed_score = self.test_case_dict[review.review_text][index]

            self.assertTrue(actual_score == assumed_score)
            self.assertTrue(prev_score >= actual_score)

            prev_score = actual_score















