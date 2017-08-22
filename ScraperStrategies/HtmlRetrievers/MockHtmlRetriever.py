from ScraperStrategies.HtmlRetrievers.HtmlRetrieverBase import HtmlRetrieverBase
from bs4 import BeautifulSoup
import os.path

class MockHtmlRetriever(HtmlRetrieverBase):

    def retrieve_page_content(self, file_name):
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, "..", "..", file_name))
        if os.path.isfile(filepath):
            f = open(filepath, "r")
            fake_html = f.read()
            f.close()
            return BeautifulSoup(fake_html, "html.parser")
        else:
            return None