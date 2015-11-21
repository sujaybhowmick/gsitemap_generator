__author__ = 'sujay'

class SiteMap:

    def __init__(self, loc):
        self.loc = loc
        self.tagname = 'sitemap'

    @property
    def loc(self):
        return self.__loc

    @property
    def site_map_tagname(self):
        return self.__site_map_tagname

    @loc.setter
    def loc(self, loc):
        self.__loc = loc
