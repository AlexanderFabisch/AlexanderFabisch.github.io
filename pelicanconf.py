#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alexander Fabisch'
SITENAME = u'Alexander Fabisch'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'pelican-themes/bootstrap2'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video', 'liquid_tags.include_code',
           'liquid_tags.notebook', 'liquid_tags.literal']
EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('DFKI', 'http://robotik.dfki-bremen.de/en/about-us/staff/alfa02.html'),
          ('Scholar', 'http://scholar.google.de/citations?user=HhlbbxMAAAAJ'),
          ('Github', 'https://github.com/AlexanderFabisch'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
