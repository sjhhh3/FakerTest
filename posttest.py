import requests
import json

url = "http://httpbin.org/post"

def posting(data):
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'})
    res = requests.post(url, data=data, headers=headers)
    return res

