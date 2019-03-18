import dictlib
import simplejson as json

from utils import create_recursion_dict


def my_sort(item):
    key, value = item
    return key[2:]


def make_diff_json(diff):
    DELIM = '__MY_DELIMITER__'

    gl_dict = {}
    for tuple_ in diff:
        sym, recursion_keys, value = tuple_
        recursion_keys = list(recursion_keys)
        recursion_keys[-1] = '{}{}{}'.format(sym, DELIM, recursion_keys[-1])
        recursion_keys = tuple(recursion_keys)
        d = create_recursion_dict(recursion_keys, value)

        gl_dict = dictlib.union(gl_dict, d)

    text = json.dumps(gl_dict,
                      indent=4,
                      sort_keys=True,
                      item_sort_key=my_sort
                      )

    text = text.replace('"-__MY_DELIMITER__', '- "')
    text = text.replace('"+__MY_DELIMITER__', '+ "')
    text = text.replace('" __MY_DELIMITER__', '+ "')
    text = text.replace('"', '')

    return text


if __name__ == '__main__':
    pass
