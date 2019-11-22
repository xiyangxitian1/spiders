# 方式一
# import module
#
# module.func()
#
# # print(module.Dog())
# dog = module.Dog()
#
# print(dog)

# 方式二
# 优点：可以导入模块中局部的东西，
# 缺点：如果导入的模块中有相同名的变量或函数 类  后导入的会覆盖前面导入的
# from module import count, Dog
# import module
#
# # 使用模块  不需要再写模块名了
# # module.func()
# print(module.count)  # 虽然显示有错，但是已经是导入的，运行时可以使用

# import huiqiantong
import sys

print(sys.path)  # 获取解析器可以导入的包
# 可以手动添加
sys.path.append('')  #
