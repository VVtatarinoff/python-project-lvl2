from gendiff.compare_data.comparison_tree import ADD, DEL, KEPT, SPLIT

PLAIN_COMPARISON = {('follow', DEL): False,
                    ('host', KEPT): 'hexlet.io',
                    ('proxy', DEL): '123.234.53.22',
                    ('timeout', DEL): 50,
                    ('timeout', ADD): 20,
                    ('verbose', ADD): True}

COMPLEX_COMPARISON = {('common', SPLIT):
                      {('follow', ADD): False,
                       ('setting1', KEPT): 'Value 1',
                       ('setting2', DEL): 200,
                       ('setting3', DEL): True,
                       ('setting3', ADD): None,
                       ('setting4', ADD): 'blah blah',
                       ('setting5', ADD): {'key5': 'value5'},
                       ('setting6', SPLIT):
                       {('doge', SPLIT):
                        {('wow', DEL): '',
                        ('wow', ADD): 'so much'},
                        ('key', KEPT): 'value',
                        ('ops', ADD): 'vops'}},
                      ('group1', SPLIT):
                      {('baz', DEL): 'bas',
                       ('baz', ADD): 'bars',
                       ('foo', KEPT): 'bar',
                       ('nest', DEL):
                       {'key': 'value'},
                       ('nest', ADD): 'str'},
                      ('group2', DEL):
                      {'abc': 12345,
                       'deep': {'id': 45}},
                      ('group3', ADD):
                      {'deep':
                       {'id':
                        {'number': 45}},
                      'fee': 100500}}

HEXLET_COMPARISON = {('common', SPLIT): {('follow', ADD): False,
                     ('setting1', KEPT): 'Value 1',
                     ('setting2', DEL): 200,
                     ('setting3', DEL): True,
                     ('setting3', ADD): {'key': 'value'},
                     ('setting4', ADD): 'blah blah',
                     ('setting5', ADD): {'key5': 'value5'},
                     ('setting6', SPLIT):
                     {('doge', SPLIT):
                      {('wow', DEL): 'too much',
                       ('wow', ADD): 'so much'},
                      ('key', KEPT): 'value',
                      ('ops', ADD): 'vops'}},
                     ('group1', SPLIT):
                     {('baz', DEL): 'bas',
                      ('baz', ADD): 'bars',
                      ('foo', KEPT): 'bar',
                      ('nest', DEL): {'key': 'value'},
                      ('nest', ADD): 'str'},
                     ('group2', DEL):
                     {'abc': 12345, 'deep': {'id': 45}},
                     ('group3', ADD):
                     {'deep': {'id':
                      {'number': 45}}, 'fee': 100500},
                     ('group4', SPLIT):
                     {('default', DEL): None,
                      ('default', ADD): '',
                      ('foo', DEL): 0,
                      ('foo', ADD): None,
                      ('isNested', DEL): False,
                      ('isNested', ADD): 'none',
                      ('key', ADD): False,
                      ('nest', SPLIT):
                      {('bar', DEL): '',
                       ('bar', ADD): 0,
                       ('isNested', DEL): True},
                      ('someKey', ADD): True,
                      ('type', DEL): 'bas',
                      ('type', ADD): 'bar'}}
