import os
import pytest
from fixtures.test_comparisons import PLAIN_COMPARISON
from fixtures.test_comparisons import COMPLEX_COMPARISON
from fixtures.test_comparisons import HEXLET_COMPARISON
from fixtures.test_raw_data import PLAIN1_RAW_DATA
from fixtures.test_raw_data import PLAIN2_RAW_DATA
from fixtures.test_raw_data import COMPLEX1_RAW_DATA
from fixtures.test_raw_data import COMPLEX2_RAW_DATA
from fixtures.test_raw_data import HEXLET1_RAW_DATA
from fixtures.test_raw_data import HEXLET2_RAW_DATA

# scenarios
PLAIN = 'plain'
COMPLEX = 'complex'
HEXLET = 'hexlet'

# styles of report
REPORT_STYLISH = 'stylish'
REPORT_PLAIN = 'plain'
REPORT_JSON = 'json'

# json, yaml files for different scenarios
SOURCE_FILES = ({PLAIN + '1': 'source_json/test01.json',
                 PLAIN + '2': 'source_json/test02.json'},
                {COMPLEX + '1': 'source_json/test11.json',
                 COMPLEX + '2': 'source_json/test12.json'},
                {PLAIN + '1': 'source_yml/test21.yaml',
                 PLAIN + '2': 'source_yml/test22.yaml'},
                {COMPLEX + '1': 'source_yml/test31.yml',
                 COMPLEX + '2': 'source_yml/test32.yaml'},
                {COMPLEX + '1': 'source_json/test11.json',
                 COMPLEX + '2': 'source_yml/test32.yaml'},
                {HEXLET + '1': 'source_json/f1.json',
                 HEXLET + '2': 'source_json/f2.json'})

# files contain two scenarios for each style
REPORTS = {REPORT_PLAIN:
           {PLAIN: 'plain/plain00.txt',
            COMPLEX: 'plain/plain10.txt',
            HEXLET: 'plain/hexlet_plain.txt'},
           REPORT_STYLISH:
           {PLAIN: 'stylish/result00.txt',
            COMPLEX: 'stylish/result10.txt',
            HEXLET: 'stylish/hexlet.txt'},
           REPORT_JSON:
           {PLAIN: 'js_report/json00.txt',
            COMPLEX: 'js_report/json10.txt',
            HEXLET: 'js_report/hexlet.txt'}}

# what should be recieved from differnet scenarios
RAW_DATA = {PLAIN + '1': PLAIN1_RAW_DATA,
            PLAIN + '2': PLAIN2_RAW_DATA,
            COMPLEX + '1': COMPLEX1_RAW_DATA,
            COMPLEX + '2': COMPLEX2_RAW_DATA,
            HEXLET + '1': HEXLET1_RAW_DATA,
            HEXLET + '2': HEXLET2_RAW_DATA}


# merging of two files is a dictionary:
COMPARISONS = ((PLAIN, PLAIN_COMPARISON),
               (COMPLEX, COMPLEX_COMPARISON),
               (HEXLET, HEXLET_COMPARISON))


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


@pytest.fixture(scope='session')
def raw_data():
    return RAW_DATA


@pytest.fixture(scope='session', params=SOURCE_FILES)
def complexity_pair_files(request):
    file_pair = []
    for key, value in request.param.items():
        file_pair.append(key[:-1])
        file_pair.append(get_fixture_path(value))
    file_pair.pop(2)
    return tuple(file_pair)


def source_file():
    source_list = []
    for pair_file in SOURCE_FILES:
        for key, value in pair_file.items():
            value = get_fixture_path(value)
            source_list.append((key, value))
    return tuple(source_list)


@pytest.fixture(scope='session', params=source_file())
def complexity_and_file(request):
    return request.param


@pytest.fixture(scope='session')
def reports():
    reports = dict()
    for style, files in REPORTS.items():
        one_style_reports = dict()
        for pattern, path in files.items():
            with open(get_fixture_path(path), 'r') as file:
                one_style_reports[pattern] = file.read()
        reports[style] = one_style_reports
    return reports


@pytest.fixture(scope='session', params=COMPARISONS)
def mergings(request):
    return request.param


@pytest.fixture(scope='session')
def merging_versions():
    mergings = dict()
    for key, value in COMPARISONS:
        mergings[key] = value
    return mergings
