from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import json

def first_step(headers, url):
    session = requests.Session()
    session.headers.update(headers)

    response = session.get(url, headers=headers, timeout=20).text
    soup = BeautifulSoup(response, "lxml")

    content = soup.get_text()
    dict = json.loads(content)

    return dict['content_urls']['desktop']['page']

def chain(headers, url):
    session = requests.Session()
    session.headers.update(headers)

    response = session.get(url, headers=headers, timeout=20).text
    soup = BeautifulSoup(response, "lxml")
    title = soup.find("title").text
    content = soup.find("li", id="n-randompage")
    url_output = content.find("a").get("href")

    return title, url_output

headers = {
        "User-Agent": "Mozilla/5.0 (SeminarScraper/1.0; +https://example.org/)",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "ru,en;q=0.8",
    }
first_url = "https://ru.wikipedia.org/api/rest_v1/page/random/summary"
base_url = "https://ru.wikipedia.org"

prev = {}

url = first_step(headers, first_url)

for i in range(2):
    article_title, article_url = chain(headers, url)
    url = urljoin(base_url, article_url)
    prev[article_title] = url

print(prev)