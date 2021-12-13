ADD = '+'
DEL = '-'
KEPT = ' '
SPLIT = '?'


def is_dict(argument):
    return isinstance(argument, dict)


"""
Итог функции - промежуточные данные, используемые для построения отчета
По сути - объединение двух словарей, получается древовидная структура
В объединенном словаре в качестве ключа выступает tuple, первое значение - ключ
из источника, второе значение - символ, означающий
'+' - ключа не было в первом источнике, либо значение изменилось
'-' - ключа не было во втором источнике, либо значение изменилось

Таким образом, если ключ сохранился, но значение изменилось, в результирующем
дереве получаются две сущности (с минусом и с плюсом)
' ' - ключи и значения совпадают
'?' - специальный случай: ключи совпадают, но значение и в первом и
        во втором массиве данных - сами являются словарями. Таким образом,
        это раздвоение
Логика символов повторяет stylish отчет, но легко используется для других
отчетов

"""


def create_comparison_tree(arg1, arg2): # noqa C901
    if not is_dict(arg1):
        return arg1
    if not is_dict(arg2):
        return arg2
    keys = sorted(list(arg1.keys() | arg2.keys()))
    dif_dict = {}
    for key in keys:
        if key not in arg1:
            dif_dict[(key, ADD)] = arg2[key]
        elif key not in arg2:
            dif_dict[(key, DEL)] = arg1[key]
        elif arg1[key] == arg2[key]:
            dif_dict[(key, KEPT)] = arg1[key]
        else:
            if is_dict(arg1[key]) and is_dict(arg2[key]):
                dif_dict[(key, SPLIT)] = create_comparison_tree(arg1[key],
                                                                arg2[key])
            else:
                dif_dict[(key, DEL)] = arg1[key]
                dif_dict[(key, ADD)] = arg2[key]
    return dif_dict
