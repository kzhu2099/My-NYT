from mynyt import MyNYT

news = MyNYT(
    'finnyemails@gmail.com',
    'hshx zles yddd nlle',
    [
        'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
        'https://rss.nytimes.com/services/xml/rss/nyt/Science.xml',
        'https://rss.nytimes.com/services/xml/rss/nyt/Business.xml',
        'https://rss.nytimes.com/services/xml/rss/nyt/Sports.xml'
    ]
)
news.get_all_stories()
news.remove_duplicates()
news.trim_to_length(12)
news.convert_news_to_html()
# news.send_email(['finnyinvesting@gmail.com'], timezone = 'US/Central')