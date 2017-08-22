import unittest
from ScraperStrategies.HtmlRetrievers.MockHtmlRetriever import MockHtmlRetriever
from ScraperStrategies.SimpleReviewScraper import SimpleReviewScraper

class TestSimpleReviewScraperMethods(unittest.TestCase):

    def setUp(self):
        self.review_scraper = SimpleReviewScraper(html_retriever=MockHtmlRetriever())
        return

    def test_scrape_reviews_from_page(self):
        review_list = self.review_scraper.scrape_reviews_from_page("UnitTest/MockHtml/MockHtml", "review-content", 5, "")
        self.assertTrue(len(review_list) == 40)