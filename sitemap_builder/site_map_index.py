__author__ = 'sujay'

class SiteMapIndex:

    def __init__(self, xmlns, site_maps=None):
        if site_maps is None:
            self.__site_maps = []
        else:
            self.__site_maps = site_maps
        self.xmlns = xmlns
        self.tag_name = 'sitemapindex'

    @property
    def tag_name(self):
        return self.__tag_name

    @property
    def site_maps(self):
        return self.__site_maps

    @property
    def xmlns(self):
        return self.__xmlns

    @site_maps.setter
    def site_maps(self, site_maps):
        self.__site_maps = site_maps

    def add(self, site_map):
        self.__site_maps.append(site_map)
