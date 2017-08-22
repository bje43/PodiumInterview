from ReviewAnalysisStrategies.NaiveBayesReviewAnalyzer import NaiveBayesReviewAnalyzer
from ReviewAnalysisStrategies.PatternReviewAnalyzer import PatternReviewAnalyzer
from ReviewObjects.ReviewPrinter import ReviewPrinter
from ScraperStrategies.HtmlRetrievers.HtmlRetriever import HtmlRetriever
from ScraperStrategies.ScrapyReviewScraper import ScrapyReviewScraper
from ScraperStrategies.SimpleReviewScraper import SimpleReviewScraper


class ReviewAnalyzerEngine(object):

    def get_user_input(self):
        self.review_analyzer = self.get_review_analyzer_from_prompt()
        self.review_scraper = self.get_review_scraper_from_prompt()
        self.number_of_crawlers = self.get_number_of_crawlers_from_prompt()
        self.number_of_pages_to_scrape = self.get_number_of_pages_to_scrape_from_prompt()
        self.number_of_reviews_to_display = self.get_number_of_reviews_to_display_from_prompt()
        self.is_initialized = 1
        return

    def set_engine_attributes(self,review_analyzer, review_scraper, number_of_crawlers, number_of_page_to_scrape, number_of_reviews_to_display):
        self.review_analyzer = review_analyzer
        self.review_scraper = review_scraper
        self.number_of_crawlers = number_of_crawlers
        self.number_of_pages_to_scrape = number_of_page_to_scrape
        self.number_of_reviews_to_display = number_of_reviews_to_display
        self.is_initialized = 1
        return

    def get_review_analyzer_from_prompt(self):
        valid_options = {"1":PatternReviewAnalyzer(),"2":NaiveBayesReviewAnalyzer()}
        prompt = """Please enter the number of the type of analyzer you would like to use to score review positivity:\n
                        1. Basic Pattern Analyzer\n
                        2. Naive Bayes Analyzer\n"""
        return self.get_valid_dict_option_from_prompt(prompt, valid_options)

    def get_review_scraper_from_prompt(self):
        valid_options = {"1": SimpleReviewScraper(html_retriever=HtmlRetriever()),"2": ScrapyReviewScraper()}
        prompt =  """Please enter the number of the type of scraper you would like to use to scrape review from the web:\n
                        1. Simple Web Scaper\n
                        2. Scrapy Web Scraper\n"""
        return self.get_valid_dict_option_from_prompt(prompt, valid_options)

    def get_valid_dict_option_from_prompt(self, prompt, option_dict):
        option = ""
        while option not in option_dict:
            option = input(prompt)
        return option_dict[option]

    def get_number_of_crawlers_from_prompt(self):
        number_of_crawlers = 1
        if isinstance(self.review_scraper,ScrapyReviewScraper):
            number_of_crawlers = self.get_pos_int_from_prompt("Please enter the number of crawlers you would like to use:\n")
        return number_of_crawlers

    def get_number_of_pages_to_scrape_from_prompt(self):
        return self.get_pos_int_from_prompt("Please enter the number of pages you would like to scrape reviews for:\n")

    def get_number_of_reviews_to_display_from_prompt(self):
        return self.get_pos_int_from_prompt("Please enter the number of reviews you would like to display:\n")

    def get_pos_int_from_prompt(self, prompt):
        num = 0
        while not isinstance(num, int) or num <= 0:
            num = input(prompt)
            if num.isdigit(): num = int(num)
        return num

    def run(self):

        if not self.is_initialized: self.get_user_input()

        website = "http://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/"
        target = "review-content"
        review_list = self.review_scraper.scrape_reviews_from_page(website, target, self.number_of_pages_to_scrape, self.number_of_crawlers)

        review_list = self.review_analyzer.analyze_reviews(review_list)

        review_printer = ReviewPrinter()
        review_printer.print_review_list(review_list,self.number_of_reviews_to_display)

        return review_list


if __name__=="__main__":
    review_analyzer_engine = ReviewAnalyzerEngine()
    review_analyzer_engine.run()


