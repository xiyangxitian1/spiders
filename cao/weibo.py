import requests

url = 'http://f.video.weibocdn.com/001nJ054lx07yHEKMPqU01041201Sbj70E010.mp4?label=mp4_720p&template=864x486.25.0&trans_finger=1f0da16358befad33323e3a1b7f95fc9&Expires=1582539171&ssig=xN2afUF9PV&KID=unistore,video'

resp = requests.get(url)


print(resp.status_code)
if resp.status_code == "200":
    content = resp.content
    print(len(content))
    with open('1.mp4', 'wb') as file:
        file.write(content)

    print("success")
