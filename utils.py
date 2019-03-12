import os

with open('help.txt') as f:
    HELP_TEXT = f.read()

VERSION = 'version 0.01'
FORMAT = 'json'


def gendiff(file_1, file_2, format=FORMAT):
    return 'test "{}" "{}" "{}"'.format(file_1, file_2, format)


def is_args_correct(file_1, file_2, format=FORMAT):
    if not os.path.isfile(file_1):
        print('"{}" is not file'.format(file_1))

        return False

    if not os.path.isfile(file_2):
        print('"{}" is not file'.format(file_2))

        return False

    if format not in {'json', 'plain'}:
        print('format {} is not correct'.format(format))

        return False

    return True


def heandler(args):
    if not args:
        return HELP_TEXT

    if len(args) == 1:  # gendiff -V
        option = args[0]
        if option in {'-h', '--help'}:
            return HELP_TEXT

        elif option in {'-V', '--version'}:
            return VERSION

        else:
            return HELP_TEXT

    elif len(args) == 2:  # gendiff first-config.ini second-config.ini
        file_1, file_2 = args

        if not is_args_correct(file_1, file_2):
            return None

        return gendiff(file_1, file_2)

    elif len(args) == 4:  # gendiff --format plain first-config.ini second-config.ini
        option, format, file_1, file_2 = args

        if option not in {'-f', '--format'}:
            return HELP_TEXT

        option, format, file_1, file_2 = args

        if not is_args_correct(file_1, file_2, format):
            return None

        return gendiff(file_1, file_2, format)

    else:
        return HELP_TEXT


if __name__ == '__main__':
    pass
