def is_dict(argument):
    return isinstance(argument, dict)


def parse_data(arg1, arg2): # noqa C901
    if not is_dict(arg1):
        return arg1
    if not is_dict(arg2):
        return arg2
    keys = sorted(list(arg1.keys() | arg2.keys()))
    if not keys:
        return {}
    dif_dict = {}
    for key in keys:
        if key not in arg1:
            dif_dict[(key, '+')] = parse_data({}, arg2[key])
        elif key not in arg2:
            dif_dict[(key, '-')] = parse_data(arg1[key], {})
        elif arg1[key] == arg2[key]:
            dif_dict[(key, ' ')] = parse_data(arg1[key], arg2[key])
        else:
            if is_dict(arg1[key]) and is_dict(arg2[key]):
                dif_dict[(key, "?")] = parse_data(arg1[key], arg2[key])
            else:
                dif_dict[(key, '-')] = parse_data(arg1[key], {})
                dif_dict[(key, '+')] = parse_data({}, arg2[key])
    return dif_dict
