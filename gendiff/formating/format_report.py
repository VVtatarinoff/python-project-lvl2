import gendiff.formating.stylish as styl


def generate_report(data, style=None):
    if style is None:
        return styl.generate_stylish_report(data)
