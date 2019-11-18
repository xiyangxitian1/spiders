import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time

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

base_url = 'https://www.toutiao.com/a'
mouse_move = 'window.scrollTo(0,' + str(300) + ')'
browser.execute_script(mouse_move)
time.sleep(5)
page = browser.page_source
soup = BeautifulSoup(page, 'lxml')
div = soup.find('div', class_='sections')
# print("*" * 200)
href_list = []
for div1 in div.find_all('div'):
    href = div1.find('a')['href']
    if href and 'http' not in href:
        href_list.append(base_url + href.split('/')[-2])

for l in href_list:
    resp = requests.get(l)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'lxml')
        divs = soup.find_all('div', class_='pgc-img')
        for div in divs:
            src = div.find('img')['src']
            print(src)
