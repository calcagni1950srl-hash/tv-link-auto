import requests
import re
import json

RUSSIA1_PAGE = "https://smotrim.ru/channel/1"
RUSSIA24_PAGE = "https://smotrim.ru/channel/3"

def extract_m3u8(url):
    html = requests.get(url).text
    match = re.search(r'https://[^"]+\.m3u8[^"]*', html)
    return match.group(0) if match else ""

def main():
    data = {
        "russia1": extract_m3u8(RUSSIA1_PAGE),
        "russia24": extract_m3u8(RUSSIA24_PAGE)
    }

    with open("links.json", "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    main()
