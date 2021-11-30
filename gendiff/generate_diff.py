from gendiff.parsing_reporting.parsing import parse_data
from gendiff.parsing_reporting.diff_report import generate_json_report
from gendiff.convert_from_file import extract_raw_data


def generate_report(first_file, second_file):
    first_arguments = extract_raw_data(first_file)
    second_arguments = extract_raw_data(second_file)
    parsed_data = parse_data(first_arguments, second_arguments)
    report = generate_json_report(parsed_data)
    return report


if __name__ == '__main__':
    generate_report()
