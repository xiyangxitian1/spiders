# coding:utf-8
# with open('123.txt', 'w+', encoding='utf-8') as f:
#     f.write('李炎的python学习')
# with open('123.txt', 'r+') as f:
#     a = f.read()
#     print(type(a))
#     f.write(a)

with open('123.txt', 'w', encoding='utf-8') as f:
    f.write('你好啊')  # 中文简体编码是GBK 繁体BIG5
    # 所以现在写入用的GBK  再用pycharm打开是用utf-8打开就会乱码
