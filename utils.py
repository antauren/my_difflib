def create_dict(key, value):
    dict_ = {}
    dict_[key] = value

    return dict_


def create_recursion_dict(recursion_keys, value):
    keys_list = list(recursion_keys)

    # keys_list = recursion_keys.split('.')

    dict_ = {keys_list.pop(): value}

    for k in reversed(keys_list):
        dict_ = create_dict(k, dict_)
    return dict_





if __name__ == '__main__':
    # dict_ = create_recursion_dict('common.setting6.ops', 'vops')
    dict_ = create_recursion_dict(
        ('common', 'setting6', 'ops'), 'vops'
    )
    print(dict_)
