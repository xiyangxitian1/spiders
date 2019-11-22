# -*- conding:utf-8 -*-
import os

"""
需求：
遍历指定目录，完成以下操作
1.列出该目录下所有文件的名称及大小，
  文件大小用选择的方式显示（KB,MB,B)
2.找出该目录下最大和最小的文件，输出文件名及大小


"""
# 目录
dir_my = r'F:\BaiduNetdiskDownload\基础班预习视频\01-Python基础\01-Python基础'


def file_size(dir, KB=False, MB=False):
    size = os.path.getsize(dir)
    if KB:
        return str(round(size / 1024, 2)) + "KB"
    elif MB:
        return str(round(size / (1024 * 1024), 2)) + "MB"
    else:
        return str(size) + "B"


def list_all_file(path):
    if os.path.isdir(path):
        dirs = os.listdir(path)
        for dir in dirs:
            dir = os.path.join(path, dir)
            if os.path.isdir(dir):
                list_all_file(dir)
            else:
                print(dir, file_size(dir, True))


def get_all_files(path):
    files = {}
    get_files_list(path, files)
    return files


def get_files_list(path, files):
    if os.path.isdir(path):
        list = os.listdir(path)
        for l in list:
            l = os.path.join(path, l)
            if os.path.isdir(l):
                get_files_list(l, files)
            else:
                files[l] = file_size(l)
    else:
        files[path] = file_size(path)


if __name__ == '__main__':
    # list_all_file(dir_my)
    # print(os.path.join('a', 'b'))
    files = get_all_files(dir_my)
    print(files)
    max_file = max(files, key=lambda x: int(files[x][:-1]))
    print('max_file:{}:{}'.format(max_file, files[max_file]))
