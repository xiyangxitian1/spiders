import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException
import json
import time
from hashlib import md5


# a = md5('aaa'.encode()).hexdigest()

hd = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}


def get_page_index(offset, keyword):
    '''获取索引页'''
    params = {
        'aid': 24,
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'en_qc': 1,
        'cur_tab': 1,
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': int(time.time()),
    }
    # url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)
    url = 'https://www.toutiao.com/api/search/content/'
    try:
        resp = requests.get(url, headers=hd, params=params)
        if resp.status_code == 200:
            return resp.json()
        else:
            return None
    except RequestException:
        print('请求索引页出错！')
        return None


def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data:
        print(data.get('data'))
        for item in data.get('data'):
            yield item.get('article_url')


def main():
    offset = 0
    keyword = '街拍'
    html = get_page_index(offset, keyword)
    print(html)
    # for url in parse_page_index(html):
    #     print(url)


if __name__ == '__main__':
    main()
