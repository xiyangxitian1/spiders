from selenium import webdriver

###  安装selenium    pip install selenium
### webdriver 不同的浏览器有不同的驱动 ,需要下载浏览器对应的版本
# response = requests.get('https://www.toutiao.com/')
# print(response.text)
url = 'https://www.toutiao.com/'
driver = webdriver.Chrome()
driver.get(url)
# myinput = driver.find_element_by_css_selector('#kw')  # 定位一个元素
# myinput.send_keys('武汉军运会')  # 与元素发生交互
#
# mybtn = driver.find_element_by_css_selector('#form > span.bg.s_btn_wr')
# mybtn.click()  # 点击百度一下

page = driver.page_source
print(page)
