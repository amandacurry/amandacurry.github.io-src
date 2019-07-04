#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Amanda Cercas Curry'
SITENAME = 'Amanda Cercas Curry'
SITEURL = ''

THEME = "Flex"
STATIC_PATHS = ['img', 'static']
CUSTOM_CSS = 'static/custom.css'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

LOAD_CONTENT_CACHE = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DELETE_OUTPUT_DIRECTORY = False
SHOW_ARTICLE_AUTHOR = True

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('About', '/index.html'),
    ('Publications', '/pages/publications.html'),
    ('Vita', '/pdfs/HouserCV.pdf'),)

'''
 # Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),) 
'''

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
SOCIAL = (('linkedin', 'https://br.linkedin.com/in/test'),
          ('github', 'https://github.com/test'),
          ('twitter', 'https://twitter.com/test'))