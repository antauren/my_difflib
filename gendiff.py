"""Usage: gendiff [options] <firstConfig> <secondConfig>

  Compares two configuration files and shows a difference.

  Options:

    -h, --help           output usage information
    -V, --version        output the version number
    -f, --format [type]  Output format
"""

import os

from docopt import docopt
from parsers import parse
from my_json_dumps import my_json_dumps
from make_diff_dict import make_diff_dict

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

        diff = make_diff_dict(before, after, {})

        pretty = my_json_dumps(diff)

        print(pretty)
