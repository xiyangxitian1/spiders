import time

import requests

url = 'https://www.toutiao.com/api/pc/feed/'

hd = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}

l = int(time.time())
params = {
    'max_behot_time': 'l',
    'category': '__all__',
    'utm_source': 'toutiao',
    'widen': '1',
    'tadrequire': 'true',
    'as': 'A105DD7CAF6F877',
    'cp': '5DCF9F68D7D7FE1',
    '_signature': 'HGbe7AAgEBLwWqXedd8rZhxm3vAAEGt',
}

resp = requests.get(url, headers=hd, params=params)
html = resp.json()
list = html['data']
title_list = []
for l in list:
    title = l['title']
    title_list.append(title)

print(title_list)
print(len(title_list))

# print(int(l))  # 1573814348

# 1573909815.3344214
# 1573814348
