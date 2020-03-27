import os


def merge_file(path, title):
    os.chdir(path)
    cmd = 'copy /b *.ts new.tmp'
    os.system(cmd)
    os.system('del /Q *.ts')
    os.rename('new.tmp', title + '.mp4')


if __name__ == '__main__':
    # path = r'F:\tubian_leaf'
    path = r"F:\temp\安家\52"
    merge_file(path, "52集")
