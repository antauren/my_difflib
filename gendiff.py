import sys

import difflib
import json

from utils import heandler, is_args_correct


def gendiff(file_1, file_2, format):
    return 'test "{}" "{}" "{}"'.format(file_1, file_2, format)


if __name__ == '__main__':
    args = sys.argv[1:]

    heandled_args = heandler(args)

    print(heandled_args)
