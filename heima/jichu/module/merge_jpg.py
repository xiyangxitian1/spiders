with open('f:/1.jpg', 'rb') as f1:
    with open('f:/3.jpg', 'wb') as f2:
        f2.write(f1.read(1024 * 10+500))
        # with open('F:/2.jpg', 'rb') as f3:
        #     f2.write(f3.read(1024 * 9))
