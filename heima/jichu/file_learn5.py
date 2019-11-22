# 需求 123.txt [复件]123.txt
# 1.接收用户输入的文件名

file_name = input("请输入要要制作复件的文件名：")
# 2.拼接新的文件名字
index = file_name.rindex('.')  # rindex是从后往前找 index是从前往后找

new_file_name = file_name[:index] + "[复件]" + file_name[index:]

# 3.读取原文件 写入到复件文件中
with open(file_name, 'r', encoding='utf-8') as old_f:
    with open(new_file_name, 'w', encoding='utf-8') as new_f:
        content = old_f.read()  # 读取旧文件
        new_f.write(content)  # 把旧文件中的内容写入到新文件中
