import requests

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get("http://example.org", headers=headers)
print(r.text)