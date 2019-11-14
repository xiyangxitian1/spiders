import os

files = {}

root_dir = r'D:\allfile'


def list_file(root_dir, KB=True, MB=False):
    if os.path.isfile(root_dir):
        size = file_size(root_dir, KB=KB, MB=MB)
        files[root_dir] = size
    else:
        for f in os.listdir(root_dir):
            file_path = os.path.join(root_dir, f)
            if os.path.isfile(file_path):
                size = file_size(file_path, KB=KB, MB=MB)
                files[file_path] = size
            else:
                list_file(file_path, KB)  # 递归


def file_size(file_path, KB=False, MB=False):
    size = os.path.getsize(file_path)  # bytes
    if KB:
        return str(round(size / 1024, 2)) + "KB"
    elif MB:
        return str(round(size / (1024 * 1024), 2)) + "MB"
    else:
        return str(size) + "B"


def max_min():
    max_file = max(files, key=lambda x: files[x])
    min_file = min(files, key=lambda x: files[x])
    return max_file, min_file


list_file(root_dir, KB=False)

max_file, min_file = max_min()
print('最大文件：', max_file, '文件大小：', files[max_file])
print('最小文件：', min_file, '文件大小：', files[min_file])
# for k, v in files.items():
#     print(k, v)

for root, dirs, files in os.walk(root_dir):
    print(root, "consumes", end="")
    print(sum([os.path.getsize(os.path.join(root, name)) for name in files]),
          end="")
    print("bytes in", len(files), "non-directory files")
