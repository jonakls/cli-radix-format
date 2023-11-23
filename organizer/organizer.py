import time

from organizer import serialize as Serializer
from organizer.manager.radix import RadixFormatManager
from organizer.util import DataFrameUtil


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
    "G:\\Mi unidad\\TRABAJO\\VERIFICACION\\NOVIEMBRE\\15\\Inclusiones Banco Davivienda BPJ - Noviembre\\rad.xlsx",
    "G:\\Mi unidad\\TRABAJO\\VERIFICACION\\NOVIEMBRE\\15\\Inclusiones Banco Davivienda BPJ - Noviembre\\results.csv"
)
