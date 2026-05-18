import requests
import os
from bs4 import BeautifulSoup
def fetchAndSaveToFile(url, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:
        r = requests.get(url, headers=headers, timeout=10)

        if r.status_code == 200:
            with open(path, "w", encoding="utf-8") as f:
                f.write(r.text)
            print("✅ File saved successfully!")
        else:
            print("❌ Failed with status:", r.status_code)

    except requests.exceptions.RequestException as e:
        print("⚠️ Error:", e)


url = "https://timesofindia.indiatimes.com/"
fetchAndSaveToFile(url, "data/times.html")
