# Basic Customization

There are many parameters that are easy to use as well as others that require a mentioning.

#### rss_links

The parameter rss_links can be changed for what you want your news to be about.
Feeds can be found here: https://www.nytimes.com/rss

## recipient

If you created a new Google Account, you can have the email recipient be your main email like: ```main.email@other.com```
IMPORTANT: You may not use this feature to send emails to other parties or for commercial use because it breaks the NYTimes Terms of Service.

From the NYTimes:

"We allow the use of NYTimes.com RSS feeds for personal use in a news reader or as part of a non-commercial blog.
We require proper format and attribution whenever New York Times content is posted on your website, and we reserve the right to require that you cease distributing NYTimes.com content.
Please read the Terms and Conditions for complete instructions.
Commercial use of the Service is prohibited without prior written permission from NYT which may be requested via email to: nytlg-sales@nytimes.com."

## Timezone

If your timezone is not ```US/Eastern```, you may change it to a different string that is a valid pytz timezone.
To find them:

```python
import pytz
print(pytz.all_timezones())
```

# Advanced Customization

Advanced customization can be added for your own personal taste.

## style_sheet

The style sheet allows you to change the formatting and style of the email, like in regular HTML.

It is preset as this:

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Verdana, sans-serif;
}

h1 {
    font-size: 15px;
}

p, div {
    font-size: 12px;
}
```

## story_html_template

There are two templates for each story, one for ones with images and one for ones without images.

```html
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
```

```html
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
```

Note that the brackets are placeholders for the ```.format()``` function that is handled by the internal method. All of those parameters must be included, and no more can be added.

## main_html_template

Similar to the images, this is a template for the entire email.
The default is set to this:

```html
<!DOCTYPE html>
<html>
    <head>
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
```

The parameter ```html_body``` is what the stories are, each with their own paragraph headers.