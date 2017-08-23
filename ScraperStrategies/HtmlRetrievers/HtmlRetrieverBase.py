import abc


class HtmlRetrieverBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def retrieve_page_content(self, web_url):
        """Return the content of the given web_url"""
        return
