"""
 This settings for programm
"""

# URL sites for parsing
URL = 'https://www.python.org/blogs/'

# This all tags html for parser
TAGS_HTML = ['h3', 'h1', 'h2', 'li']  # Tags for adding elements for parsing

# This all links classes for parsera
LINKS_CLASS = ['event-title', 'call-to-action', 'widget-title', 'tier-1 element-1'] # Classes for adding elements for parsing

# HEADERS for parsing
HEADER = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; \
            rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}


# if SAVE_FILES = False, maximum record in file "save"  == 10.
SAVE_FILE = True