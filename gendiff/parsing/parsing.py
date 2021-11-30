def get_differences(arg1, arg2): # noqa C901
    if not isinstance(arg1, dict):
        return arg1
    if not isinstance(arg2, dict):
        return arg2
    keys = sorted(list(arg1.keys() | arg2.keys()))
    if not keys:
        return {}
    dif_dict = {}
    for key in keys:
        if key not in arg1:
            dif_dict[(key, '+')] = get_differences({}, arg2[key])
        elif key not in arg2:
            dif_dict[(key, '-')] = get_differences(arg1[key], {})
        elif arg1[key] == arg2[key]:
            dif_dict[(key, ' ')] = get_differences(arg1[key], arg2[key])
        else:
            if isinstance(arg1[key], dict) and isinstance(arg2[key], dict):
                dif_dict[(key, "?")] = get_differences(arg1[key], arg2[key])
            else:
                dif_dict[(key, '-')] = get_differences(arg1[key], {})
                dif_dict[(key, '+')] = get_differences({}, arg2[key])
    return dif_dict


def parse_data(initial_data, modified_data):
    diff = get_differences(initial_data, modified_data)
    return diff
