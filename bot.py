import os
import json
import requests
from bs4 import BeautifulSoup

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = "1890536088"

URL = "https://www.fmkorea.com/hotdeal"
STATE_FILE = "last_seen.txt"

KEYWORDS = [
    "아이폰",
    "에어팟",
    "ssd",
    "갤럭시",
    "닌텐도",
    "그래픽카드",
    "특가",
    "핫딜",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def send_telegram(message: str) -> None:
    api_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    response = requests.post(
        api_url,
        data={
            "chat_id": CHAT_ID,
            "text": message,
            "disable_web_page_preview": True,
        },
        timeout=15,
    )
    print("telegram status:", response.status_code)
    print("telegram body:", response.text)


def load_last_seen() -> str:
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
    return ""


def save_last_seen(post_id: str) -> None:
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        f.write(post_id)


def fetch_posts():
    response = requests.get(URL, headers=HEADERS, timeout=15)
    print("fmkorea status:", response.status_code)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    posts = []
    for a_tag in soup.select("a.hotdeal_var8"):
        title = a_tag.get_text(strip=True)
        href = a_tag.get("href", "").strip()

        if not title or not href:
            continue

        if not href.startswith("/"):
            continue

        link = "https://www.fmkorea.com" + href
        post_id = href.split("/")[-1]

        posts.append({
            "id": post_id,
            "title": title,
            "link": link,
        })

    return posts


def filter_keyword_posts(posts):
    matched = []
    for post in posts:
        title_lower = post["title"].lower()
        for keyword in KEYWORDS:
            if keyword.lower() in title_lower:
                matched.append(post)
                break
    return matched


def main():
    print("bot start")

    posts = fetch_posts()
    if not posts:
        print("no posts found")
        return

    matched_posts = filter_keyword_posts(posts)
    print("matched count:", len(matched_posts))

    if not matched_posts:
        print("no matched keyword posts")
        return

    latest_matched = matched_posts[0]
    last_seen = load_last_seen()

    print("latest matched id:", latest_matched["id"])
    print("last seen id:", last_seen)

    if latest_matched["id"] == last_seen:
        print("already sent")
        return

    message = (
        "🚨 펨코 핫딜 알림\n\n"
        f"{latest_matched['title']}\n\n"
        f"{latest_matched['link']}"
    )

    send_telegram(message)
    save_last_seen(latest_matched["id"])
    print("sent and saved")


if __name__ == "__main__":
    main()
