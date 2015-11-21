__author__ = 'sujay'

from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement

from site_map_index import SiteMapIndex
import xml.dom.minidom

class SiteMapBuilder:

    def __init__(self, xmlns):
        self.__site_map_index = SiteMapIndex(xmlns)

    def site_map(self, site_map):
        self.__site_map_index.add(site_map)
        return self

    def build(self, prettify=False):
        site_map_index_elem = Element(self.__site_map_index.tag_name, xmlns=self.__site_map_index.xmlns)
        for site_map in self.__site_map_index.site_maps:
            site_map_elem = SubElement(site_map_index_elem, site_map.tagname)
            site_map_loc_elem = SubElement(site_map_elem, 'loc').text = site_map.loc
        xml_str = ElementTree.tostring(site_map_index_elem, 'utf-8')
        if prettify:
            reparsed = xml.dom.minidom.parseString(xml_str)
            return reparsed.toprettyxml(indent="\t")
        else:
            return xml_str
