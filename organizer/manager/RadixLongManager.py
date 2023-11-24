from organizer.util import FormatUtil


def format_c9(value):
    clean_value = FormatUtil.clean_numbers(value)

    generic_value = generic_format(clean_value)
    if generic_value is None:
        return ''
    if len(generic_value) == 1:
        return f'{generic_value[0]}'
    elif len(generic_value) == 2:
        return f'{generic_value[0]}{generic_value[1]}'
    return ''


def format_c10(value):
    clean_value = FormatUtil.clean_numbers(value)

    generic_value = generic_format(clean_value)
    if generic_value is None:
        return ''
    if len(generic_value) == 1:
        return f'{generic_value[0]}'
    if len(generic_value) == 2:
        return f'{generic_value[0]}-{generic_value[1]}'
    return ''


def generic_format(value):
    clean_value = FormatUtil.clean_numbers(value)

    year = FormatUtil.extract_year(clean_value)

    if year is None:
        return None

    position = clean_value.find(year)
    clean_value = clean_value.replace(year, "")
    process = FormatUtil.extract_process(clean_value[position:])
    if process is not None:
        return [year, process]

    process = FormatUtil.extract_process(clean_value[:position])
    if process is not None:
        return [year, process]
    return None
