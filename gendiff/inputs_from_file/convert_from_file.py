import gendiff.inputs_from_file.convert_from_json as js
import gendiff.inputs_from_file.convert_from_yaml as yml

CONVERTERS = {
    '.json': js.load_json,
    '.yaml': yml.load_yaml,
    '.yml': yml.load_yaml}

"""Здесь я не совсем понял задание
'Как я уже говорил, эта функция может быть чистой и принимать
на вход содержимое файла в виде строки.
Вынесите извлечение содержимого в отдельную фукнцию'
я его понял как выделить чисто грузную функцию,
чтобы остальные остались читсенькими
"""


def extract_raw_data(file):
    with open(file) as f:
        data = f.read()
    return extract_data(data, file)


def extract_data(data, file):
    path = file.lower()
    for key in CONVERTERS:
        if path.endswith(key):
            return CONVERTERS[key](data)
    return {}
