import requests

url = 'https://www.iqiyi.com/v_19rs97niz4.html#vfrm=19-9-0-1'
# url = 'blob:https://www.iqiyi.com/41d9cb54-a0a5-4770-b003-5e929cf809cb'
hd = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/78.0.3904.87 Safari/537.36',
}
resp = requests.get(url)
print(resp)
