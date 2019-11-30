import multiprocessing
import time


def sing():
    for _ in range(5):
        print('sing..')
        time.sleep(1)


def dance():
    for _ in range(5):
        print('dance...')
        time.sleep(1)


if __name__ == '__main__':
    sing_process = multiprocessing.Process(target=sing)
    dance_press = multiprocessing.Process(target=dance)
    sing_process.start()
    dance_press.start()
