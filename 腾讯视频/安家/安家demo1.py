import requests
import time
import re


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
