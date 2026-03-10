import requests

TOKEN="8473111628:AAHtQaEyPl89VDKMRqMvtPV1pxTWjHFpcEg"
CHAT_ID="1890536088"

print("bot start")

url="https://api.telegram.org/bot"+TOKEN+"/sendMessage"

data={
"chat_id":CHAT_ID,
"text":"🔥 GitHub 테스트 메시지"
}

r=requests.post(url,data=data)

print(r.status_code)
print(r.text)
