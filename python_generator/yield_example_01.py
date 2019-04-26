def func_gan():
    print('A')
    print('B')
    yield 1
    print('C')
    yield 2


if __name__ == "__main__":
    # func_gan()
    # print(next(func_gan()))
    # print(next(func_gan()))
    # print(list(func_gan()))
    i = 0
    for item in func_gan():
        print("@index: {}".format(i))
        print(item)
        i += 1

