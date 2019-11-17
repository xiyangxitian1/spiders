import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'http://www.tianqihoubao.com/aqi/beijing-201812.html'


def getcontent1():
    """
    普通的方式获取表格数据
    :return:
    """
    response = requests.get(url)
    if response.status_code == 200:
        # print(response.text)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        table = soup.find('table', class_='b')
        columns = ''
        datas = ''
        trs = table.find_all('tr')
        column_names = trs[0].find_all('td')
        for name in column_names:
            columns += name.get_text().strip()
            columns += ','
        for tr in trs[1:]:
            tds = tr.find_all('td')
            for td in tds:
                datas += td.get_text().strip()
                datas += ','
            datas += '\n'
        print(columns)
        print(datas)


def getcontent2(url):
    """
    pandas的方式获取表格数据
    :return:
    """
    response = requests.get(url)
    if response.status_code == 200:
        # print(response.text)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        table = soup.find('table', class_='b')
        df = pd.read_html(table.prettify(), header=0)
        # print(df)
        # print(df[0])
        # print(type(df))
        df[0].to_csv('results.csv', header=None, encoding='utf-8-sig', mode='a')


if __name__ == '__main__':
    base_url = 'http://www.tianqihoubao.com/aqi/'
    citys = ['beijing', 'shanghai', 'shenzhen', 'wuhan']
    months = ['201801', '201802', '201803', '201804', '201805', '201806',
              '201807', '201808', '201809', '201810']
    for c in citys:
        for m in months:
            url = base_url + c + '-' + m + '.html'
            getcontent2(url)
    print('执行结束')
