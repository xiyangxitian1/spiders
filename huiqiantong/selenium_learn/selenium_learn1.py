from bs4 import BeautifulSoup
from selenium import webdriver

###  安装selenium    pip install selenium
### webdriver 不同的浏览器有不同的驱动 ,需要下载浏览器对应的版本
# response = requests.get('https://www.toutiao.com/')
# print(response.text)
url = 'https://www.toutiao.com/'
url = 'https://www.baidu.com/'
driver = webdriver.Chrome()
driver.get(url)
myinput = driver.find_element_by_css_selector('#kw')  # 定位一个元素
myinput.send_keys('武汉军运会')  # 与元素发生交互

mybtn = driver.find_element_by_css_selector('#form > span.bg.s_btn_wr')
mybtn.click()  # 点击百度一下

##  Keys Keys.ENTER 回车
# 保存截图
# time.sleep(5)
# driver.save_screenshot('juyunhui.png')  # phantonJS 无界面浏览器
# myinput.clear()
# driver.back()
# time.sleep(5)
# driver.forward()
# driver.execute_script('window.open()')  # 执行javascript脚本
# driver.switch_to.window(driver.window_handles[1])  # 切换到相应的窗口
# driver.get('https://www.toutiao.com/')
# driver.close()
# driver.switch_to.window(driver.window_handles[0])
driver.get('https://www.toutiao.com/')
page = driver.page_source
print(page)
soup = BeautifulSoup(page, 'lxml')
news_zone = soup.find('div', attrs={'class': 'feed-infinite-wrapper'})
# print(news_zone)

# for news in news_list:
#     print(news)
#     title = news.find('a', attrs={'class': 'link'})
#     if title:
#         title = title.get_text()
#     print(title)
#     print('*'*50)




