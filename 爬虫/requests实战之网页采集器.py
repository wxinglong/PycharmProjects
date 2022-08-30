import requests
if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }
    url = "https://www.sogou.com/web?"
    # 处理url携带的参数，封装到字典中
    value = input("enter a word:")
    params = {
        "query": value
    }
    response = requests.get(url=url, params=params, headers=headers)
    page_text = response.text
    file_name = value + ".html"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(page_text)
