from gendiff.compare_data.comparison_tree import ADD, DEL, KEPT, SPLIT, CHANGED

PLAIN_COMPARISON = {'follow':
                    {'status': DEL,
                     'value': False},
                    'host':
                    {'status': KEPT,
                     'value': 'hexlet.io'},
                    'proxy':
                    {'status': DEL,
                     'value': '123.234.53.22'},
                    'timeout':
                    {'status': CHANGED,
                     'value_inintial': 50,
                     'value_modified': 20},
                    'verbose':
                    {'status': ADD,
                     'value': True}}

COMPLEX_COMPARISON = {'common':
                      {'status': SPLIT,
                       'value':
                       {'follow':
                        {'status': ADD,
                         'value': False},
                        'setting1':
                        {'status': KEPT,
                         'value': 'Value 1'},
                        'setting2':
                        {'status': DEL,
                         'value': 200},
                        'setting3':
                        {'status': CHANGED,
                         'value_inintial': True,
                         'value_modified': None},
                        'setting4':
                        {'status': ADD,
                         'value': 'blah blah'},
                        'setting5':
                        {'status': ADD,
                         'value':
                         {'key5': 'value5'}},
                        'setting6':
                        {'status': SPLIT,
                         'value':
                         {'doge':
                          {'status': SPLIT,
                           'value':
                           {'wow':
                            {'status': CHANGED,
                             'value_inintial': '',
                             'value_modified': 'so much'}}},
                          'key':
                          {'status': KEPT,
                           'value': 'value'},
                          'ops':
                          {'status': ADD,
                           'value': 'vops'}}}}},
                      'group1':
                      {'status': SPLIT,
                          'value':
                          {'baz':
                           {'status': CHANGED,
                            'value_inintial': 'bas',
                            'value_modified': 'bars'},
                           'foo':
                           {'status': KEPT,
                            'value': 'bar'},
                           'nest':
                           {'status': CHANGED,
                            'value_inintial':
                            {'key': 'value'},
                            'value_modified': 'str'}}},
                      'group2':
                      {'status': DEL,
                       'value':
                       {'abc': 12345,
                        'deep':
                        {'id': 45}}},
                      'group3':
                      {'status': ADD,
                       'value':
                       {'deep':
                        {'id':
                         {'number': 45}},
                        'fee': 100500}}}

HEXLET_COMPARISON = {'common':
                     {'status': SPLIT,
                      'value':
                      {'follow':
                       {'status': ADD,
                        'value': False},
                       'setting1':
                       {'status': KEPT,
                        'value': 'Value 1'},
                       'setting2':
                       {'status': DEL,
                        'value': 200},
                       'setting3':
                       {'status': CHANGED,
                        'value_inintial': True,
                        'value_modified':
                        {'key': 'value'}},
                       'setting4':
                       {'status': ADD,
                        'value': 'blah blah'},
                       'setting5':
                       {'status': ADD,
                        'value':
                        {'key5':
                         'value5'}},
                       'setting6':
                           {'status': SPLIT,
                            'value':
                            {'doge':
                             {'status': SPLIT,
                              'value':
                              {'wow':
                               {'status': CHANGED,
                                'value_inintial': 'too much',
                                'value_modified': 'so much'}}},
                             'key':
                             {'status': KEPT,
                              'value': 'value'},
                             'ops':
                             {'status': ADD,
                              'value': 'vops'}}}}},
                     'group1':
                     {'status': SPLIT,
                      'value':
                      {'baz':
                       {'status': CHANGED,
                        'value_inintial': 'bas',
                        'value_modified': 'bars'},
                       'foo':
                       {'status': KEPT,
                        'value': 'bar'},
                       'nest':
                       {'status': CHANGED,
                        'value_inintial':
                        {'key': 'value'},
                        'value_modified': 'str'}}},
                     'group2':
                         {'status': DEL,
                          'value':
                          {'abc': 12345,
                           'deep':
                           {'id': 45}}},
                     'group3':
                         {'status': ADD,
                          'value':
                          {'deep':
                           {'id':
                            {'number': 45}},
                           'fee': 100500}},
                     'group4':
                         {'status': SPLIT,
                          'value':
                          {'default':
                           {'status': CHANGED,
                            'value_inintial': None,
                            'value_modified': ''},
                           'foo':
                           {'status': CHANGED,
                            'value_inintial': 0,
                            'value_modified': None},
                           'isNested':
                           {'status': CHANGED,
                            'value_inintial': False,
                            'value_modified': 'none'},
                           'key':
                           {'status': ADD,
                            'value': False},
                           'nest':
                           {'status': SPLIT,
                            'value':
                            {'bar':
                             {'status': CHANGED,
                              'value_inintial': '',
                              'value_modified': 0},
                             'isNested':
                             {'status': DEL,
                              'value': True}}},
                           'someKey':
                           {'status': ADD,
                            'value': True},
                           'type':
                           {'status': CHANGED,
                            'value_inintial': 'bas',
                            'value_modified': 'bar'}}}}
