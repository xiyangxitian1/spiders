import random
import time

import requests

"""爬取百度图片"""
params = {
    'tn': 'resultjson_com',
    'ipn': 'rj',
    'ct': 201326592,
    'fp': 'result',
    'queryWord': '皮卡丘图片',
    'cl': 2,
    'lm': -1,
    'ie': 'utf-8',
    'oe': 'utf-8',
    'st': -1,
    'word': '皮卡丘图片',
    'face': 0,
    'istype': 2,
    'nc': 1,
    'pn': 0,
    'rn': 30,
}

hd = {
    'Connection': 'close',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
}

url = 'https://image.baidu.com/search/acjson'
pn = 0
img_paths = []
for i in range(30):
    pn += i * 30
    params['pn'] = pn
    resp = requests.get(url, params=params)
    json = resp.json()
    list = json['data']
    for l in list:
        if l:
            for dict in l['replaceUrl']:
                for key in dict:
                    if key == 'ObjUrl':
                        p_url = dict[key]
                        # print(p_url)
                        img_paths.append(p_url)
                        break

print(len(img_paths))
requests.adapters.DEFAULT_RETRIES = 5
count = 0
for u in img_paths:
    try:
        resp = requests.get(u, headers=hd, stream=True)  # 使用requests.get()获取图片，但要将参数stream设为True。
        if resp.status_code == 200:
            # print(u)
            count += 1
            if '?' in str(u):
                jpg = str(u).split('?')[0].split('.')[-1]
            else:
                jpg = str(u).split('.')[-1]
            img_name = str(count) + '.' + jpg
            with open('f:/pikaqiu/' + img_name, 'wb') as f:
                f.write(resp.content)
            time.sleep(random.randint(1, 2))
    except (requests.exceptions.ConnectionError, FileNotFoundError) as e:
        print('出错了ConnectionError')
        continue
    # print(resp)
