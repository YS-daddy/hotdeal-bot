import requests

TOKEN = "8473111628:AAFXmP7sl9XAgnFw3Feja9kiggZ7_AXWZc8"
CHAT_ID = "1890536088"

print("bot start")

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {
    "chat_id": CHAT_ID,
    "text": "github test message"
}

try:
    r = requests.post(url, data=data, timeout=15)
    print("status:", r.status_code)
    print("body:", r.text)
except Exception as e:
    print("error:", repr(e))
