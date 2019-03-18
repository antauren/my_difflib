"""Usage: gendiff [options] <firstConfig> <secondConfig>

  Compares two configuration files and shows a difference.

  Options:

    -h, --help           output usage information
    -V, --version        output the version number
    -f, --format [type]  Output format
"""

import os

from docopt import docopt

from plain_diff import get_diff
from parsers import parse
from bfs_for_dict import make_plain_dict
from make_json import make_diff_json

if __name__ == '__main__':
    args = docopt(__doc__, version='gendiff 0.3')

    file_1, file_2 = args['<firstConfig>'], args['<secondConfig>']

    if not os.path.isfile(file_1):
        print('"{}" is not file'.format(file_1))
    elif not os.path.isfile(file_2):
        print('"{}" is not file'.format(file_2))

    else:
        before = parse(file_1)
        after = parse(file_2)

        pd1 = make_plain_dict(before)
        pd2 = make_plain_dict(after)

        diff = get_diff(pd1, pd2)

        text = make_diff_json(diff)

        print(text)
