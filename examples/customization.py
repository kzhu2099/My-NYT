from mynyt import MyNYT

new_style_sheet = '''\
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Times, serif;
}

h1 {
    font-size: 18px;
}

p, div {
    font-size: 14px;
}
'''

news = MyNYT(
    'your.email@gmail.com',
    'your appp pass word',
    rss_links = [
        'https://rss.nytimes.com/services/xml/rss/nyt/World.xml',
        'https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml',
        'https://rss.nytimes.com/services/xml/rss/nyt/Sports.xml'
    ],
    style_sheet = new_style_sheet
)

news.get_all_stories(
    rotate_through_feeds = True
)

news.remove_duplicates()

news.trim_to_length(
    length = 12
)

new_image_story_html_template = '''\
<div style = 'display: flex; width: 100%; padding: 10px;'>
<div style = 'width: 80%; margin-right: 20px;'>
    <h3><a href='{link}'>{title}</a></h3>
    <p><br>
    {description}<br><br>
    {authors}<br>
    </p>
</div>
<div style = 'width: 20%;'>
    <img src = '{article_image_link}' alt = 'HTML Image' width = '100%'>
</div>
</div>
<hr style = 'margin-left: 10px; margin-right: 10px; width: calc(100% - 20px);'>
'''

news.convert_news_to_html(
    image_story_html_template = new_image_story_html_template,
)

news.send_email(
    recipient = 'your.email@gmail.com',
    main_subject = 'The Trifecta',
    timezone = 'US/Central',
    main_html_template = None,
)