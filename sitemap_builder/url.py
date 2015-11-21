__author__ = 'sujay'

class Url:
    def __init__(self, loc, lastmod, changefreq):
        self.loc = loc
        self.lastmod = lastmod
        self.changefreq = changefreq
        self.tag_name = 'url'

    @property
    def loc(self):
        return self.__tag_name

    @property
    def loc(self):
        return self.__loc

    @loc.setter
    def loc(self, loc):
        self.__loc = loc

    @property
    def lastmod(self):
        return self.__lastmod

    @lastmod.setter
    def lastmod(self, lastmod):
        self.__lastmod = lastmod

    @property
    def changefreq(self):
        return self.__changefreq

    @changefreq.setter
    def changefreq(self, changefreq):
        self.__changefreq = changefreq
