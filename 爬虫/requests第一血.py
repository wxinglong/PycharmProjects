import requests
if __name__ == "__main__":
    url = "https://www.sougou.com/"
    response = requests.get(url=url)
    page_text = response.text
    print(page_text)
    with open("./sougou.html", "w", encoding="utf-8") as f:
        f.write(page_text)