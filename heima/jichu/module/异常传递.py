try:
    f = open('123.txt', 'r')  # try里面的代码出现异常后，当前try内部后续代码不会执行
    # 而是执行它对应的except里的代码，及后面的代码
    try:
        content = f.read()
        print(content)
    except:
        print('文件不存在')
except:
    print('出现异常')
