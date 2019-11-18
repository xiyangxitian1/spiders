import time
from urllib.parse import urlencode

import requests
from requests.exceptions import RequestException


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
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)
    hd = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
    }
    try:
        resp = requests.get(url, headers=hd)
        if resp.status_code == 200:
            return resp.text
        else:
            return None
    except RequestException:
        print('请求索引页出错！')
        return None


if __name__ == '__main__':
    json = get_page_index(0, '街拍')
    print(json)
