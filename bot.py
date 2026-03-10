import requests

TOKEN = "8473111628:AAHtQaEyPl89VDKMRqMvtPV1pxTWjHFpcEg"
CHAT_ID = "1890536088"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "text": "🔥 GitHub에서 보낸 테스트 메시지"
}

response = requests.post(url, data=data)

print(response.status_code)
print(response.text)
