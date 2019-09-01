"""Decorated function with parameters.

This is an example where the function we are going to
decorate has parameters.

Author: GAN MOHIM.
"""


def hello(func):
    def wrapper(*args, **kwargs):
        #print(func.__name__)
        print("Hello ", end='')
        return func(*args, **kwargs)
    return wrapper

@hello
def world(end_line='\n--The End--\n'):
    print("World!", end=end_line)


if __name__ == "__main__":
    world()
    #wrapper_world = hello(world)
    #wrapper_world(end_line = "Ma")