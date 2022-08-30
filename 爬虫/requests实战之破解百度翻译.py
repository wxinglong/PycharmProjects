import requests
import json
if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }
    url = "https://fanyi.baidu.com/sug"
    value = input("enter a word:")
    data = {
        "kw": value
    }
    response = requests.post(url=url, data=data, headers=headers)
    obj_dict = response.json()
    file_name = value + ".json"
    fp = open(file_name, "w", encoding="utf-8")
    json.dump(obj_dict, fp=fp, ensure_ascii=False)