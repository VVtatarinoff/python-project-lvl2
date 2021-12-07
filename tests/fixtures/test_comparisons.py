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

HEXLET_COMPARISON = {('common', '?'):
                     {('follow', '+'): False,
                      ('setting1', ' '): 'Value 1',
                      ('setting2', '-'): 200,
                      ('setting3', '-'): True,
                      ('setting3', '+'):
                         {('key', '+'): 'value'},
                      ('setting4', '+'): 'blah blah',
                      ('setting5', '+'):
                          {('key5', '+'): 'value5'},
                      ('setting6', '?'):
                          {('doge', '?'):
                           {('wow', '-'): 'too much',
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
                          ('fee', '+'): 100500},
                     ('group4', '?'):
                         {('default', '-'): None,
                          ('default', '+'): '',
                          ('foo', '-'): 0,
                          ('foo', '+'): None,
                          ('isNested', '-'): False,
                          ('isNested', '+'): 'none',
                          ('key', '+'): False,
                          ('nest', '?'):
                              {('bar', '-'): '',
                               ('bar', '+'): 0,
                               ('isNested', '-'): True},
                          ('someKey', '+'): True,
                          ('type', '-'): 'bas',
                          ('type', '+'): 'bar'}}