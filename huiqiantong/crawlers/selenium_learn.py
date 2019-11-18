from selenium import webdriver

url = 'https://www.toutiao.com/'
options = webdriver.ChromeOptions
options.binary_location = r"C:\Users\ly\AppData\Local\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(r'D:\ly\Python\Python37\chromedriver.exe')  #

# 会自动打开Chrome浏览器
# driver.maximize_window()
driver.get('https://www.toutiao.com/')
# driver.implicitly_wait(10)

print(driver.page_source)

