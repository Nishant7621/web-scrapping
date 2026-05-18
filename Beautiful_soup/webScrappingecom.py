# import requests
# from bs4 import BeautifulSoup

# url = "https://timesofindia.indiatimes.com/"

# headers = {
#     "User-Agent": (
#         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#         "AppleWebKit/537.36 (KHTML, like Gecko) "
#         "Chrome/124.0.0.0 Safari/537.36"
#     )
# }

# r = requests.get(url, headers=headers)

# print("Status Code:", r.status_code)

# soup = BeautifulSoup(r.text, "html.parser")

# print("Title:", soup.title.text)

# # Extract headings
# headlines = soup.find_all(["h1", "h2", "h3"])

# print("\nTop Headlines:\n")

# for i, h in enumerate(headlines[:20], start=1):

#     text = h.get_text(strip=True)

#     if text:
#         print(f"{i}. {text}")

# spans=soup.find(class_="a-size-medium")
# print(spans)


import requests
import os
import csv
from bs4 import BeautifulSoup

# URL
url = "https://timesofindia.indiatimes.com/"

# Headers
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive"
}

# Send request
r = requests.get(url, headers=headers, timeout=10)

print("Status Code:", r.status_code)

# Parse HTML
soup = BeautifulSoup(r.text, "html.parser")

# ---------------------------------------------------
# 1. Page Title
# ---------------------------------------------------

if soup.title:
    print("Page Title:", soup.title.text)
else:
    print("No title found")

# ---------------------------------------------------
# # 2. Extract Headlines
# # ---------------------------------------------------

print("\nHEADLINES:\n")

headlines = soup.find_all(["h1", "h2", "h3"])

for i, h in enumerate(headlines[:10], start=1):

    text = h.get_text(strip=True)

    if text:
        print(f"{i}. {text}")

# # ---------------------------------------------------
# # 3. Extract Links
# # ---------------------------------------------------

print("\nLINKS:\n")

links = soup.find_all("a")

for i, link in enumerate(links[:10], start=1):

    href = link.get("href")

    if href:
        print(f"{i}. {href}")

# # ---------------------------------------------------
# # 4. Extract Images
# # ---------------------------------------------------

print("\nIMAGE LINKS:\n")

images = soup.find_all("img")

for i, img in enumerate(images[:5], start=1):

    src = img.get("src")

    if src:
        print(f"{i}. {src}")

# ---------------------------------------------------
# 5. Find by Class
# ---------------------------------------------------

print("\nFIND BY CLASS:\n")

elements = soup.find_all(class_=True)

for i, el in enumerate(elements[:10], start=1):

    print(f"{i}.", el.get("class"))

# ---------------------------------------------------
# 6. Save HTML File
# ---------------------------------------------------

os.makedirs("data", exist_ok=True)

with open("data/timesofindia.html", "w", encoding="utf-8") as f:
    f.write(r.text)

print("\nHTML Saved Successfully!")

# ---------------------------------------------------
# 7. Save Headlines into CSV
# ---------------------------------------------------

with open("data/headlines.csv", "w", newline="", encoding="utf-8") as f:

    writer = csv.writer(f)

    writer.writerow(["Headline"])

    for h in headlines:

        text = h.get_text(strip=True)

        if text:
            writer.writerow([text])

print("CSV Saved Successfully!")