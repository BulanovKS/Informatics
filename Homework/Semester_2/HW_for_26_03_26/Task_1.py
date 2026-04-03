import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
from collections import deque
import json
from urllib.parse import urljoin
import time

import networkx as nx

#Вспомогательные функции
BASE = "https://ru.wikipedia.org"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (SeminarScraper/1.0; +https://example.org/)",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "ru,en;q=0.8",
}

def article_to_url(title: str) -> str:
    return f"{BASE}/wiki/{title.replace(' ', '_')}"

def is_valid_article_href(href: str) -> bool:
    if not href.startswith("/wiki/"):
        return False

    title = href[len("/wiki/"):]

    if not title:
        return False
    if "#" in title:
        return False
    if ":" in title:
        return False
    if title.startswith("Заглавная_страница"):
        return False

    return True

def href_to_title(href: str) -> str:
    return unquote(href[len("/wiki/"):]).replace("_", " ")

def extract_article_links(article_title: str, max_links: int = 30):
    url = article_to_url(article_title)
    resp = requests.get(url, headers=HEADERS, timeout=20)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "lxml")
    content = soup.find("div", id="mw-content-text")
    if content is None:
        return []

    links = []
    seen = set()

    for a in content.find_all("a", href=True):
        href = a["href"]

        if not is_valid_article_href(href):
            continue

        target_title = href_to_title(href)

        if target_title == article_title:
            continue
        if target_title in seen:
            continue

        seen.add(target_title)
        links.append(target_title)

        if len(links) >= max_links:
            break

    return links

def build_wikipedia_graph(start_title: str, depth: int = 1, max_links_per_page: int = 20, sleep_sec: float = 0.3, goal: str = "Математика"):
    G = nx.DiGraph()
    visited = set()
    queue = deque([(start_title, 0)])

    while queue:
        current_title, current_depth = queue.popleft()

        if current_title in visited:
            continue
        visited.add(current_title)

        try:
            neighbors = extract_article_links(current_title, max_links=max_links_per_page)
        except Exception as e:
            print(f"Ошибка при обработке статьи '{current_title}': {e}")
            continue

        for nb in neighbors:
            G.add_edge(current_title, nb)

            if current_depth < depth:
                queue.append((nb, current_depth + 1))

        for _ in range(len(queue)):
            #print(queue[_][0])
            if goal == queue[_][0]:
                return queue[_][1]
            else:
               depth += 1

        time.sleep(sleep_sec)

    return G

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
    title = soup.find("title").text[:-12]

    return title

first_url = "https://ru.wikipedia.org/api/rest_v1/page/random/summary"

url = first_step(HEADERS, first_url)

START_ARTICLE = chain(HEADERS, url)
print(START_ARTICLE)
GOAL = "Английский язык"

G = build_wikipedia_graph(
    start_title=START_ARTICLE,
    depth=1,
    max_links_per_page=15,
    sleep_sec=0.2,
    goal=GOAL
)

#with open("latin.txt", "a", encoding="utf_8") as file:
#    file.write(START_ARTICLE + " " + str(G) + "\n")

with open("english.txt", "a", encoding="utf_8") as file:
    file.write(START_ARTICLE + " " + str(G) + "\n")