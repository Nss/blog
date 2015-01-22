#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Luca Lanziani'
SITENAME = u'Luca Lanziani'
SITEURL = 'http://127.0.0.1:8000'

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "./pelican-themes/pure"

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['gravatar', 'series', 'sitemap', 'related_posts', 'neighbors',
           'liquid_tags.img', 'liquid_tags.video', 'liquid_tags.youtube',
           'liquid_tags.vimeo', 'liquid_tags.include_code',
           'liquid_tags.notebook', 'pelican_gist']

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/Nss'),
          ('twitter', 'http://twitter.com/_Nss_'),
          ('linkedin', 'http://uk.linkedin.com/in/lucalanziani/'),
          ('envelope', 'mailto:luca.lanziani+site@gmail.com'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

PROFILE_IMG_URL = SITEURL + '/images/minime.jpg'
COVER_IMG_URL = SITEURL + '/images/london.jpg'
USER_LOGO_URL = SITEURL + '/images/minime.jpg'

TAGLINE = ('Software engineer, linux addict, '
           'hacker as http://bit.ly/hacker_def, '
           'InnovAction Lab alumnus')

TAGLINE_HTML = ('Software engineer, linux addict, '
                'hacker as <a href="http://bit.ly/hacker_def">'
                'hacker_def</a>, '
                '<a href="http://www.innovactionlab.org/">InnovAction Lab</a> '
                'alumnus')

