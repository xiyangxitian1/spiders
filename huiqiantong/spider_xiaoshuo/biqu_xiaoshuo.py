# import urllib
import requests
from bs4 import BeautifulSoup

base_url = 'https://www.biquge.info/21_21099/'


# html.parse  pip install lxml
# 没有安装就不能解析 可以用html.parse 不用安装，不过效率会低点
# pip install lxml

def get_all_list():
    """得到所有章节的url"""
    url_list = []
    html = get_data(base_url)
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    mydiv = soup.find('div', id='list')  # 找到所有章节所在的div标签
    mydds = mydiv.find_all('dd')
    for dd in mydds:
        new_url = dd.find('a')['href']
        url_list.append(new_url)
    return url_list


def get_data(url):
    response = requests.get(url)

    if response.status_code == 200:
        html = response.content.decode(response.apparent_encoding, 'ignore')
        return html


def parse_data(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find('div', {'class': 'bookname'}).find('h1').get_text()
    mydiv = soup.find('div', id='content')
    text = mydiv.get_text()
    text = '\t\t\t' + title + '\n' + text
    return text


content = '\t\t\t打火机与公主裙\n'

for url in get_all_list():
    real_url = base_url + url
    html = get_data(real_url)
    text = parse_data(html)
    content += text
    content += '\n\n'
# print(content)
with open('f:/a.txt', mode='w', encoding='utf-8') as file:
    file.write(content)
print("执行完毕！")
