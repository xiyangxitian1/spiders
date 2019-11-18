import requests
from bs4 import BeautifulSoup
import time

# url = 'http://p3.pstatp.com/large/pgc-image/e89813b24c544f849a36a9f6c714fbc5'
# resp = requests.get(url)
# print(resp)
# if resp.status_code == 200:
#     with open('2.jpg', 'wb') as f:
#         f.write(resp.content)

url = 'https://www.toutiao.com/a6760558441883763207/'
hd = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}
resp = requests.get(url, headers=hd)
time.sleep(5)
if resp.status_code == 200:
    print(resp.text)
    soup = BeautifulSoup(resp.text, 'lxml')

    divs = soup.find_all('div', class_='pgc-img')
    print(divs)
    for div in divs:
        src = div.find('img')['src']
        print(src)
