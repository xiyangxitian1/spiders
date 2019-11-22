# -*- conding:utf-8 -*-


path_source1 = R'F:\tubian_leaf\凸变英雄LEAF 第1集.mp4'
path_source2 = r'F:\tubian_leaf\凸变英雄LEAF 第2集.mp4'
path_source3 = r'F:\tubian_leaf\凸变英雄LEAF 第3集.mp4'
path_dest = R'F:\tubian_leaf\a.mp4'

with open(path_source3, 'rb') as f:
    with open(path_dest, 'ab') as f1:
        f1.write(f.read())
