import gendiff.gendiff as gen


def test_generate_report(get_test_data):
    normalized_paths, data_and_results = get_test_data
    for index, value in enumerate(normalized_paths):
        assert gen.generate_diff(value[0],
                                 value[1]) == data_and_results[
            index][2]
        assert gen.generate_diff(value[0],
                                 value[1],
                                 'plain') == data_and_results[index][3]
        assert gen.generate_diff(value[0],
                                 value[1],
                                 'json') == data_and_results[index][4]
