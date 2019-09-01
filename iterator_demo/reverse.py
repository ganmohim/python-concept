"""
Reverse a list using iterator protocol.


Author: GAN MOHIM.
"""


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        #print(self.data[self.index])
        return self.data[self.index]


if __name__ == "__main__":
    name_list = ['gan', 'ann', 'bob']
    reverse = Reverse(name_list)
    # list(reverse)

    # iter_obj = iter(reverse)
    # next(iter_obj)
    # next(iter_obj)
    # next(iter_obj)
    # next(iter_obj)

    for i in Reverse(name_list):
        print(i)
