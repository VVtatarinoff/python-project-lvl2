import gendiff.formating.stylish as styl
import gendiff.formating.plain as plain

CHOICES = {None: styl.generate_stylish,
           'plain': plain.generate_plain}


def generate_report(data, style=None):
    if style not in CHOICES.keys():
        return "not supported format"
    return(CHOICES[style](data))
