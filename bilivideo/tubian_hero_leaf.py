import os
import re
from multiprocessing import Pool
from urllib.request import urlretrieve

import requests
from pyquery import PyQuery as pq


class video_down():
    """
    下载F:\tubian_leaf
    凸变英雄  下载   腾讯视频vip可以看
    """

    def __init__(self, url):
        # 拼接全民解析url
        self.api = 'https//jx.618g.com'
        self.get_url = 'https://jx.618g.com/?url=' + url
        # 设置UA模拟浏览器访问
        self.head = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        }
        # 设置多线程数量
        self.thread_num = 32
        # 当前已经下载的文件数目
        self.i = 0
        self.path = r'F:\tubian_leaf'
        # 调用网页获取
        html = self.get_page(self.get_url)
        if html:
            # 解析网页
            self.parse_page(html)

    def get_page(self, get_url):
        try:
            print('正在请求目标网页完成...\n准备解析', get_url)
            response = requests.get(get_url, headers=self.head)
            if response.status_code == 200:
                print('请求目标网页完成...\n准备解析...')
                return response.text

        except Exception:
            print('请求目标网页失败，请检查错误重试')
            return None

    def parse_page(self, html):
        # print('目标信息正在解析')
        doc = pq(html)
        self.title = doc('head title').text()
        print(self.title)
        url = doc('#player').attr('src')[17:]
        # print(url)
        all_ts = self.get_m3u8_1(url)
        self.ts_lists = list(all_ts)
        # print('信息提取完成   \n 准备下载')
        self.pool()
        # for ts in all_ts:
        #     down_url = url[:23] + ts
        #     print('解析完成，获取缓存ts文件')
        #     self.get_m3u8_2(self.url)

    def get_m3u8_1(self, url):
        try:
            response = requests.get(url, headers=self.head)
            html = response.text
            # print('获取ts文件成功，准备提取信息')
            pattern = '/hls.*\.ts'
            allts = re.findall(pattern, html)
            for ts in allts:
                yield url[:23] + ts
            # return html[-20:]
        except Exception:
            print('缓存文件请求错误1，请检查错误')

    def pool(self):
        # print('需要下载%d个文件' % len(self.ts_lists))
        # self.ts_url = self.url[:-10]
        if self.title not in os.listdir():
            # os.makedirs('正在下载...所需时间较长，请耐心等待..')
            # os.makedirs('/videos', 0o755)
            # os.makedirs('F:\\tubian_leaf\\' + self.title)
            try:
                os.makedirs(self.path)
            except FileExistsError:
                # print('文件{}已经存在，不需要再创建'.format(self.path))
                pass
            # print('正在下载...所需时间较长，请耐心等待...')
            # 开启多线程下载
            pool = Pool(16)
            pool.map(self.save_ts, self.ts_lists)
            pool.close()
            pool.join()
            print('下载完成')
            self.ts_to_mp4(self.path, self.title)

    def ts_to_mp4(self, path, title):
        print('ts文件正在进行转录mp4....')
        os.chdir(path)
        cmd = 'copy /b *.ts new.tmp'
        os.system(cmd)
        os.system('del /Q *.ts')
        os.rename('new.tmp', title + '.mp4')
        # shutil.rmtree(self.title)

    def save_ts(self, ts_list):
        try:
            # print('线程名：' + threading.current_thread().getName(), ts_list)
            self.i += 1
            # print('当前进度%d/%d' % (self.i, len(self.ts_lists)))
            urlretrieve(url=ts_list,
                        filename=self.path + '\\{}'.format(ts_list[-8:]))
        except Exception:
            print('保存文件出现错误')


if __name__ == '__main__':
    # 电影目标url：狄仁杰之四大天王
    # url = 'https://v.qq.com/x/cover/r6ri9qkcu66dna8.html'
    # # 电影碟中谍5：神秘国度
    # url1 = 'https://v.qq.com/x/cover/5c58griiqftvq00.html'
    # # 电视剧斗破苍穹
    # url2 = 'https://v.qq.com/x/cover/lcpwn26degwm7t3/z0027injhcq.html'
    # url3 = 'https://v.qq.com/x/cover/33bfp8mmgakf0gi.html'
    # url = 'https://v.qq.com/x/cover/blhvtkddwgr1x28/z0029bd3j5q.html?ptag=iqiyi'
    # url = 'https://v.qq.com/x/cover/blhvtkddwgr1x28/z0029bd3j5q.html'  # 第一集
    url = 'https://v.qq.com/x/cover/blhvtkddwgr1x28/'
    url_ji = ['z0029bd3j5q.html',
              'o0029jg9qpl.html',  # 第2集
              'd0029mivqfc.html',
              'u0029kvzopw.html',
              'r0029giksh1.html',
              'a0029nds3z8.html',
              'p0029ddbn8x.html',  # 第7集
              'v0029gscl7i.html',
              'e0029ay7q0c.html',
              'u0029e2ggcn.html',
              'a0029051x1b.html',
              'e0029pspmjk.html',  # 12
              ]
    all_url_list = []
    for url_ in url_ji:
        all_url_list.append(url + url_)

    for i, url in enumerate(all_url_list):
        print('正在下载第{}集'.format(i + 1))
        video_down(url)

    print('全部下载完成')
