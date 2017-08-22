from ScraperStrategies.HtmlRetrievers.HtmlRetrieverBase import HtmlRetrieverBase
from bs4 import BeautifulSoup
import os.path

class MockHtmlRetriever(HtmlRetrieverBase):

    def retrieve_page_content(self, file_name):
        base_path = os.path.dirname(__file__)
        file_path = os.path.abspath(os.path.join(base_path, "..", "..", file_name))
        if os.path.isfile(file_path):
            f = open(file_path, "r")
            fake_html = f.read()
            f.close()
            return BeautifulSoup(fake_html, "html.parser")
        else:
            return None