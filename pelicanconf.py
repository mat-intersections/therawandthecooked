#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys
sys.path.append('.')
import jinja_filters

AUTHOR = 'Tom Gurion'
SITENAME = 'The RAW and The COOKED'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'GMT'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'theme'
ARTICLE_ORDER_BY = 'date'
SLUGIFY_SOURCE = 'basename'
JINJA_FILTERS = {
    'event_time': jinja_filters.event_time,
    'strip_paragraph': jinja_filters.strip_paragraph,
}
DESCRIPTION = 'A two day ‘happening’ of new approaches to musical creation and creativity hosted by the Media & Arts Technology Centre for Doctoral Training at Queen Mary University of London.'
