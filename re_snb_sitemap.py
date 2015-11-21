__author__ = 'sujay'

from sitemap_builder.url_set_builder import UrlSetBuilder
from sitemap_builder.site_map_builder import SiteMapBuilder
from sitemap_builder.site_map import SiteMap
from sitemap_builder.url import Url
import datetime
import math
from os import listdir
from os.path import isfile, join

import json
import io
#base_re_url = "{{env('APP_URL')}}"

base_re_url = "http://www.quikr.com"
base_re_snb_url = '/homes/property/'
base_file_name = 'sitemap_snb_urlset'
site_maps_folder = 'sitemaps/'

def generate_urlset():

    page_size = 40000

    with open('/Users/quikr/tmp/sitemap_urls.json') as sitemap:
        json_sitemap = json.load(sitemap)
        total_count = len(json_sitemap)
        pages = int(math.ceil(total_count / page_size))
        next_page = 1
        for page in range(0, pages):
            start = page * page_size
            paged_json_sitemap = json_sitemap[start: next_page * page_size]
            print "Page %d, %d" % (next_page, len(paged_json_sitemap))
            generate_paged_urlset(paged_json_sitemap, next_page)
            next_page += 1


def generate_paged_urlset(json_sitemap, page):

    snb_url_page = site_maps_folder + '/' + base_file_name + '_' + str(page) + '.blade.php'
    url_set_builder = UrlSetBuilder('http://www.sitemaps.org/schemas/sitemap/0.9')
    snb_base_url = base_re_url + base_re_snb_url
    for url in json_sitemap:
        url_set_builder.url(Url(snb_base_url + url, datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"), 'daily'))

    with io.open(snb_url_page, 'w', encoding='utf-8') as f:
        f.write(unicode(url_set_builder.build(prettify=True)))

def generate_snb_sitemap():
    sitemap_file_name = 'snb_sitemap.blade.php'
    sitemaps = [f for f in listdir(site_maps_folder) if isfile(join(site_maps_folder, f)) and f.endswith('.php')]
    site_map_builder = SiteMapBuilder('http://www.sitemaps.org/schemas/sitemap/0.9')
    for sitemap in sitemaps:
        sitemap_url = base_re_url + '/' + sitemap
        site_map_builder.site_map(SiteMap(sitemap_url))
    with io.open(sitemap_file_name, 'w', encoding='utf-8') as f:
        f.write(unicode(site_map_builder.build(prettify=True)))


if __name__ == '__main__':
    generate_urlset()
    generate_snb_sitemap()

