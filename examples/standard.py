'''
Author: Kevin Zhu
'''

from mynyt import MyNYT

if __name__ == '__main__':
    news = MyNYT(
        'your.email@gmail.com',
        'your appp pass word',
        rss_links = None,
        style_sheet = None
    )

    news.get_all_stories(
        rotate_through_feeds = True
    )

    news.remove_duplicates(
        all_stories = None,
    )

    news.trim_to_length(
        length = 12,
        stories = None
    )

    news.convert_news_to_html(
        stories = None,
        image_story_html_template = None,
        imageless_story_html_template = None,
        main_div_styles = None
    )

    news.send_email(
        recipient = 'your.email@gmail.com',
        main_subject = 'Daily NYT',
        timezone = 'US/Eastern',
        story_html_body = None,
        main_html_template = None
    )