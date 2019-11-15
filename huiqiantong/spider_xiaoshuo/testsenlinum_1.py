from selenium import webdriver

params = {
    'tn': 'resultjson_com',
    'ipn': 'rj',
    'ct': 201326592,
    'fp': 'result',
    'queryWord': '皮卡丘图片',
    'cl': 2,
    'lm': -1,
    'ie': 'utf-8',
    'oe': 'utf-8',
    'st': -1,
    'word': '皮卡丘图片',
    'face': 0,
    'istype': 2,
    'nc': 1,
    'pn': 0,
    'rn': 30,
}

hd = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
}

base_url = 'http://image.baidu.com'
browser = webdriver.Chrome(executable_path=r'D:\ly\Python37_64\chromedriver.exe')
search_url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1573838278577_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E7%9A%AE%E5%8D%A1%E4%B8%98%E5%9B%BE%E7%89%87&f=3&oq=%E7%9A%AE&rsp=2'
browser.get(search_url)
print(browser.page_source)
# selector = Selector(text=browser.page_source)
# divs = selector.css('.imgpage')
# for div in divs:
#     urls = div.css('li a::attr(href)').extract()
# for url in urls:
#     now_url = base_url + url
# print(now_url)
# resp = requests.get(now_url, headers=hd)

browser.quit()  # 退出模拟浏览器
