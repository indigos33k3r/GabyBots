from __future__ import absolute_import

# Setup of environment for Scrapy script #
##########################################

# Insure the project root is in the python path using this file as a reference
import os
import sys
from os.path import abspath, dirname, join
PROJECT_ROOT = abspath(join(dirname(__file__), '..', '..', '..'))
sys.path.extend([PROJECT_ROOT])

import settings
from django.core.management import setup_environ
setup_environ(settings)

assert PROJECT_ROOT == settings.PROJECT_ROOT
os.chdir(PROJECT_ROOT)

##########################################
# Scrapy settings for scraping.news project
#
# All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'scraping'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['dynamic_scraper.spiders', 'gbots.scraping.news.spiders']
NEWSPIDER_MODULE = 'gbots.scraping.news.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
    'dynamic_scraper.pipelines.ValidationPipeline',
    'gbots.scraping.news.pipelines.DjangoWriterPipeline',
]

