def gen1():
    for i in range(10):
        yield i


for i, v in enumerate(gen1()):
    print(i, v)
