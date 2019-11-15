import requests

url = 'https://movie.douban.com/top250?start=300'
resp = requests.get(url)
print(resp.ok)
