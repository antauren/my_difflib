import simplejson as json


def my_sort(item: tuple) -> str:
    key, _ = item
    return key[2:]


def my_json_dumps(dict_: dict) -> str:
    text = json.dumps(dict_,
                      indent=4,
                      sort_keys=True,
                      item_sort_key=my_sort
                      )

    return text.replace('"', '')
