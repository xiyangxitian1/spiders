import requests
from bs4 import BeautifulSoup


class XueZhong(object):

    def __init__(self):
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
        }
        self.base_url = "https://www.37zw.net/0/761/"

    def run(self):
        resp = requests.get(self.base_url)
        if resp.status_code == 200:
            print(resp.text)
            soup = BeautifulSoup(resp.text, "lxml")
            div = soup.find("div", id="list")
            # print(div)
            for d in div:
                a = soup.find_all("a.href")
                print(a)

if __name__ == '__main__':
    x = XueZhong()
    x.run()
