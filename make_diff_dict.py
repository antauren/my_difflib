def make_new_key(operation: str, key: str) -> str:
    sym_dict = {'ADD': '+',
                'REMOVE': '-',
                'EQUAL': ' '
                }

    return '{} {}'.format(sym_dict[operation], key)


def make_diff_dict(before: dict, after: dict, diff: dict) -> dict:
    for key in set(before) | set(after):

        if (key in before) and (key not in after):
            new_key = make_new_key('REMOVE', key)
            diff[new_key] = before[key]

        elif (key not in before) and (key in after):
            new_key = make_new_key('ADD', key)
            diff[new_key] = after[key]

        elif (key in before) and (key in after) and (before[key] == after[key]):
            new_key = make_new_key('EQUAL', key)
            diff[new_key] = before[key]

        elif (not isinstance(before[key], dict)) or (not isinstance(after[key], dict)):
            new_key = make_new_key('REMOVE', key)
            diff[new_key] = before[key]

            new_key = make_new_key('ADD', key)
            diff[new_key] = after[key]

        else:
            new_key = make_new_key('EQUAL', key)
            diff[new_key] = make_diff_dict(before[key], after[key], {})

    return diff
