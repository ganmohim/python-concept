import operator
import time

#from memory_profiler import profile


def data_selector(data, selector):
    """Select data based on map


    :param data:
    :param selector:
    :return:
    """
    selected_data = [data_item
                     for data_item, selector_item in zip(data, selector)
                     if selector_item]
    return selected_data


def drop_until_true(data, filter_func):
    data_iter = iter(data)
    for item in data_iter:
        if not filter_func(item):
            yield item
            break

    for item in data_iter:
        yield item


def drop_until_true_slow(data, filter_func):
    item_list = []
    for item in data:
        if filter_func(item):
            continue
        else:
            item_list.append(item)
    return item_list


def accumulate(numbers, math_operator):
    """Running total

    >>> list(accumulate([10, 20, 30, 40, 50], operator.add))
    [10, 30, 60, 100, 150]

    >>> list(accumulate([10, 20, 30, 40, 50], operator.mul))
    [10, 200, 6000, 240000, 12000000]


    :param numbers:
    :param math_operator:
    :return:
    """
    data_iter = iter(numbers)

    total = next(data_iter)
    yield total

    for item in data_iter:
        total = math_operator(total, item)
        yield total


def map(func, iterable):
    for iter_item in iterable:
        yield func(iter_item)


def starmap(func, iterable):
    for iter_item in iterable:
        yield func(*iter_item) # power_func(a, b)



if __name__ == "__main__":
    ##################################################
    # Test data_selector()
    # Here we only select odd numbers
    ##################################################
    data = [1, 2, 3, 4, 5, 6]
    selector = [1, 0, 1, 0, 1, 0]
    #print("Selected data is: {}".format(data_selector(data, selector)))

    ##################################################
    # Test drop_until_true()data = [1, 2, 3, 4, 5, 6]
    # Here we only select number greater than 10
    # Try rang ending at 100000
    ##################################################
    data = list(range(1, 100000))
    start_time = time.time()
    result = drop_until_true_slow(data, lambda x: x < 50)
    end_time = time.time()
    # print("Execution Time: '{}".format(end_time - start_time))
    #
    # print(list(result))

    ##################################################
    # Finding incremental math ops (add or mul)
    #
    ##################################################
    data = [10, 20, 30, 40, 50]
    result = accumulate(data, operator.add)
    # print(list(result))

    ##################################################
    # Custom map functions
    ##################################################
    numbers = [1, 2, 3, 4, 5]

    def square(num):
        return num * 2

    print(list(map(square, numbers)))

    ##################################################
    # Custom starmap functions
    ##################################################
    number_tuples = [(2, 3), (3, 2), (4, 3), (5, 3)]

    def power_func(num, power):
        return pow(num, power)

    print(list(starmap(power_func, number_tuples)))





