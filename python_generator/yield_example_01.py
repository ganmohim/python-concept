def func_gan():
    print('A')
    print('B')
    yield 1
    print('C')
    yield 2


if __name__ == "__main__":
    print(func_gan().__next__())
