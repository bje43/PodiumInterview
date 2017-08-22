import collections
import scrapy
from scrapy.crawler import CrawlerProcess
from ReviewObjects.Review import Review
from ScraperStrategies.ReviewScraperBase import ReviewScraperBase


class ScrapyReviewScraper(ReviewScraperBase):

    def __init__(self):
        self.urls_to_visit = collections.deque()
        self.review_list = collections.deque()

    def scrape_reviews_from_page(self, web_url, class_target, num_pages_to_scrape, number_of_crawlers):

        self.setup_urls_to_visit(web_url,num_pages_to_scrape)

        self.deploy_crawlers(number_of_crawlers, class_target)

        self.review_list = list(self.review_list)

        return self.review_list

    def deploy_crawlers(self,number_of_crawlers,class_target):
        process = CrawlerProcess()

        for i in range(0, number_of_crawlers):
            process.crawl(ReviewSpider,scraper_parent=self,class_target=class_target)

        process.start()

    def setup_urls_to_visit(self,base_url,num_pages_to_scrape):
        curr_page_num = 0
        while curr_page_num <= num_pages_to_scrape:
            self.urls_to_visit.append(ReviewScraperBase.get_next_page_url(base_url, curr_page_num))
            curr_page_num += 1

    def add_review(self,review_text):
        review = Review(review_text, 0)
        self.review_list.append(review)

    def get_next_page_url(self):
        if len(self.urls_to_visit) == 0:
            return None
        else:
            return self.urls_to_visit.pop()


class ReviewSpider(scrapy.Spider):
    name = 'podiumspider'

    custom_settings = {
        'LOG_LEVEL': 'ERROR',
    }

    def __init__(self, *args, **kwargs):
        super(ReviewSpider, self).__init__(*args, **kwargs)

        self.scraper_parent = kwargs['scraper_parent']
        self.class_target = kwargs['class_target']

        self.set_next_url()

    def set_next_url(self):
        next_url = (self.scraper_parent.get_next_page_url())
        if next_url is not None:
            self.start_urls = [next_url]

    def parse(self, response):
        path = "//*[contains(@class,'" + self.class_target +"')]/text()"
        reviews = response.xpath(path).extract()
        for review_text in reviews:
            self.scraper_parent.add_review(review_text)

        next_page_url = self.scraper_parent.get_next_page_url()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
