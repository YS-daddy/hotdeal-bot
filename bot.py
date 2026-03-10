import os
import requests
import xml.etree.ElementTree as ET

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = "1890536088"

RSS_URL = "https://www.fmkorea.com/hotdeal.rss"
STATE_FILE = "last_seen.txt"

KEYWORDS = [
    "아이폰",
    "ssd",
    "그래픽카드",
    "에어팟",
    "닌텐도",
    "특가",
    "핫딜"
]

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message,
            "disable_web_page_preview": True
        },
        timeout=10
    )

def load_last_seen():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return f.read().strip()
    return ""

def save_last_seen(post_id):
    with open(STATE_FILE, "w") as f:
        f.write(post_id)

def fetch_posts():

    r = requests.get(RSS_URL, timeout=10)

    if r.status_code != 200:
        send_telegram(f"⚠️ RSS 접속 실패 {r.status_code}")
        return []

    root = ET.fromstring(r.text)

    posts = []

    for item in root.findall(".//item"):

        title = item.find("title").text
        link = item.find("link").text
        guid = item.find("guid").text

        posts.append({
            "id": guid,
            "title": title,
            "link": link
        })

    return posts

def filter_posts(posts):

    matched = []

    for post in posts:

        title = post["title"].lower()

        for k in KEYWORDS:
            if k.lower() in title:
                matched.append(post)
                break

    return matched

def main():

    posts = fetch_posts()

    if not posts:
        return

    matched = filter_posts(posts)

    if not matched:
        return

    latest = matched[0]

    last_seen = load_last_seen()

    if latest["id"] == last_seen:
        return

    msg = f"🚨 펨코 핫딜\n\n{latest['title']}\n\n{latest['link']}"

    send_telegram(msg)

    save_last_seen(latest["id"])

if __name__ == "__main__":
    main()
