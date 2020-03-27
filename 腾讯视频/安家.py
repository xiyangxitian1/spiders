import gevent.monkey

gevent.monkey.patch_all()
import requests
import os

from gevent.pool import Pool


# with open(os.path.join(save_path,"51集.mp4"))
class AnJianDowload(object):

    def __init__(self, title, ts_url, ts_prefix, save_path):
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        }
        # self.api = "https://jx.618g.com/?url="
        # self.save_path = r"F:\temp\安家"
        # self.download_url = self.api + url
        self.title = title
        self.ts_url = ts_url
        self.ts_prefix = ts_prefix
        self.save_path = save_path

    def get_ts_url(self):
        # 获取ts文件的地址
        # url = "https://youku.cdn2-okzy.com/20200319/8453_d5e24b8d/1000k/hls/index.m3u8"
        resp = requests.get(self.ts_url)
        # ts_prefix = "https://youku.cdn2-okzy.com/20200319/8453_d5e24b8d/1000k/hls/"

        # print(resp.text)
        # result = re.findall("^*.ts$", resp.text)
        all_ts_list = []
        for url1 in resp.text.splitlines():
            if ".ts" in url1:
                all_ts_list.append(url1)

        # print(all_ts_list)
        all_ts_url = list(map(lambda x: self.ts_prefix + x, all_ts_list))
        self.all_ts_url = all_ts_url

    def down_all_ts(self):
        # urlretrieve(url=all_ts_url, filename=os.path.join(r"F:\temp\安家", all_ts_url[-20:]))
        for url in self.all_ts_url:
            resp = requests.get(url)
            # print(resp.text)
            with open(os.path.join(self.save_path, url[-20:]), 'wb') as f:
                f.write(resp.content)

    def merge_file(self):
        os.chdir(self.save_path)
        cmd = 'copy /b *.ts new.tmp'
        os.system(cmd)
        os.system('del /Q *.ts')
        os.rename('new.tmp', self.title + '.mp4')


def run(anjia_obj):
    anjia_obj.get_ts_url()
    anjia_obj.get_all_ts()
    anjia_obj.merge_file()


def get_movie():
    # 2. 创建协程池，初始化线程数量
    # pool = Pool(5)
    # for i in range(5):
    #     pool.apply_async(get_all_ts, callback=exec_task_finished)
    #
    anjia_51 = AnJianDowload("51集",
                             ts_url="https://youku.cdn2-okzy.com/20200319/8453_d5e24b8d/1000k/hls/index.m3u8",
                             ts_prefix="https://youku.cdn2-okzy.com/20200319/8453_d5e24b8d/1000k/hls/",
                             save_path=r"F:\temp\安家\51")
    anjia_52 = AnJianDowload("52集",
                             ts_url="https://youku.cdn2-okzy.com/20200319/8454_dafd3614/1000k/hls/index.m3u8",
                             ts_prefix="https://youku.cdn2-okzy.com/20200319/8454_dafd3614/1000k/hls/",
                             save_path=r"F:\temp\安家\52")
    anjia_53 = AnJianDowload("53集",
                             ts_url="https://youku.cdn2-okzy.com/20200320/8473_1e6d9ca0/1000k/hls/index.m3u8",
                             ts_prefix="https://youku.cdn2-okzy.com/20200320/8473_1e6d9ca0/1000k/hls/",
                             save_path=r"F:\temp\安家\53")
    # anjia_obj_list = [anjia_51, anjia_52, anjia_53]
    # pool = Pool(2)
    # pool.map(run, anjia_obj_list)

    run(anjia_53)

if __name__ == '__main__':
    get_movie()