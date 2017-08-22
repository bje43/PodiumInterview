import unittest
from unittest.mock import patch
from ReviewAnalyzerEngine import ReviewAnalyzerEngine
from ReviewAnalysisStrategies.PatternReviewAnalyzer import PatternReviewAnalyzer
from ReviewAnalysisStrategies.NaiveBayesReviewAnalyzer import NaiveBayesReviewAnalyzer
from ScraperStrategies.ScrapyReviewScraper import ScrapyReviewScraper
from ScraperStrategies.SimpleReviewScraper import SimpleReviewScraper

class testReviewAnalyzerEngineMethods(unittest.TestCase):

    def setUp(self):
        self.engine = ReviewAnalyzerEngine()
        self.engine.review_scraper = ScrapyReviewScraper()

    def test_int_getting_methods(self):
        methods = [
            'get_number_of_crawlers_from_prompt',
            'get_number_of_pages_to_scrape_from_prompt',
            'get_number_of_reviews_to_display_from_prompt'
        ]

        test_options = ["-1", "0", "b", "a", "", "1", "2"]
        valid_responses = [1, 2]

        for method_name in methods:
            method = getattr(self.engine, method_name)
            self.get_pos_int_from_promt_test(method, test_options, valid_responses)

    def get_pos_int_from_promt_test(self, method, test_options, valid_responses):
        with patch('builtins.input', side_effect=test_options):
            for val in valid_responses:
                result = method()
                self.assertTrue(val == result)

    def test_get_review_analyzer_from_prompt(self):
        method = self.engine.get_review_analyzer_from_prompt
        test_options = ["-1", "0", "b", "a", "", "1", "2"]
        valid_response_types = [PatternReviewAnalyzer, NaiveBayesReviewAnalyzer]

        self.get_valid_dict_option_from_prompt_test(method, test_options, valid_response_types)

    def test_get_review_scraper_from_prompt(self):
        method = self.engine.get_review_scraper_from_prompt
        test_options = ["-1", "0", "b", "a", "", "1", "2"]
        valid_response_types = [SimpleReviewScraper, ScrapyReviewScraper]

        self.get_valid_dict_option_from_prompt_test(method, test_options, valid_response_types)

    def get_valid_dict_option_from_prompt_test(self, method, test_options, valid_response_type):
        with patch('builtins.input', side_effect=test_options):
            for type in valid_response_type:
                result = method()
                self.assertTrue(isinstance(result, type))
