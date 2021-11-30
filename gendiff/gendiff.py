from gendiff.parsing.parsing import parse_data
from gendiff.formating.format_report import generate_report
from gendiff.convert_from_file import extract_raw_data


def generate_diff(first_file, second_file):
    first_arguments = extract_raw_data(first_file)
    second_arguments = extract_raw_data(second_file)
    parsed_data = parse_data(first_arguments, second_arguments)
    report = generate_report(parsed_data)
    return report