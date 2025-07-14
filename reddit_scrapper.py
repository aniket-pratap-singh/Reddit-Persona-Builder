import requests
from bs4 import BeautifulSoup
import re

def extract_username(profile_url):
    match = re.search(r'reddit\.com\/user\/([^\/]+)', profile_url)
    return match.group(1) if match else None

def fetch_user_data(username, limit=10):
    url = f"https://old.reddit.com/user/{username}/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch profile page: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    entries = soup.find_all('div', class_='thing', limit=limit)
    data = []

    for entry in entries:
        title = entry.find('a', class_='title')
        body = entry.find('div', class_='md')
        subreddit = entry.get('data-subreddit')
        url = entry.get('data-permalink')

        post_data = {
            'type': 'post' if title else 'comment',
            'title': title.text.strip() if title else None,
            'body': body.text.strip() if body else None,
            'subreddit': subreddit,
            'url': f"https://reddit.com{url}" if url else None
        }

        data.append(post_data)

    return data

