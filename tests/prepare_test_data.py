import os


"""индексы 0 и 1 - входные файлы, 2 - целевой отчет в stylish 
3 - целевой отчет в plain"""
FILES_AND_RESULTS = [['test01.json', 'test02.json', 'result00.txt', 'plain00.txt'],
                     ['test11.json', 'test12.json', 'result10.txt', 'plain10.txt'],
                     ['test21.yml', 'test22.yaml', 'result00.txt', 'plain00.txt'],
                     ['test31.yml', 'test32.yaml', 'result10.txt', 'plain10.txt'],
                     ['test11.json', 'test32.yaml', 'result10.txt', 'plain10.txt']]
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
pattern_to_file = {'test01.json': PLAIN1,
                   'test02.json': PLAIN2,
                   'test11.json': COMPLEX1,
                   'test12.json': COMPLEX2,
                   'test21.yml': PLAIN1,
                   'test22.yaml': PLAIN2,
                   'test31.yml': COMPLEX1,
                   'test32.yaml': COMPLEX2}

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

def get_test_data():
    normalized_paths = []
    data_and_results = []
    for check_data in FILES_AND_RESULTS:
        normalized_paths.append([get_fixture_path(check_data[0]),
                                 get_fixture_path(check_data[1]),
                                 get_fixture_path(check_data[2]),
                                 get_fixture_path(check_data[3])])
        with open(normalized_paths[-1][2]) as file:
            result_stylish = file.read()
        with open(normalized_paths[-1][3]) as file:
            result_plain = file.read()
        data1 = pattern_to_file[check_data[0]]
        data2 = pattern_to_file[check_data[1]]
        data_and_results.append([data1, data2, result_stylish, result_plain])
    return normalized_paths, data_and_results