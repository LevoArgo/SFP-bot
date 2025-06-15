import yfinance as yf
import pandas as pd
import requests
from datetime import datetime

# Telegram ayarları
BOT_TOKEN = "bot7964205504:AAEWHnCAQN8kSWQMlS2ocrjOFm3AL2a_l2M"  # kendi bot token'ını yaz
CHAT_ID = "5891187255"  # kendi chat_id'ni yaz

# BIST sembolleri (örnek)
symbols = ["AKBNK.IS", "THYAO.IS", "SISE.IS", "ASELS.IS", "KRDMD.IS"]  # tüm BIST'i buraya ekle

# Zaman dilimleri
timeframes = {
    "30m": "30m",
    "1h": "60m",
    "4h": "240m",
    "1d": "1d",
    "1w": "1wk",
    "1mo": "1mo"
}

def send_to_telegram(message):
    url = f"https://api.telegram.org/{7964205504:AAEWHnCAQN8kSWQMlS2ocrjOFm3AL2a_l2M}/sendMessage"
    payload = {"chat_id": 5891187255, "text": message}
    requests.post(url, json=payload)

def check_sfp(df):
    if len(df) < 51:
        return False
    prev = df.iloc[-2]
    curr = df.iloc[-1]
    body = abs(prev['Close'] - prev['Open'])
    half_range = body * 0.5
    max_high = prev['Close'] + half_range
    max_close = prev['Close'] + half_range
    is_ref = prev['Close'] <= df['Close'][-51:-1].min()
    is_trigger = curr['Low'] < prev['Low'] and curr['High'] <= max_high and curr['Close'] > prev['Close'] and curr['Close'] <= max_close
    return is_ref and is_trigger

for symbol in symbols:
    for label, interval in timeframes.items():
        try:
            df = yf.download(symbol, interval=interval, period="60d")
            if check_sfp(df):
                msg = f"📣 SFP Sinyali Tespit Edildi!\n\n🪙 Sembol: {symbol}\n⏱️ Zaman Dilimi: {label}\n🕒 Zaman: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
                send_to_telegram(msg)
        except Exception as e:
            print(f"{symbol} - {label} hata: {e}")