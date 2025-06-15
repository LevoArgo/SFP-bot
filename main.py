from flask import Flask, request
import requests

app = Flask(__name__)

# Sabit bot bilgileri
TELEGRAM_TOKEN = "7964205504:AAEWHnCAQN8kSWQMlS2ocrjOFm3AL2a_l2M"
CHAT_ID = "5891187255"

@app.route("/hook", methods=["POST"])
def hook():
    try:
        data = request.get_json(force=True)
        print("Webhook içeriği:", data)
    except Exception as e:
        print("Webhook JSON hatası:", str(e))
        data = {}

    # TradingView'den gelen mesaj varsa al, yoksa varsayılan mesaj yolla
    incoming_msg = data.get("message", "📣 SFP sinyali tetiklendi kralım!")

    # Telegram'a POST isteği gönder
    response = requests.post(
        f"https://api.telegram.org/bot7964205504:AAEWHnCAQN8kSWQMlS2ocrjOFm3AL2a_l2M/sendMessage",
        data={"chat_id": "5891187255", "text": incoming_msg}
    )

    # Log için istersen bu satırı da bırakabilirsin:
    print("Telegram yanıtı:", response.text)

    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)