# import os
# from bs4 import BeautifulSoup
#
# rootPath = 'F:/EnglishWord/'
#
# list = []
# if os.path.isdir(rootPath):
#     # print('true')
#     list = os.listdir(rootPath)
#
#
list = ['Chapter-1-page-1.html', 'Chapter-1-page-10.html',
        'Chapter-1-page-2.html', 'Chapter-1-page-3.html']


def sortList(list):
    result = []
    dict = {}
    for l in list:
        splits = str(l).split('-')
        # print(splits)
        num1 = splits[1]
        num2 = splits[3].split('.')[0]
        num = 0
        if int(num2) < 10:
            num = int(str(num1) + '0' + str(num2))
        else:
            num = int(str(num1) + str(num2))
        dict[num] = l

    sorted(dict)
    print(dict)


def getNum(l):
    splits = str(l).split('-')
    # print(splits)
    num1 = splits[1]
    num2 = splits[3].split('.')[0]
    num = 0
    if int(num2) < 10:
        num = int(str(num1) + '0' + str(num2))
    else:
        num = int(str(num1) + str(num2))
    return num


if __name__ == '__main__':
    print(list)
    list.sort(key=lambda l: getNum(l))
    print(list)
