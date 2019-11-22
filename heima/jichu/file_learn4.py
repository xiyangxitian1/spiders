# path = r'F:\1.jpg'
# dest = r'f:/2.jpg'
# # 说明readlineb也可以操作二进制数据
# # 图片视频这种都可以
# f2 = open(dest, 'wb')
# with open(path, 'rb') as f:
#     while True:
#         a = f.readline()
#         if len(a) > 0:
#             f2.write(a)
#             f2.flush()
#         else:
#             break
# f2.close()
with open('123.txt', 'r', encoding='utf-8') as f:
    content = f.readline()
    print(content, end='')
