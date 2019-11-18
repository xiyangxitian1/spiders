import time

import numpy as np
import requests
import selenium.webdriver as webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

import img_url

url = 'https://www.toutiao.com/'
browser = webdriver.Chrome()
browser.get(url)
page = browser.page_source
myinput = browser.find_element_by_css_selector('#rightModule > '
                                               'div.search-wrapper > div > div > div > input')

myinput.send_keys('街拍')
myinput.send_keys(Keys.ENTER)
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[1])  这个提示过时了
# print(browser.current_window_handle)
browser.switch_to.window(browser.window_handles[1])
# print(browser.current_window_handle)
href_list = []

for i in range(30):
    base_url = 'https://www.toutiao.com/a'
    mouse_move = 'window.scrollTo(0,' + str(500 * i) + ')'
    browser.execute_script(mouse_move)
    time.sleep(np.random.randint(1, 3))
    page = browser.page_source
    soup = BeautifulSoup(page, 'lxml')
    div = soup.find('div', class_='sections')
    # print("*" * 200)

    for div1 in div.find_all('div'):
        href = div1.find('a')['href']
        if href and 'http' not in href:
            s_url = base_url + href.split('/')[-2]
            if s_url not in href_list:
                # browser.get(s_url)
                # browser.switch_to.window(browser.window_handles[-1])
                # time.sleep(10)
                href_list.append(s_url)

# print(href_list)

# browser.quit()
url_list = []
for l in href_list:
    lst = list(img_url.get_img_url_list(l))
    if lst:
        url_list = url_list + lst
# print('*' * 100)
# print(url_list)
if url_list:
    i = 0
    for image_url in url_list:
        pic = requests.get(image_url)
        i += 1
        with open('G:\\downs\\jiepai\\' + str(i) + '.jpg', 'wb') as f:
            print('正在保存第{0}'.format(i))
            f.write(pic.content)

browser.quit()  # 关闭浏览器
