import requests
import os
import re
import time
from urllib.request import urlretrieve
from multiprocessing import Pool

"""
进程池和协程池一起使用会卡住
"""
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}


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
    resp = requests.get(url, headers=headers, params=params)
    resp_text = resp.text
    pattern = re.compile(r'"playUrl":"(.*?)",')
    list_url = pattern.findall(resp_text)
    # 获取到53值电视剧的打开地址
    # print(list_url)
    return list_url


def getUrl(ji_url):
    api = "https://jx.618g.com/?url="
    url = api + ji_url

    resp = requests.get(url, headers=headers)
    pattern = re.compile(r'url=(.*?)"')
    if resp.status_code == 200:
        text = resp.text
        ret = pattern.findall(text)
        url = ret[0]
        resp = requests.get(url, headers=headers)
        url = url[:-10] + resp.text[-20:]
        return url


def get_all_ji_url():
    for url in get_all_ji():
        url = getUrl(url)
        yield url


def split_group_by(data, split_num):
    result = []
    i = 0
    while i < len(data):
        result.append(data[i:i + split_num])
        i = i + split_num
    return result


class AnJianDowload(object):

    def __init__(self, title, ts_url, ts_prefix, save_path):
        self.title = title
        self.ts_url = ts_url
        self.ts_prefix = ts_prefix
        self.save_path = save_path

    def get_ts_url(self):
        resp = requests.get(self.ts_url, headers=headers)
        all_ts_list = []
        for url1 in resp.text.splitlines():
            if ".ts" in url1:
                all_ts_list.append(url1)

        all_ts_url = list(map(lambda x: self.ts_prefix + x, all_ts_list))
        print(all_ts_url)
        return all_ts_url

    def merge_file(self):
        os.chdir(self.save_path)
        cmd = 'copy /b *.ts new.tmp'
        os.system(cmd)
        os.system('del /Q *.ts')
        os.rename('new.tmp', self.title + '.mp4')
        print("已经下载完成{}.mp4".format(self.title))

    def download_all_ts(self, ts_url):
        pool = Pool(processes=15)
        for url in ts_url:
            filepath = os.path.join(self.save_path, url[-20:])
            pool.apply_async(urlretrieve, kwds={"url": url, "filename": filepath})
            # urlretrieve(url, filename=os.path.join(self.save_path, url[-20:]))
            # resp = requests.get(url, headers=headers)
            # # print(resp.text)
            # with open(os.path.join(self.save_path, url[-20:]), 'wb') as f:
            #     f.write(resp.content)
        pool.close()
        pool.join()


def run(anjia_obj):
    all_ts_url = anjia_obj.get_ts_url()
    anjia_obj.download_all_ts(all_ts_url)
    anjia_obj.merge_file()


def get_movie(ji_url, ji):
    save_path = r"F:\temp\安家\{}".format(ji)
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    anjia = AnJianDowload("{}集".format(ji),
                          ts_url=ji_url,
                          ts_prefix=ji_url[:-10],
                          save_path=save_path)
    run(anjia)


if __name__ == '__main__':
    ji_url_list = get_all_ji_url()
    for ji, url in enumerate(ji_url_list):
        get_movie(url, ji + 1)
        # 因为我已经下载好了之后的
        if ji >= 48:
            break
