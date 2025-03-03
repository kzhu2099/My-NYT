import datetime
import itertools
import smtplib
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import feedparser
import pytz
import requests

class MyNYT:
    def __init__(self, sender_email, sender_email_app_password, rss_links = None, style_sheet = None):
        self.rss_links = rss_links or [
            'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
        ]

        self.style_sheet = style_sheet or '''\
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Verdana, sans-serif;
}

h1 {
    font-size: 15px;
}

h2 {
    font-size: 14px;
}

p, div {
    font-size: 12px;
}
'''

        self.sender_email = sender_email
        self.sender_email_app_password = sender_email_app_password

    def get_all_stories(self):
        feeds = []
        for rss_link in self.rss_links:
            response = requests.get(rss_link)
            feeds.append(feedparser.parse(response.content))

        self.all_stories = []

        for sublist in itertools.zip_longest(*[feed.entries for feed in feeds], fillvalue = None):
            for item in sublist:
                if item:
                    self.all_stories.append(item)

                else:
                    continue

        return self.all_stories

    def remove_duplicates(self):
        titles = []
        initial_stories = self.all_stories[:]
        self.all_stories = []
        for story in initial_stories:
            if story.title not in titles:
                self.all_stories.append(story)
                titles.append(story.title)

        return self.all_stories

    def trim_to_length(self, length):
        if len(self.all_stories) > length:
            self.all_stories = self.all_stories[:length]

        return self.all_stories

    def convert_news_to_html(self, image_story_html_template = None, imageless_story_html_template = None, div_styles = None):
        image_story_html_template = image_story_html_template or '''\
<div style = 'display: flex; width: 100%; padding: 10px;'>
<div style = 'width: 70%; margin-right: 10px;'>
    <h3><a href='{link}'>{title}</a></h3>
    <p><br>
    {description}<br><br>
    {authors}<br>
    </p>
</div>
<div style = 'width: 30%;'>
    <img src = '{article_image_link}' alt = 'HTML Image' width = '100%'>
</div>
</div>
<hr style = 'margin-left: 10px; margin-right: 10px; width: calc(100% - 20px);'>
'''
        imageless_story_html_template = '''\
<div style = 'width: 100%; padding: 10px;'>
    <div>
        <h3><a href='{link}'>{title}</a></h3>
        <p><br>
        {description}<br><br>
        {authors}<br>
        </p>
    </div>
</div>
<hr style = 'margin-left: 10px; margin-right: 10px; width: calc(100% - 20px);'>
'''
        all_html_content = []
        imageless_stories = []
        for story in self.all_stories:
            if 'media_content' in story:
                article_image_link = story.media_content[0]['url']

            else:
                imageless_stories.append(story)
                continue

            title = story.title
            link = story.link
            description = story.description

            authors = story.author if 'author' in story else ''

            story_html = image_story_html_template.format(
                link = link,
                title = title,
                description = description,
                authors = authors,
                article_image_link = article_image_link,
            )

            all_html_content.append(story_html)

        for story in imageless_stories:
            title = story.title
            link = story.link
            description = story.description
            authors = story.author if 'author' in story else ''

            story_html = imageless_story_html_template.format(
                link = link,
                title = title,
                description = description,
                authors = authors,
            )

            all_html_content.append(story_html)

        self.html_body = ''
        div_styles = div_styles or 'width: 100%; height: 100%; max-width: 700px; max-height: 500px; overflow-x: hidden; overflow-y: auto;'
        self.html_body += f'''<div style = '{div_styles}'>'''
        self.html_body += ''.join(all_html_content)
        self.html_body += '</div>'
        return self.html_body

    def send_email(self, recipients, main_subject = 'Daily NYT', timezone = None, html_template = None, html_body = None):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(self.sender_email, self.sender_email_app_password)

            html_body = html_body or self.html_body
            html_template = html_template or '''\
<!DOCTYPE html>
<html>
    <head>
        <link href='https://fonts.googleapis.com/css?family=Montserrat' rel='stylesheet'>
        <style>
            {style_sheet}
        </style>
    </head>
    <body>
        <h1>
            Daily News Summary of the New York Times
        </h1>
        {html_body}
    </body>
</html>
'''

            email = MIMEMultipart('related')
            email['From'] = self.sender_email
            latest_time = datetime.datetime.now(pytz.timezone(timezone or 'US/Eastern'))
            current_date = datetime.datetime.strftime(latest_time, '%b %d, %Y')
            email_time = datetime.datetime.strftime(latest_time, '%I:%M:%S %p %Z')

            full_subject = f'{main_subject} @ {current_date} {email_time}'
            print(f'({full_subject})')

            email['To'] = ', '.join(recipients)
            email['Subject'] = full_subject

            full_html = html_template.format(
                style_sheet = self.style_sheet,
                html_body = html_body
            )

            email.attach(MIMEText(full_html, 'html'))

            server.sendmail(self.sender_email, recipients, email.as_string())

            time.sleep(3)

        finally:
            server.quit()