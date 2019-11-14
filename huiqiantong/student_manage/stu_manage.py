"""
学生信息管理系统
"""

students = {}


def showMenu():
    print("************学生管理系统***********")
    print('1.添加学生信息')
    print('2.删除学生信息')
    print('3.修改学生信息')
    print('4.查询学生信息')
    print('5.所有学生信息')
    print('6.退出系统')
    print('*' * 34)


def addStu():
    stuID = input('请输入学生的学号(学号必须唯一):')
    while stuID in students.keys():
        stuID = input('你输入的学号已经存在！请重新输入:')
    name = input('请输入学生的姓名：')
    students[stuID] = name


def deleteStu():
    stuID = input('请输入要删除的学生的学号:')
    while stuID not in students.keys():
        stuID = input('该学号不存在，请重新输入:')

    del (students[stuID])
    print('删除成功')


def updateStu():
    stuID = input('请输入要修改的学生的学号：')
    while stuID not in students.keys():
        stuID = input('该学号不存在，请重新输入:')
    name = input('请输入修改后的名字:')
    students[stuID] = name
    print('修改成功')


def queryStu():
    stuID = input('请输入要查询的学号:')
    if stuID in students.keys():
        print('学号：{}，姓名：{}'.format(stuID, students[stuID]))
    else:
        print('要查询的学生不存在！')


def showAll():
    print('当前系统中有以下学生：')
    for stuID in students:  # 等同于 students.keys()
        print('{}:{}'.format(stuID, students[stuID]))


def exitStu():
    print("操作结束，退出系统")
    return 'exit'


switch = {
    1: addStu,
    2: deleteStu,
    3: updateStu,
    4: queryStu,
    5: showAll,
    6: exitStu,
}

while True:
    showMenu()
    str1 = input('请选择你要进行的操作：')
    if str1.isdigit() == False:
        print('你输入的不正确,请重新输入')
        continue
    choice = int(str1)
    if choice not in (1, 2, 3, 4, 5, 6):
        print('你输入的不正确,请重新输入')
        continue
    result = switch[choice]()
    if result == 'exit':
        break
