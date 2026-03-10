import requests
from bs4 import BeautifulSoup

TOKEN = "8473111628:AAHtQaEyPl89VDKMRqMvtPV1pxTWjHFpcEg"
CHAT_ID = "1890536088"

URL = "https://www.fmkorea.com/hotdeal"

def send(msg):

    api=f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data={
        "chat_id":CHAT_ID,
        "text":msg
    }

    requests.post(api,data=data)

def check_hotdeal():

    headers={"User-Agent":"Mozilla/5.0"}

    r=requests.get(URL,headers=headers)

    soup=BeautifulSoup(r.text,"html.parser")

    posts=soup.select("a.hotdeal_var8")

    if not posts:
        send("⚠️ 펨코 글 파싱 실패")
        return

    title=posts[0].text.strip()
    link="https://www.fmkorea.com"+posts[0]["href"]

    msg=f"""
🔥 펨코 핫딜 최신글

{title}

{link}
"""

    send(msg)


if __name__=="__main__":

    send("✅ 핫딜봇 정상 실행 테스트")

    check_hotdeal()
