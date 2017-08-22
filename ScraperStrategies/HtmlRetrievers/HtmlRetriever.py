import requests
from bs4 import BeautifulSoup
from ScraperStrategies.HtmlRetrievers.HtmlRetrieverBase import HtmlRetrieverBase


class HtmlRetriever(HtmlRetrieverBase):

    def retrieve_page_content(self, web_url):
        try:
            page = requests.get(web_url)
            page_content = BeautifulSoup(page.content, 'html.parser')
        except requests.exceptions.RequestException:
            page_content = None

        return page_content
