# -*- conding:utf-8 -*-
# with open(r'F:\python_file\a.txt', 'w')as f:
#     f.write('python')

# 复制一个视频
path_source1 = R'F:\tubian_leaf\凸变英雄LEAF 第1集.mp4'
path_source2 = r'F:\tubian_leaf\凸变英雄LEAF 第2集.mp4'
path_dest = R'F:\tubian_leaf\a.mp4'
# 把两个视频合并成一个

buf = 1024
f1 = open(path_source2, 'rb')
fw = open(path_dest, 'wb')
with open(path_source1, 'rb') as f:
    a1 = f.read()
    fw.write(a1)
    fw.flush()
a2 = f1.read()
fw.write(a2)
fw.flush()
fw.close()
f1.close()
