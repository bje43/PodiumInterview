import abc


class ReviewScraperBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def scrape_reviews_from_page(self, web_url, class_target, num_pages_to_scrape, number_of_crawlers):
        """Retrieve reviews tagged with the given target from the passed in website """
        return

    @staticmethod
    def get_next_page_url(base_url, curr_page):
        return base_url + "page" + str(curr_page + 1)
