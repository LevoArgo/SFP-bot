from flask import Flask, request
import requests
import json

app = Flask(__name__)

# Telegram bilgileri
TELEGRAM_BOT_TOKEN = "bot7964205504:AAEWHnCAQN8kSWQMlS2ocrjOFm3AL2a_l2M"  # 🔴 Buraya kendi bot token'ını yaz
CHAT_ID = "5891187255"  # 🔴 Buraya kendi chat_id'ni yaz

def send_to_telegram(msg):
    url = f"https://api.telegram.org/{7964205504:AAEWHnCAQN8kSWQMlS2ocrjOFm3AL2a_l2M}/sendMessage"
    payload = {
        "chat_id": 5891187255,
        "text": msg
    }
    response = requests.post(url, json=payload)
    print("Telegram yanıtı:", response.text)

@app.route('/hook', methods=['POST'])
def webhook():
    print("Ham veri:", request.data.decode())
    try:
        print("Header:", request.headers.get("Content-Type"))
        print("Ham veri:", request.data.decode())

        if request.is_json:
            data = request.get_json()
        else:
            data = json.loads(request.data.decode())

        print("Webhook içeriği:", data)

        msg = data.get("message", "⚠️ Boş mesaj geldi kralım")
        send_to_telegram(msg)
        return "OK", 200
    except Exception as e:
        print("Webhook JSON hatası:", str(e))
        return "Error", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)