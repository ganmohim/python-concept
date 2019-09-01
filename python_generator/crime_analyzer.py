"""
Shows usage of yield in reading long file content.


Author: GAN MOHIM.
"""
import logging
import types

from memory_profiler import profile

logger = logging.getLogger(__name__)


@profile
def read_file():
    with open('Crime_Data.csv') as file_obj:
        header = file_obj.readline().split(",")
        print("{:20} -- {:20} -- {:20}".format(
            header[1], header[5], header[-1]))
        for line in file_obj:
            line_parts = line.split(",")
            if line_parts[5] == 'HOMICIDE':
                print("{:20} -- {:20} -- {:20}".format(
                    line_parts[1], line_parts[5], line_parts[-1]))


def read_file_with_list():
    """Reading file using list.

    Not so effective implementation. Just used to
    show users how it impacts performance and uses
    more memories.

    :return: list containing all lines are returned.
    """
    with open('Crime_Data.csv') as file_obj:
        list_of_lines = file_obj.readlines()
        logger.debug("Size of list_of_lines: {}".format(len(list_of_lines)))
        return list_of_lines


def read_file_with_yield():
    """Reading file content using yield.

    :return:
    """
    with open("Crime_Data.csv") as file_obj:
        for line in file_obj:
            logger.debug("Type of line: {}".format(
                isinstance(line, types.GeneratorType)))
            yield line


@profile
def show_data(data_index, data_filter):
    count = 1

    print(">" * 78, end='\n\n')
    line_gen = read_file_with_yield()
    logger.debug("read_file_with_yield(): {}".format(
        isinstance(line_gen, types.GeneratorType)))
    for line in read_file_with_yield():
        if count == 1:
            header = line.split(",")
            print("{:20} -- {:20} -- {:20}".format(
                header[1], header[5], header[-1]))
        else:
            line_parts = line.split(",")
            if line_parts[data_index] == data_filter:
                print("{:20} -- {:20} -- {:20}".format(
                    line_parts[1], line_parts[5], line_parts[-1]))

        count += 1
        if count == 10:
            break
    print(">" * 78, end='\n\n')


if __name__ == "__main__":
    logger = logging.getLogger('root')
    log_formatter = "[%(lineno)s - %(funcName)10s() ] %(message)s"
    logging.basicConfig(format=log_formatter)
    logger.setLevel(logging.DEBUG)

    show_data(5, 'HOMICIDE')
