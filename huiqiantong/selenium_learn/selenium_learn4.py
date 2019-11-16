import time

from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.toutiao.com/'
driver = webdriver.Chrome()
driver.get(url)

i = 0
title_list = []
while True:
    time.sleep(1)
    i += 100
    mouse_move = 'window.scrollTo(0,' + str(i) + ')'
    driver.execute_script(mouse_move)
    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')
    div = soup.find('div', class_='feed-infinite-wrapper')
    ul = div.find('ul')
    lis = ul.find_all('li')
    for li in lis:
        a = li.find('a')
        if a:
            title = li.find('a', class_='link').get_text()
            if title not in title_list:
                title_list.append(title)
                print(title)

