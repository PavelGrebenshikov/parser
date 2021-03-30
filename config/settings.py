"""
 This settings for programm
"""

# URL sites for parsing
URL = 'https://www.newsru.com/'

# This all tags html for parser
TAGS_HTML = ['h3', 'div']

# This all links classes for parsera
LINKS_CLASS = ['event-title', 'event-warp']

# HEADERS for parsing
HEADER = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; \
            rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}