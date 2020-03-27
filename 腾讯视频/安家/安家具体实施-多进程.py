import requests
import os

from multiprocessing import Process as Task


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
        resp = requests.get(self.ts_url)
        all_ts_list = []
        for url1 in resp.text.splitlines():
            if ".ts" in url1:
                all_ts_list.append(url1)

        all_ts_url = list(map(lambda x: self.ts_prefix + x, all_ts_list))
        return all_ts_url

    def merge_file(self):
        os.chdir(self.save_path)
        cmd = 'copy /b *.ts new.tmp'
        os.system(cmd)
        os.system('del /Q *.ts')
        os.rename('new.tmp', self.title + '.mp4')

    def download_all_ts(self, ts_url):
        for url in ts_url:
            resp = requests.get(url)
            # print(resp.text)
            with open(os.path.join(self.save_path, url[-20:]), 'wb') as f:
                f.write(resp.content)


def run(anjia_obj):
    all_ts_url = anjia_obj.get_ts_url()
    all_ts_url_group_list = split_group_by(all_ts_url, split_num=5)
    tasks = []
    for ts_url in all_ts_url_group_list:
        task = Task(target=anjia_obj.download_all_ts, args=(ts_url,), daemon=True)
        tasks.append(task)
        task.start()

    for task in tasks:
        task.join()

    anjia_obj.merge_file()


def get_movie(ji_url):
    save_path = r"D:\temp\安家\50"
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    anjia_50 = AnJianDowload("50集",
                             # ts_url="https://youku.cdn2-okzy.com/20200318/8430_bb611164/1000k/hls/index.m3u8",
                             ts_url=ji_url,
                             ts_prefix=ji_url[:-10],
                             save_path=save_path)
    run(anjia_50)


if __name__ == '__main__':
    get_movie()
