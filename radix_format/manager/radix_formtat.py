import numpy as np


def init_format(data_frame):
    from radix_organizer.manager import radix_short
    from radix_organizer.manager import radix_long
    from radix_organizer.util import FormatUtil
    if data_frame is None:
        raise Exception('No se ha cargado ningún archivo o simplemente hubo un error al cargarlo.')

    data_frame['LARGO_RADICADO'] = np.nan
    data_frame['RADICADO_VIRGEN'] = np.nan
    data_frame['LARGO_RADICADO_VIRGEN'] = np.nan
    data_frame['RADICADO_C9'] = np.nan
    data_frame['LARGO_RAD_C9'] = np.nan
    data_frame['RADICADO_C10'] = np.nan
    data_frame['LARGO_RAD_C10'] = np.nan

    data_frame['RADICADO_VIRGEN'] = data_frame['RADICADO_VIRGEN'].astype('object')
    data_frame['LARGO_RADICADO_VIRGEN'] = data_frame['LARGO_RADICADO_VIRGEN'].astype('object')
    data_frame['LARGO_RADICADO'] = data_frame['LARGO_RADICADO'].astype('object')
    data_frame['RADICADO_C9'] = data_frame['RADICADO_C9'].astype('object')
    data_frame['RADICADO_C10'] = data_frame['RADICADO_C10'].astype('object')
    data_frame['LARGO_RAD_C9'] = data_frame['LARGO_RAD_C9'].astype('object')
    data_frame['LARGO_RAD_C10'] = data_frame['LARGO_RAD_C10'].astype('object')

    if data_frame is None:
        raise Exception('No se ha cargado ningún archivo o simplemente hubo un error al cargarlo.')

    for index, row in data_frame.iterrows():
        value = row['RADICACION']

        if value is None or value == '':
            data_frame.at[index, 'LARGO_RADICADO'] = 'Valor nulo'
            continue

        if value is None or value == '':
            data_frame.at[index, 'LARGO_RADICADO'] = 'Valor nulo'
            continue

        data_frame.at[index, 'LARGO_RADICADO'] = str(value).__len__()
        clean_value = FormatUtil.clean_numbers(value)
        data_frame.at[index, 'RADICADO_VIRGEN'] = str("." + clean_value)
        data_frame.at[index, 'LARGO_RADICADO_VIRGEN'] = str(clean_value).__len__()
        if FormatUtil.is_short(value):
            format_value_c9 = radix_short.format_c9(value)
            format_value_c10 = radix_short.format_c10(value)
            set_values(data_frame, index, format_value_c9, format_value_c10)
        elif FormatUtil.is_long(value):
            format_value_c9 = radix_long.format_c9(value)
            format_value_c10 = radix_long.format_c10(value)
            set_values(data_frame, index, format_value_c9, format_value_c10)
        else:
            set_values(data_frame, index, '0', '0')


def set_values(data_frame, index, value_c9, value_c10):
    data_frame.at[index, 'RADICADO_C9'] = value_c9
    data_frame.at[index, 'RADICADO_C10'] = value_c10

    if value_c9 is None:
        data_frame.at[index, 'LARGO_RAD_C9'] = 0
    else:
        data_frame.at[index, 'LARGO_RAD_C9'] = str(len(value_c9))

    if value_c10 is None:
        data_frame.at[index, 'LARGO_RAD_C10'] = 0
    else:
        data_frame.at[index, 'LARGO_RAD_C10'] = str(value_c9).__len__()
