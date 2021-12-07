PLAIN1_RAW_DATA = {'host': 'hexlet.io',
                   'timeout': 50,
                   'proxy': '123.234.53.22',
                   'follow': False}

PLAIN2_RAW_DATA = {'timeout': 20,
                   'verbose': True,
                   'host': 'hexlet.io'}

COMPLEX1_RAW_DATA = {'common':
                     {'setting1': 'Value 1',
                      'setting2': 200,
                      'setting3': True,
                      'setting6':
                          {'key': 'value',
                           'doge': {'wow': ''}}},
                     'group1':
                         {'baz': 'bas',
                          'foo': 'bar',
                          'nest': {'key': 'value'}},
                     'group2':
                         {'abc': 12345,
                          'deep': {'id': 45}}}

COMPLEX2_RAW_DATA = {'common':
                     {'follow': False,
                      'setting1': 'Value 1',
                      'setting3': None,
                      'setting4': 'blah blah',
                      'setting5': {'key5': 'value5'},
                      'setting6':
                      {'key': 'value',
                       'ops': 'vops',
                       'doge': {'wow': 'so much'}}},
                     'group1':
                         {'foo': 'bar',
                          'baz': 'bars',
                          'nest': 'str'},
                     'group3':
                         {'deep':
                          {'id':
                           {'number': 45}},
                          'fee': 100500}}

PLAIN_COMPARISON = {('follow', '-'): False,
                    ('host', ' '): 'hexlet.io',
                    ('proxy', '-'): '123.234.53.22',
                    ('timeout', '-'): 50,
                    ('timeout', '+'): 20,
                    ('verbose', '+'): True}

COMPLEX_COMPARISON = {('common', '?'):
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
