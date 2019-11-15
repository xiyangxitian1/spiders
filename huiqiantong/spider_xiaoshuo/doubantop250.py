import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250?start='
# https://movie.douban.com/top250?start=0&filter=
count = 0
mlist = []
for i in range(10):
    count = 25 * i
    url1 = url + str(count)
    resp = requests.get(url1)
    if resp.status_code == 200:
        html = resp.text
        mysoup = BeautifulSoup(html, 'lxml')  # 默认的解析方式是html.parser
        # find方法只找第一个  find_all方法查找所有的
        res = mysoup.find('ol')  # 返回是是Tag标签对象
        movie_list = res.find_all('li')
        # print(len(movie_list))
        for movie in movie_list:
            # movie.find('sapn', {'class', 'title'})
            # movie.find('span', attrs={'class', 'title'})
            title = movie.find('span', class_='title').get_text()
            # title = title.get_text()
            # print(title)
            mlist.append(title)
print(len(mlist))
with open('results.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(mlist))
