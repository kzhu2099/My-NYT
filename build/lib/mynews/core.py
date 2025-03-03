import smtplib

import feedparser
import requests

class MyNews:
    def __init__(self, rss_sources = None):
        self.rss_sources = rss_sources or [
            'https://news.google.com/rss',
            'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
        ]

    def get_news(self):
        news_items = []

        for rss_source in self.rss_sources:
            feed = feedparser.parse(rss_source)

            for entry in feed.entries:
                news_items.append({
                    'title': entry.title,
                    'summary': entry.summary,
                    'link': entry.link,
                    'published': entry.published
                })

        return news_items

    def to_html(self):
        pass