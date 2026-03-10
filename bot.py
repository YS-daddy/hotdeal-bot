import requests

TOKEN = "8473111628:AAHtQaEyPl89VDKMRqMvtPV1pxTWjHFpcEg"
CHAT_ID = "1890536088"

def send(msg):

    url=f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data={
        "chat_id":CHAT_ID,
        "text":msg
    }

    r=requests.post(url,data=data)

    print(r.text)


if __name__=="__main__":

    send("✅ 핫딜봇 테스트 성공")
