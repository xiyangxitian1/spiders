# 尽量避免程序出错
path = input('请输入文件路径:')
# 如果用了try语法，后面必须要跟except或finally,else可以不写
try:
    # print(a)
    with open(path, 'r') as f:
        content = f.read()
        print(content)
except NameError as error:
    print('提示：%s ' % error)
except FileNotFoundError:  # 只拦截文件未找到的错误
    print('文件未找到')
except Exception as error:
    print(error)
else:
    print('如果try里面的代码下执行，没有出错就会走else')
finally:
    print('finally  不管有没有出错，都会执行')

print('后续处理')
