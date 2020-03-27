from multiprocessing.dummy import Pool
import random


def add(a, b):
    ret = a + b
    print(ret)


if __name__ == '__main__':

    pool = Pool(2)
    for i in range(10):
        a = random.randint(0, i)
        b = random.randint(a, a + i)
        pool.apply_async(func=add, args=(a, b))

    pool.close()
    pool.join()
