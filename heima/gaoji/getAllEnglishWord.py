import os
from bs4 import BeautifulSoup

rootPath = 'F:/EnglishWord/'

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


list = []
if os.path.isdir(rootPath):
    # print('true')
    list = os.listdir(rootPath)
    list.sort(key=lambda l: getNum(l))
    # list.sort()
    # print(list)

# dict = {}
f1 = open('words.txt', 'w', encoding='utf-8')

for path in list:
    f1.write('\n{}\n'.format(path))
    path = rootPath + path
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
        soup = BeautifulSoup(c, features='lxml')
        # print(c)
        tbody = soup.find('tbody')
        # print(tbody)
        trs = tbody.find_all('tr')
        for tr in trs:
            tds_title = tr.find_all('td', class_='span2')
            tds_words = tr.find_all('td', class_='span10')
            title = tds_title[0].get_text()
            word = tds_words[0].get_text()
            word = word.replace('\n', ' ')
            # dict[title] = word
            f1.write('{:<20s}'.format(title) + ":" + word + '\n')
            # for td in tds:
            #     print(td.get_text())
            #     print('*****************************')
    # print(dict)
f1.close()


