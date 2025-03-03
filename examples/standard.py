from mynyt import MyNYT

news = MyNYT(
    'your.email@gmail.com',
    'your appp pass word',
    rss_links = None,
    style_sheet = None
)

news.get_all_stories(
    rotate_through_feeds = True
)

news.remove_duplicates()

news.trim_to_length(
    length = 12
)

news.convert_news_to_html(
    image_story_html_template = None,
    imageless_story_html_template = None,
    main_div_styles = None
)

news.send_email(
    recipient = 'your.email@gmail.com',
    main_subject = 'Daily NYT',
    timezone = 'US/Eastern',
    main_html_template = None,
    story_html_body = None
)