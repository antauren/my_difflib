from collections import deque


def make_plain_dict(dict_: dict) -> dict:
    '''

    :param dict_:
    :return:
    '''

    plain_dict = {}

    for parent_key in dict_:
        key_value = [parent_key], dict_[parent_key]
        queue = [key_value]
        queue = deque(queue)

        while queue:
            k_list, current_value = queue.popleft()

            if not isinstance(current_value, dict):
                k_tuple = tuple(k_list)
                plain_dict[k_tuple] = current_value

            else:
                for key in current_value:
                    keys_value = k_list + [key], current_value[key]
                    queue.append(keys_value)

    return plain_dict


if __name__ == '__main__':
    pass
