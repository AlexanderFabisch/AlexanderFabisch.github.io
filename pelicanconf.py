#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
# https://github.com/danielfrg/pelican-jupyter
from pelican_jupyter import markup as nb_markup

AUTHOR = 'Alexander Fabisch'
SITENAME = 'Alexander Fabisch'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MARKUP = ("md", "ipynb")

THEME="pelican-themes/basic"
PLUGIN_PATHS = ['pelican-plugins']
STATIC_PATHS = ['images', 'downloads']
PLUGINS = [nb_markup]
IPYNB_COLORSCHEME = "staroffice"  # pygments style: https://pygments.org/styles/
IPYNB_MARKUP_USE_FIRST_CELL = False
with open('_nb_header.html', "r") as f:
    EXTRA_HEADER = f.read()
IGNORE_FILES = [".ipynb_checkpoints"]

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
