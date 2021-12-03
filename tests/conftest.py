import os
import pytest


"""индексы 0 и 1 - входные файлы, 2 - целевой отчет в stylish, 3 - отчет json
3 - целевой отчет в plain, 4 - отчет json"""
FILES_AND_RESULTS = [['source_json/test01.json',
                      'source_json/test02.json',
                      'stylish/result00.txt',
                      'plain/plain00.txt',
                      'js_report/json00.txt'],
                     ['source_json/test11.json',
                      'source_json/test12.json',
                      'stylish/result10.txt',
                      'plain/plain10.txt',
                      'js_report/json10.txt'],
                     ['source_yml/test21.yml',
                      'source_yml/test22.yaml',
                      'stylish/result00.txt',
                      'plain/plain00.txt',
                      'js_report/json00.txt'],
                     ['source_yml/test31.yml',
                      'source_yml/test32.yaml',
                      'stylish/result10.txt',
                      'plain/plain10.txt',
                      'js_report/json10.txt'],
                     ['source_json/test11.json',
                      'source_yml/test32.yaml',
                      'stylish/result10.txt',
                      'plain/plain10.txt',
                      'js_report/json10.txt']]
# patterns data
PLAIN1 = {'host': 'hexlet.io',
          'timeout': 50,
          'proxy': '123.234.53.22',
          'follow': False}
PLAIN2 = {'timeout': 20,
          'verbose': True,
          'host': 'hexlet.io'}
COMPLEX1 = {'common':
            {'setting1': 'Value 1',
             'setting2': 200,
             'setting3': True,
             'setting6':
             {'key': 'value',
              'doge':
              {'wow': ''}}},
            'group1':
            {'baz': 'bas',
             'foo': 'bar',
             'nest':
             {'key': 'value'}},
            'group2':
            {'abc': 12345,
             'deep':
                {'id': 45}}}
COMPLEX2 = {'common':
            {'follow': False,
             'setting1': 'Value 1',
             'setting3': None,
             'setting4': 'blah blah',
             'setting5':
             {'key5': 'value5'},
             'setting6':
             {'key': 'value',
              'ops': 'vops',
              'doge':
              {'wow': 'so much'}}},
            'group1':
            {'foo': 'bar',
             'baz': 'bars',
             'nest': 'str'},
            'group3':
            {'deep':
             {'id':
              {'number': 45}},
             'fee': 100500}}
# Matching patterns and files
pattern_to_file = {'source_json/test01.json': PLAIN1,
                   'source_json/test02.json': PLAIN2,
                   'source_json/test11.json': COMPLEX1,
                   'source_json/test12.json': COMPLEX2,
                   'source_yml/test21.yml': PLAIN1,
                   'source_yml/test22.yaml': PLAIN2,
                   'source_yml/test31.yml': COMPLEX1,
                   'source_yml/test32.yaml': COMPLEX2}
# промежуточные деревья для двух сценариев:
PLAIN_COMPARE = {('follow', '-'): False,
                 ('host', ' '): 'hexlet.io',
                 ('proxy', '-'): '123.234.53.22',
                 ('timeout', '-'): 50,
                 ('timeout', '+'): 20,
                 ('verbose', '+'): True}
COMPLEX_COMPARE = {('common', '?'):
                   {('follow', '+'): False,
                    ('setting1', ' '): 'Value 1',
                    ('setting2', '-'): 200,
                    ('setting3', '-'): True,
                    ('setting3', '+'): None,
                    ('setting4', '+'): 'blah blah',
                    ('setting5', '+'):
                    {('key5', '+'): 'value5'},
                    ('setting6', '?'):
                    {('doge', '?'):
                    {('wow', '-'): '',
                     ('wow', '+'): 'so much'},
                     ('key', ' '): 'value',
                     ('ops', '+'): 'vops'}},
                   ('group1', '?'):
                   {('baz', '-'): 'bas',
                    ('baz', '+'): 'bars',
                    ('foo', ' '): 'bar',
                    ('nest', '-'):
                    {('key', '-'): 'value'},
                    ('nest', '+'): 'str'},
                   ('group2', '-'):
                   {('abc', '-'): 12345,
                    ('deep', '-'):
                    {('id', '-'): 45}},
                   ('group3', '+'):
                   {('deep', '+'):
                    {('id', '+'):
                    {('number', '+'): 45}},
                    ('fee', '+'): 100500}}


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)

# normalized_paths - абсолютные пути до проверочных файлов
# data_and_results - данные для сравнения в виде списков
# (два первых элемента), три последних - отчеты в разных
# выводимых форматах


@pytest.fixture(scope='session')
def get_test_data():
    normalized_paths = []
    data_and_results = []
    for check_data in FILES_AND_RESULTS:
        file_list = []
        data1 = pattern_to_file[check_data[0]]
        data2 = pattern_to_file[check_data[1]]
        result_list = [data1, data2]
        for index, file in enumerate(check_data):
            full_path = get_fixture_path(file)
            file_list.append(full_path)
            if index > 1:
                with open(full_path) as f:
                    report = f.read()
                    result_list.append(report)
        normalized_paths.append(file_list)
        data_and_results.append(result_list)
    return normalized_paths, data_and_results


@pytest.fixture(scope='session')
def get_plain_source_patterns():
    return PLAIN1, PLAIN2


@pytest.fixture(scope='session')
def get_complex_source_patterns():
    return COMPLEX1, COMPLEX2


@pytest.fixture(scope='session')
def get_plain_merging():
    return PLAIN_COMPARE


@pytest.fixture(scope='session')
def get_complex_merging():
    return COMPLEX_COMPARE
