# 定位 就是光标所在位置
with open('123.txt', 'w+') as f:
    print(f.tell())  # 获取定位
    f.write('hello')
    print(f.tell())  # 获取定位
    f.seek(3, 0)  # 改变文件定位  光标所在位置  在python3  whence只能是0
    print(f.read())
"""
seek  用来改变文件中光标的所在位置
offset 以当前定位whence 去偏移的字节数 
编码不一样 偏移不一样 特别是汉字编码

whence 0表示移到的文件开头，1表示定位不变，2表示移动到尾部

Python3中 如果whence它的值不是0的时候 offset只能是0  中有在文件开头时才能用偏移

"""

