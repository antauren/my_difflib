import sys

from utils import heandler, is_args_correct, json_load  # TODO
from step2 import get_diff


def gendiff(file_1, file_2, format):
    return 'test "{}" "{}" "{}"'.format(file_1, file_2, format)


if __name__ == '__main__':

    args = sys.argv[1:]
    heandled_args = heandler(args)

    file_1, file_2 = heandled_args[:2]

    before = json_load(file_1)
    after = json_load(file_2)

    for row in get_diff(before, after):
        print(row)
