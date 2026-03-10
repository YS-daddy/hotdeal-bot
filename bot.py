import os
import requests

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = "1890536088"

print("bot start")

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {
    "chat_id": CHAT_ID,
    "text": "github test message"
}

r = requests.post(url, data=data, timeout=15)

print("status:", r.status_code)
print("body:", r.text)
