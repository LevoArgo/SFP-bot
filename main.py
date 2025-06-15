from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Telegram ayarları (Token ve Chat ID .env’den veya direkt değişkenden alabilirsin)
BOT_TOKEN = os.getenv("BOT_TOKEN", "bot7964205504:AAEWHnCAQN8kSWQMlS2ocrjOFm3AL2a_l2M")  # kendi token'ını yaz
CHAT_ID = os.getenv("5891187255", "5891187255")  # kendi chat ID'ni yaz

def send_to_telegram(msg):
    url = f"https://api.telegram.org/bot{7964205504:AAEWHnCAQN8kSWQMlS2ocrjOFm3AL2a_l2M}/sendMessage"
    payload = {"chat_id": 5891187255, "text": msg}
    try:
        res = requests.post(url, json=payload)
        print("📤 Telegram’a gönderildi:", res.status_code)
    except Exception as e:
        print("❌ Telegram gönderim hatası:", e)

@app.route('/')
def index():
    return "👋 SFP Bot Aktif Kralım!"

@app.route('/hook', methods=['POST'])
def hook():
    try:
        raw = request.data.decode('utf-8')
        print("🔥 GÖNDERİLEN VERİ:", raw)

        data = request.get_json(force=True)
        print("✅ ÇÖZÜLEN VERİ:", data)

        message = data.get("message", "❗ Mesaj alanı boş kralım.")
        print("📢 Mesaj:", message)

        send_to_telegram(message)
        return "OK", 200

    except Exception as e:
        print("❌ Webhook Hatası:", str(e))
        return "ERROR", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)