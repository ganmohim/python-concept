"""The Hello World version of Python decorator.

This is a Python decorator at its simplest form.

Author: GAN MOHIM.
"""
def hello(func):
    def wrapper():
        print("Hello ", end='')
        return func()
    return wrapper


@hello
def world():
    print("World!")


if __name__ == "__main__":
    world()
