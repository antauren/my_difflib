'''docstring'''  # TODO


def make_row(sym, key, value):
    '''pattern'''  # TODO
    return sym, key, value


def get_diff(before: dict, after: dict) -> list:
    '''diff'''  # TODO
    diff = []

    for key in set(before) | set(after):

        if key not in before:
            row = make_row('+', key, after[key])
            diff.append(row)

        elif key not in after:
            row = make_row('-', key, before[key])
            diff.append(row)

        elif before[key] == after[key]:
            row = make_row(' ', key, before[key])
            diff.append(row)

        else:
            row = make_row('-', key, before[key])
            diff.append(row)

            row = make_row('+', key, after[key])
            diff.append(row)

    return diff


if __name__ == '__main__':
    pass
