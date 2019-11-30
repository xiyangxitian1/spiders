import multiprocessing
import os


def task1():
    print('p:', os.getpid(), os.getppid())
    print('task1')
    process = multiprocessing.Process(target=task2)
    process.start()


def task2():
    print('task2')
    print('p2:', os.getpid(), os.getppid())


if __name__ == '__main__':
    p = multiprocessing.Process(target=task1)
    p.start()
    print('main:', os.getpid(), os.getppid())
