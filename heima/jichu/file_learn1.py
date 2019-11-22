# -*- conding:utf-8 -*-
# 文件就是用来持久化数据（把数据 保存到硬盘）
# 文件基础操作
# 1 打开文件 2 关闭
# 文件操作模式 ： w:write写入  r：写入
# 1.打开文件
# f = open('123.txt', 'w')  # 用w模式 如果文件不存在，会自动创建此文件，如果存在会覆盖里面的内容
#
# 2.写入数据
# f.write('hello')
# 3.关闭文件    不关闭会  内存泄露  应该要释放的内存无法释放
# f.close()
"""文件操作的推荐方式"""
with open('123.txt', 'w') as f:
    f.write('python learn')
