import requests

url = 'https://cn5.7639616.com/hls/20191102/e77b2eef9d20909732e4bdf990be8a1c/1572677033/0.ts'
hd = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}
resp = requests.get(url, hd)
with open('f:/1.ts', 'wb') as f:
    f.write(resp.content)
