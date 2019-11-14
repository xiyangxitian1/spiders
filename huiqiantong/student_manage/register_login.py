"""
程序的结构
函数- 注册，登录，退出，显示菜单

变量类型-字典{'用户名':pwd}
数据结构，算法
"""

users = {}


def register():
    while True:
        username = input('请输入用户名：')
        pwd = input('请输入密码')
        if username in users.keys():
            print('用户名已存在，请重新输入')
            continue
        elif username.strip() == '' or pwd.strip() == '':
            print('用户名或密码不能为空，请重新输入！')
            continue
        else:
            break
    users[username] = pwd
    print('注册成功！')


def login():
    for i in range(3, 0, -1):
        username = input('请输入用户名：')
        pwd = input('请输入密码:')
        if username not in users.keys() or users[username] != pwd:
            print('您输入的用户名或密码不正确')
            if i >= 1:
                print('您还有%d次机会：' % (i - 1))
            continue
        else:
            print('登录成功！')
            break


def show_menu():
    """
    显示菜单
    """
    print('*' * 20, '注册：R/r', '*' * 20)
    print('*' * 20, '登录：L/l', '*' * 20)
    print('*' * 20, '退出：Q/q', '*' * 20)


if __name__ == '__main__':
    while True:
        show_menu()
        print('请选择你要进行的操作：')
        choice = input()
        if choice not in 'RrLlQq':
            print('您输入的指令有误，请重新输入!')
            continue
        elif choice in 'Rr':
            register()
        elif choice == 'L' or choice == 'l':
            login()
        elif choice in 'Qq':
            break
