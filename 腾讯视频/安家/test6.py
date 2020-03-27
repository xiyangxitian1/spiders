# from multiprocessing.dummy import Pool
import random
from concurrent.futures import ThreadPoolExecutor


def add(a, b):
    ret = a + b
    print(ret)
    return ret


if __name__ == '__main__':

    with ThreadPoolExecutor(3) as t:
        for i in range(10):
            a = random.randint(0, i)
            b = random.randint(a, a + i)
            t.submit(add, a, b)
            # print(task1.result())

    # t.shutdown()
    print("OK")
