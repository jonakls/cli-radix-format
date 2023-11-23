import re as regex  # Library for regular expressions
import datetime

number_pattern = r'[0-9]*'
number_pattern_white_script = r'[0-9-]*'


def clean_numbers(value):
    list_numbers = regex.findall(number_pattern, str(value))
    cached_value = ''
    for number in list_numbers:
        cached_value += number
    return cached_value


def is_short(value):
    clean_value = clean_numbers(value)
    if len(str(clean_value)) <= 10:
        return True
    return False


def is_long(value):
    clean_value = clean_numbers(value)
    if len(str(clean_value)) >= 11:
        return True
    return False


def fill_process(process):
    process = str(process)
    if len(process) < 5:
        for i in range(0, 5 - len(process)):
            process = '0' + process
    return process


def cut_process(process):
    if len(process) > 5:
        for i in range(0, len(process) - 5):
            process = process[:-1]
        process = process
    return process


# TODO: resolve problem, return various values with high possibility of correct radix
def extract_year(value):
    clean_value = clean_numbers(value)

    if extract_mil_year(clean_value) is not None:
        return extract_mil_year(clean_value)
    elif extract_old_year(clean_value) is not None:
        return extract_old_year(clean_value)

    if str(value).__contains__('-'):
        year = extract_short_year(str(value).split('-'))
        if year is not None:
            return year
    return None


def extract_old_year(value):
    year = value[value.find("19"):value.find("19") + 4]

    if year == '':
        return None

    if 1980 <= int(year) <= 1999:
        return year
    return None


def extract_mil_year(value):
    year = value[value.find("20"):value.find("20") + 4]

    if year == '':
        return None

    if int(year) > datetime.datetime.now().year:
        value = value.replace(year, "")
        year = value[value.find("20"):value.find("20") + 4]

        if year == '':
            return None

        if int(year) > datetime.datetime.now().year:
            return None
        # TODO: check if year is valid and init another process

    if len(year) < 4:
        return None
    return year


def extract_short_year(values):

    if len(values) == 1:
        return None

    for value in values:
        if value == '':
            continue

        if 1 <= len(value) < 2:
            continue

        value = clean_numbers(value)

        if len(value) == 2:
            if 85 <= int(value) <= 99:
                return [f'19{value}', f'{value}']
            elif 0 <= int(value) <= 23:
                return [f'20{value}', f'{value}']
    return None


def extract_process(value):
    value = cut_process(value)

    if value == '':
        return None

    process = abs(int(value))

    if len(str(process)) > 5:
        raw_value = str(process)
        raw_value = cut_process(raw_value)

        if len(raw_value) < 5:
            process = fill_process(raw_value)
        else:
            return None
    elif len(str(process)) < 5:
        process = fill_process(process)

    if len(str(process)) > 5:
        return None
    return process
