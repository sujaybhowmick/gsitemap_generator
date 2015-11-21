__author__ = 'sujay'

class UrlSet:
    def __init__(self, xmlns, urls=None):
        if urls is None:
            self.urls = []
        else:
            self.urls = urls
        self.xmlns = xmlns
        self.tag_name = 'urlset'

    @property
    def urls(self):
        return self.__urls

    @property
    def xmlns(self):
        return self.__xmlns

    @property
    def tag_name(self):
        return self.__tag_name

    @urls.setter
    def urls(self, urls):
        self.__urls = urls

    def add(self, url):
        self.urls.append(url)
