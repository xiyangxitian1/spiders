import gevent.monkey

gevent.monkey.patch_all()
from gevent.pool import Pool as gevent_pool

import time
import random


def add(a, b):
    ret = a + b
    print(ret)


if __name__ == '__main__':

    pool = gevent_pool(10)
    for i in range(10):
        a = random.randint(0, i)
        b = random.randint(a, a + i)
        pool.apply_async(func=add, args=(a, b))

    pool.join()

# pool.join()
# time.sleep(10)
