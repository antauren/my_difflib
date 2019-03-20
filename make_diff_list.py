def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'

    elif isinstance(value, str):
        return "'{}'".format(value)

    else:
        return value


def make_diff_list(before: dict, after: dict, diff: list, parents: list) -> list:
    for key in set(before) | set(after):
        keys = parents + [key]

        new_key = "'{}'".format('.'.join(keys))

        if (key in before) and (key not in after):

            row = "Property {} was removed".format(new_key)
            diff.append(row)

        elif (key not in before) and (key in after):
            value = format_value(after[key])

            row = "Property {} was added with value: {}".format(new_key, value)
            diff.append(row)

        elif (key in before) and (key in after) and (before[key] == after[key]):
            pass

        elif (not isinstance(before[key], dict)) or (not isinstance(after[key], dict)):
            value1 = format_value(before[key])
            value2 = format_value(after[key])

            row = "Property {} was updated. From {} to {}".format(new_key, value1, value2)
            diff.append(row)

        else:
            diff.extend(
                make_diff_list(before[key], after[key], [], keys)
            )

    return diff
