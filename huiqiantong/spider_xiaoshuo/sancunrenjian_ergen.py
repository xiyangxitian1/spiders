import requests
from bs4 import BeautifulSoup

base_url = 'http://www.cits0871.com/booktxt/1/'


def get_html(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.content.decode(resp.apparent_encoding, 'ignore')


def get_soup(url, features='lxml'):
    html = get_html(url)
    return BeautifulSoup(html, features)


def dowload(xiaoshuo_url):
    """下载小说(三寸人间)"""
    soup = get_soup(xiaoshuo_url)
    mydiv = soup.find('div', id='list')
    mydds = mydiv.find_all('dd')
    all_contents = '\t\t\t三寸人间\n'
    # len = len(mydds)
    # cen = 0
    for dd in mydds:
        # print('当前下载进度{}%'.format(cen/len))
        # cen += 1
        html = dd.find('a')['href']
        url = str(html).split('/')[-1]
        soup = get_soup(url)
        title = soup.find('div', {'class': 'bookname'}).find(
            'h1').get_text()
        # print('title', title)
        content = soup.find('div', id='content').get_text()
        # print('content', content)
        all_contents = all_contents + '\t\t\t' + title + '\n' + content + \
                       '\n'

    with open('f:/三寸人间-耳根.txt', 'w', encoding='utf-8') as f:
        f.write(all_contents)
    print('下载完成')
