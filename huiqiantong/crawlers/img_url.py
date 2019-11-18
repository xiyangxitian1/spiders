import re

import requests

url = 'https://www.toutiao.com/a6760528357990859277/'


def get_img_url_list(url):
    """获取页面的所有的图片的地址"""
    hd_guge = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    }
    hd_qq = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400',
    }
    resp = requests.get(url, headers=hd_qq)
    if resp.status_code == 200:
        page = resp.text
        # print(page)
        pattern = re.compile(r'http:.{70,90}\&')
        results = re.findall(pattern, page)
        if results:
            for result in results:
                img_path = result.split('\\&')[0].encode('utf-8').decode("unicode_escape")
                # print('img_path:', img_path)
                yield img_path


if __name__ == '__main__':
    url = 'https://www.toutiao.com/a6760303750503465480'
    result = get_img_url_list(url)
    print(list(result))
