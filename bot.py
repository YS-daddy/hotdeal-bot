import requests

TOKEN="8473111628:AAHtQaEyPl89VDKMRqMvtPV1pxTWjHFpcEg"
CHAT_ID="1890536088"

print("bot start")

url="https://api.telegram.org/bot"+TOKEN+"/sendMessage"

data={
"chat_id":CHAT_ID,
"text":"github test message"
}

r=requests.post(url,data=data)

print(r.status_code)
print(r.text)
