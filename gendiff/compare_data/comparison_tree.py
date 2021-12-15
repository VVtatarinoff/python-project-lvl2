ADD = 'ADDED'
DEL = 'DELETED'
KEPT = 'NOT_CHANGED'
SPLIT = ' '
CHANGED = "UPDATED"

STATUS = 'status'
VALUE = 'value'
VALUE_INITIAL = 'value_inintial'
VALUE_MODIFIED = 'value_modified'


def is_dict(argument):
    return isinstance(argument, dict)


def create_comparison_tree(arg1, arg2): # noqa C901
    if not is_dict(arg1):
        return arg1
    if not is_dict(arg2):
        return arg2
    keys = sorted(list(arg1.keys() | arg2.keys()))
    dif_dict = {}
    for key in keys:
        if key not in arg1:
            dif_dict[key] = {STATUS: ADD, VALUE: arg2[key]}
        elif key not in arg2:
            dif_dict[key] = {STATUS: DEL, VALUE: arg1[key]}
        elif arg1[key] == arg2[key]:
            dif_dict[key] = {STATUS: KEPT, VALUE: arg1[key]}
        # случаи присутствия ключей в обоих словарях и
        # неравенства значений
        elif is_dict(arg1[key]) and is_dict(arg2[key]):
            dif_dict[key] = {STATUS: SPLIT,
                             VALUE: create_comparison_tree(arg1[key],
                                                           arg2[key])}
        else:
            dif_dict[key] = {STATUS: CHANGED,
                             VALUE_INITIAL: arg1[key],
                             VALUE_MODIFIED: arg2[key]}
    return dif_dict
