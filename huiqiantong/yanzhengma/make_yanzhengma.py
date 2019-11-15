'''
1. 画一张空白的画
2. 画底色，给每一个像素填充一个颜色，颜色随机 -- 函数
3. 往画上写字，字是随机的（函数），字的颜色也是随机的 （函数）
4. 保存图片

PIL 在py2.6以下可以用

pillow py3以上使用
pip install pillow
Pillow_PIL  现在用的是这个包
'''

import numpy as np
from PIL import Image, ImageDraw, ImageFont

mylist = []


def random_char():
    '''
    生成随机数
    unicode
    大写字母 65-90，小写字母97-122 数字 48-57
    汉字 19968-40895
    函数chr(65)=A
    :return:
    '''
    if len(mylist) == 0:
        mylist.extend([i for i in range(48, 58)])
        mylist.extend([i for i in range(65, 91)])
        mylist.extend([i for i in range(97, 123)])
        # mylist.extend([i for i in range(19968, 40895)]) 范围太大，会出现日本字等
        mylist.extend([i for i in range(19968, 20000)])
    index = np.random.randint(0, len(mylist))
    print(chr(mylist[index]))
    return chr(mylist[index])


def char_color() -> tuple:
    """生成一个随机的颜色"""
    return np.random.randint(10, 120), np.random.randint(10, 120), np.random.randint(10, 120)


def bg_color() -> tuple:
    '''
    随机生成背景色
    '''
    return np.random.randint(122, 255), np.random.randint(122, 255), np.random.randint(122, 255)


def gen_code():
    """
    1.画一张空白图片
    2.填充像素
    3.随机写4个字符
    4.保存图片
    :return:
    """
    # 画一张空白图片
    w, h = 200, 50
    image = Image.new('RGB', (w, h), (255, 255, 255))
    # 填充像素
    draw = ImageDraw.Draw(image)
    # 遍历像素点并且设置颜色
    for width in range(w):
        for height in range(h):
            draw.point((width, height), bg_color())
    # 随机写4个字符
    # 设置字体 C:\Windows\Fonts
    # 有些字体是显示不出来中文的 现在设置成黑体，就正常显示出来中文了
    myfont = ImageFont.truetype('simhei.ttf', 36, encoding='utf-8')
    for i in range(4):
        draw.text((50 * i + 10, 10), random_char(), fill=char_color(), font=myfont)
    # 保存图片
    image.save('code_new.jpg')


if __name__ == '__main__':
    gen_code()

