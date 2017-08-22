import unittest
import os.path
from ScraperStrategies.SimpleReviewScraper import SimpleReviewScraper
from ScraperStrategies.HtmlRetrievers.MockHtmlRetriever import MockHtmlRetriever
from ReviewObjects.ReviewPrinter import ReviewPrinter

class TestReviewPrinterMethods(unittest.TestCase):

    def setUp(self):
        self.review_scraper = SimpleReviewScraper(html_retriever=MockHtmlRetriever())
        self.review_printer = ReviewPrinter()
        self.setup_review_list()
        self.setup_test_files()
        return

    def setup_review_list(self):
        self.review_list = self.review_scraper.scrape_reviews_from_page("UnitTest/MockHtml/MockHtml", "review-content", 5, "")
        return

    def setup_test_files(self):
        self.test_files = [
            ('//MockReportOutput/OutputTest1', 1),
            ('//MockReportOutput/OutputTest2', 4),
            ('//MockReportOutput/OutputTest3', 40),
            ('//MockReportOutput/OutputTestBlank', 0)
        ]

    def test_get_formatted_reviews(self):
        for test_file in self.test_files:
            test_file_name = test_file[0]
            num_reviews_to_print = test_file[1]
            actual_val = self.review_printer.get_formatted_reviews(self.review_list, num_reviews_to_print).strip()
            expected_val = self.get_string_from_test_file(test_file_name).strip()

            self.assertTrue(actual_val == expected_val)

    def get_string_from_test_file(self, file_name):
        basepath = os.path.dirname(__file__)
        filepath = basepath + file_name
        f = open(filepath, "r")
        file_string = f.read()
        f.close()
        return file_string

