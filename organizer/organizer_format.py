import time

import manager.RadixFormatManager as RadixFormatManager
from serializer import CSVSerializer as Serializer
from util import DataFrameUtil


def init_dataframe(data_frame):
    initial_epoch = round(time.time() * 1000)
    print('[!] Iniciando proceso de formato de radicados...')

    if not DataFrameUtil.isvalid(data_frame):
        print('[!] El dataframe no es válido.')
        return

    RadixFormatManager.init_format(data_frame)
    final_epoch = round(time.time() * 1000)
    print(f'[!] Se cargaron {len(data_frame)} registros desde el dataframe.')
    print(f'[!] Finalizado en: {str((final_epoch - initial_epoch) / 1000)} segundos')
    return data_frame


def init_path(input_path, output_path):
    initial_epoch = round(time.time() * 1000)
    print('[!] Iniciando proceso de formato de radicados...')
    data_frame = Serializer.deserialize(input_path)
    RadixFormatManager.init_format(data_frame)
    Serializer.serialize(output_path, data_frame)
    final_epoch = round(time.time() * 1000)
    print(f'[!] Se cargaron {len(data_frame)} registros de: {input_path}')
    print(f'[!] Finalizado en: {str((final_epoch - initial_epoch) / 1000)} segundos')


init_path(
    "C:\\Users\\jonakls\\OneDrive - LITIGAR PUNTO COM S.A\\Inclusiones\\PROCESAR\\2023\\NOVIEMBRE\\23\\INCLUIR BANCOOMEVA NOV 2023\\RAD_EJE.xlsx",
    "C:\\Users\\jonakls\\OneDrive - LITIGAR PUNTO COM S.A\\Inclusiones\\PROCESAR\\2023\\NOVIEMBRE\\23\\INCLUIR BANCOOMEVA NOV 2023\\RESULTADOS.csv"
)
