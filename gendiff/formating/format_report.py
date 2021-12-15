import gendiff.formating.stylish as styl
import gendiff.formating.plain as plain
import gendiff.formating.json as jsn

CHOICES = {'stylish': styl.generate_stylish,
           'plain': plain.generate_plain,
           'json': jsn.generate_json}
DEFAULT_STYLE = 'stylish'


def generate_report(data, style):
    if style not in CHOICES.keys():
        return "not supported format"
    return(CHOICES[style](data))
