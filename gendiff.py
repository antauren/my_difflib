import sys

import difflib
import json

from utils import heandler

if __name__ == '__main__':
    args = sys.argv[1:]

    print(heandler(args))
