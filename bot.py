import requests

TOKEN="8473111628:AAHtQaEyPl89VDKMRqMvtPV1pxTWjHFpcEg"
CHAT_ID="1890536088"

url=f"https://api.telegram.org/bot{TOKEN}/sendMessage"

data={
    "chat_id":CHAT_ID,
    "text":"🔥 텔레그램 연결 테스트 성공"
}

requests.post(url,data=data)
