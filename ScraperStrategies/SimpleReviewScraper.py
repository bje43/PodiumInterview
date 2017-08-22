from ReviewObjects.Review import Review
from ScraperStrategies.ReviewScraperBase import ReviewScraperBase


class SimpleReviewScraper(ReviewScraperBase):

    def __init__(self, **kwargs):
        self.html_retriever = kwargs['html_retriever']

    def scrape_reviews_from_page(self, web_url, class_target, num_pages_to_scrape, number_of_crawlers):
        review_list = []
        curr_page_num = 1
        curr_page_url = web_url
        while curr_page_num <= num_pages_to_scrape:
            page_content = self.html_retriever.retrieve_page_content(curr_page_url)

            if page_content is None: break

            curr_review_list = self.get_reviews_from_page_content(page_content, class_target)
            review_list = review_list + (curr_review_list)
            curr_page_url = self.get_next_page_url(web_url,curr_page_num)
            curr_page_num += 1

        return review_list

    def get_reviews_from_page_content(self, page_content, class_target):
        review_list = page_content.find_all(class_=[class_target])
        for i in range(0, len(review_list)):
            review_text = review_list[i].get_text()
            review_list[i] = Review(review_text, 0)

        return review_list




