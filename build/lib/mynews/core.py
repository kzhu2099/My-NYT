import re
import requests

from urllib.parse import urljoin, urlparse
import xml.etree.ElementTree as ET

def is_valid_rss(url):
    try:
        html = requests.get(url).text
        xml_data = ET.fromstring(html)
        return True

    except Exception:
        return False

def extract_links(html, base_url):
    links = re.findall(r'href=["\'](.*?)["\']', html)
    internal_links = []

    for link in links:
        full_link = urljoin(base_url, link) if link.startswith('/') else link
        if base_url in full_link and full_link not in internal_links:
            if not full_link.endswith('index.html'):
                internal_links.append(full_link)

    return internal_links

def find_rss_feeds(website_url, depth = None, max_rss_feeds = None):
    to_visit = [website_url]
    visited = set()
    rss_feeds = []
    valid_feeds = []
    current_depth = 0

    while True:
        if not to_visit:
            break

        for url in rss_feeds:
            if url not in valid_feeds and is_valid_rss(url):
                valid_feeds.append(url)

        if max_rss_feeds is not None and len(valid_feeds) >= max_rss_feeds:
            break

        if depth is not None and current_depth >= depth:
            break

        next_round = []

        for current_url in to_visit:
            if current_url in visited:
                continue

            visited.add(current_url)

            try:
                response = requests.get(current_url)
                html = response.text
            except requests.RequestException:
                continue

            found_feeds = re.findall(r'<link[^>]+type=["\']application/rss\+xml["\'][^>]+href=["\']([^"\']+)["\']', html)
            for feed in found_feeds:
                full_feed = feed if feed.startswith('http') else urljoin(website_url, feed)
                if full_feed not in rss_feeds:
                    rss_feeds.append(full_feed)

            internal_links = extract_links(html, website_url)
            for link in internal_links:
                if link not in visited and link not in next_round:
                    next_round.append(link)

        to_visit = next_round
        current_depth += 1

    if  max_rss_feeds is not None and len(valid_feeds) > max_rss_feeds:
        valid_feeds = valid_feeds[:max_rss_feeds]

    return valid_feeds

def get_rss_data(url):
    if is_valid_rss(url):
        html = requests.get(url).text
        return ET.fromstring(html)

    else:
        return None

def parse_rss_data(xml_data):
    if xml_data is None:
        return []

    items = []
    for item in xml_data.findall('.//item'):
        title = item.find('title').text if item.find('title') is not None else 'No title'
        link = item.find('link').text if item.find('link') is not None else 'No link'
        pub_date = item.find('pubDate').text if item.find('pubDate') is not None else 'No date'
        items.append({'title': title, 'link': link, 'pub_date': pub_date})

    return items