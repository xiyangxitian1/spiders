import requests
import re


class XiaoShuo(object):

    def __init__(self, title, base_url):
        self.base_url = base_url
        self.title = title

    def get_all_article_url(self):
        resp = requests.get(self.base_url)
        if resp.status_code == 200:
            content = resp.content.decode("gbk")
            pattern = re.compile('<a href="(\d*?).html"')
            ret = pattern.findall(content)
            for article_url in ret:
                yield self.base_url + article_url + ".html"

    def get_article_content(self):
        for article_url in self.get_all_article_url():
            resp = requests.get(article_url)
            if resp.status_code == 200:
                article = resp.content.decode("GBK")
                pattern1 = re.compile('<div id="content">(.*?)</div>')
                pattern2 = re.compile('<h1>(.*?)</h1>')
                ret = pattern1.findall(article)[0]
                title = pattern2.findall(article)[0]
                ret = ret.replace("（每一个钟头上传一章，直到传完二十章！红票和收藏别忘了～）", "") \
                    .replace("<br />", "") \
                    .replace("&nbsp;", " ")
                yield title, ret

    def download(self):
        i = 0
        with open("./{}.txt".format(self.title), "a") as f:
            for title, article in self.get_article_content():
                f.write(title)
                f.write("\n\n")
                f.write(article)
                f.write("\n\n")
                i += 1
                if i % 10 == 0:
                    print("已经下载完成{}章".format(i))
        print("下载完成，请享受阅读……")


if __name__ == '__main__':
    url = "https://www.37zw.net/6/6038/"
    title = "剑道通神"
    x = XiaoShuo(title, url)
    x.download()
