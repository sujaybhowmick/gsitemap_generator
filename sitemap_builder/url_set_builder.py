__author__ = 'sujay'

from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from url_set import UrlSet
import xml.dom.minidom

class UrlSetBuilder:

    def __init__(self, xmlns):
        self.__url_set = UrlSet(xmlns)

    def url(self, url):
        self.__url_set.add(url)
        return self

    def build(self, prettify=False):
        url_set_elem = Element(self.__url_set.tag_name, xmlns=self.__url_set.xmlns)
        for url in self.__url_set.urls:
            url_elem = SubElement(url_set_elem, url.tag_name)
            url_loc_elem = SubElement(url_elem, 'loc').text = url.loc
            url_lastmod_elem = SubElement(url_elem, 'lastmod').text = url.lastmod
            url_changefreq_elem = SubElement(url_elem, 'changefreq').text = url.changefreq
        xml_str = ElementTree.tostring(url_set_elem, 'utf-8')
        if prettify:
            reparsed = xml.dom.minidom.parseString(xml_str)
            return reparsed.toprettyxml(indent="\t")
        else:
            return xml_str