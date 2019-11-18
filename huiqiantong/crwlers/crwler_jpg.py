import requests

url = 'https://www.baidu.com/'
url = 'https://goss4.cfp.cn/creative/vcg/800/new/VCG211163010264.jpg?x-oss' \
      '-process=image/format,jpg/interlace,1'  # 一个图片的地址

resp = requests.get(url)  # 图片和视频返回给的是二进制数据
if resp.status_code == 200:
    with open('1.jpg', 'wb') as f:
        f.write(resp.content)
