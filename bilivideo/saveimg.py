import requests
import urllib.request


def save_img(url, img_path, hd):
    # hd = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    # }
    # url = 'https://pic1.zhimg.com/50/v2-55e588e4c02b47e41fefa514a32f48d0_hd.jpg'
    req = urllib.request.Request(url=url, headers=hd)
    response = urllib.request.urlopen(req)
    data = response.read()
    with open(img_path, 'wb') as file:
        file.write(data)
