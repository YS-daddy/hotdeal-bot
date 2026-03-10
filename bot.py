import requests
from bs4 import BeautifulSoup

TOKEN = "8473111628:AAHtQaEyPl89VDKMRqMvtPV1pxTWjHFpcEg"
CHAT_ID = "1890536088"

KEYWORDS = [
"아이폰",
"에어팟",
"SSD",
"그래픽카드",
"갤럭시",
"닌텐도",
"특가",
"핫딜"
]

URL = "https://www.fmkorea.com/hotdeal"

def send(msg):

    api = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": msg
    }

    requests.post(api,data=data)

def check():

    headers = {
        "User-Agent":"Mozilla/5.0"
    }

    r = requests.get(URL,headers=headers)

    soup = BeautifulSoup(r.text,"html.parser")

    posts = soup.select("a.hotdeal_var8")

    for p in posts[:15]:

        title = p.text.strip()
        link = "https://www.fmkorea.com"+p["href"]

        for k in KEYWORDS:

            if k in title:

                msg=f"""
🚨 펨코 핫딜 발견

{title}

{link}
"""

                send(msg)
                return

if __name__=="__main__":

    send("✅ 핫딜봇 테스트 메시지")

    check()

# run
