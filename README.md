# Utility to generate Google Sitemaps.

```python
	
	from sitemap_builder.url_set_builder import UrlSetBuilder
	from sitemap_builder.site_map_builder import SiteMapBuilder
	from sitemap_builder.site_map import SiteMap
	from sitemap_builder.url import Url
	
	import datetime
	
	if __name__ == '__main__':
		# Generate Url Set
		url_set_builder = UrlSetBuilder('http://www.sitemaps.org/schemas/sitemap/0.9')
		url_set_builder.url(Url("http://www.example.com/somepage.html",
								datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"), 'daily'))
	
		url_set_builder.url(Url("http://www.example.com/about.html",
								datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"), 'daily'))
	
		url_set = url_set_builder.build(prettify=True)
		print url_set
	
		# Generate sitemap index
		site_map_builder = SiteMapBuilder('http://www.sitemaps.org/schemas/sitemap/0.9')
		site_map_builder.site_map(SiteMap('http://www.example.com/sitemap_urlset1.xml'))
		site_map_builder.site_map(SiteMap('http://www.example.com/sitemap_urlset2.xml'))
		sitemap_index = site_map_builder.build(prettify=True)
		print sitemap_index
```