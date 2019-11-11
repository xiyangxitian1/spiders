import time
import requests
import random

"""下载bilibili每日热门前100条视频"""


def get_json(url, num):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    params = {
        'page_size': 10,
        'next_offset': str(num),
        'tag': '今日热门',
        'platform': 'pc'
    }
    try:
        html = requests.get(url, params=params, headers=headers)
        return html.json()
    except BaseException:
        print("request error")


def downloader(url, path):
    # start = time.time()
    # size = 0
    path = "F:\\bilibili_videos\\" + path
    # headers = {
    #     'Accept': 'application/json, text/plain, */*',
    #     'Accept-Encoding': 'gzip, deflate',
    #     'Accept-Language': 'zh-CN,zh;q=0.9',
    #     'Connection': 'keep-alive',
    #     'Cookie': 'l=v; Hm_lvt_8dabccb80a103a16cdfecde99700b220=1573439482; '
    #              'LIVE_BUVID=AUTO1815734394820873; _uuid=A04BF785-DBBD-60F3-48B3-FF24D57D0F4582032infoc; buvid3=403F186B-E761-40C7-AB38-DA847AE8CE54155832infoc; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1573439482; Hm_lpvt_8dabccb80a103a16cdfecde99700b220=1573444629; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1573444629',
    #     'Host': 'api.vc.bilibili.com',
    #     'Origin': 'http://vc.bilibili.com',
    #     'Referer': 'http://vc.bilibili.com/p/eden/rank',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    # }
    hd = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url, headers=hd, stream='True')  # stream属性必须带上
    chunck_size = 1024  # 每次下载的数据大小
    content_size = int(response.headers['Content-Length'])  # 总大小
    if response.status_code == 200:
        print(
            "[文件大小]:%0.2f MB" % (content_size / chunck_size / 1024))  # 换算单位
        print("path:" + path)
        with open(path, 'wb') as file:
            for data in response.iter_content(chunk_size=chunck_size):
                if data:
                    file.write(data)
                    # size += len(data)  # 已下载的文件大小


if __name__ == '__main__':
    for i in range(10):
        url = 'http://api.vc.bilibili.com/board/v1/ranking/top?'
        num = i * 10 + 1
        html = get_json(url, num)
        infos = html['data']['items']
        for info in infos:
            title = info['item']['description']  # 小视频的标题
            video_path = info['item']['video_playurl']  # 小视频的下载地址
            # 为了防止有些视频没有提供下载链接的情况
            try:
                downloader(video_path, path='%s.mp4' % title)
                print("成功下载一个")
            except BaseException:
                print("凉凉，下载失败！")
            # 设置随机等待时间
            time.sleep(int(format(random.randint(2, 8))))
