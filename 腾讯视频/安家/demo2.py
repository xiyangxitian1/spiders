import requests
import re
import time


def get_all_ji():
    url = "https://s.video.qq.com/get_playsource"

    params = {
        "id": "ihhsfwvvhcm16nd",
        "plat": "2",
        "type": "4",
        "range": "1 - 53",
        "data_type": "2",
        "video_type": "2",
        "plname": "qq",
        "otype": "json",
        "uid": "2ba3bc8b - 2175 - 4f57 - 825e - e1166a08032f",
        "callback": "_jsonp_0_7a86",
        "_t": int(time.time() * 1000),
    }
    resp = requests.get(url, params=params)
    resp_text = resp.text
    pattern = re.compile(r'"playUrl":"(.*?)",')
    list_url = pattern.findall(resp_text)
    # 获取到53值电视剧的打开地址
    # print(list_url)
    return list_url


def getUrl(ji_url):
    # url = "https://v.qq.com/x/cover/ihhsfwvvhcm16nd/q00335hcviu.html"
    api = "https://jx.618g.com/?url="
    #
    url = api + ji_url
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    pattern = re.compile(r'url=(.*?)"')
    if resp.status_code == 200:
        text = resp.text
        ret = pattern.findall(text)
        # https://iqiyi.cdn9-okzy.com/20200221/6520_7ce2e6f2/index.m3u8
        url = ret[0]
        resp = requests.get(url)
        url = url[:-10] + resp.text[-20:]
        return url


def get_all_ji_url():
    url_list = []
    for url in get_all_ji():
        url = getUrl(url)
        url_list.append(url)

    print(url_list)
    return url_list


if __name__ == '__main__':
    get_all_ji_url()
