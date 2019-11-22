import os

# print(os.getcwd())
# path = os.path.join(os.getcwd(), '123.txt')
# print(path)
# path = os.getcwd() +
# os.remove(path)
# os.close()
# os.close()
path = os.getcwd()  # 获取当前文件路径
# os.chdir(path)
# list = os.listdir()
# print(list)
# for l in list:
#     if '.txt' in l:
#         print(l)
#         os.remove(os.path.join(path, l))

# print(os._exists('demo1'))
# os.mkdir('demo1')  # 生成文件夹
# os.chdir('demo1')
# with open('123.txt', 'w') as f:
#     f.write('hello')
# os.rmdir('demo1')
# for l in os.listdir('demo1'):
#     os.chdir('demo1')
#     os.remove(l)
# os.chdir('./')
# os.rmdir('demo1')
# os.chdir('./huiqiantong')
os.chdir('../../huiqiantong')
print(os.getcwd())