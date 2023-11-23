import pandas as pd


def process_file(input_path):
    try:
        with open(input_path, 'r') as file:
            file.close()
            if input_path.endswith('.csv') or input_path.endswith('.txt'):
                return pd.read_csv(input_path, delimiter='\t', encoding='latin1')
            elif input_path.endswith('.xlsx'):
                return pd.read_excel(input_path)
            else:
                print('Este archivo no tiene un formato válido.')
                return None
    except PermissionError:
        print('No se pudo leer el archivo, puede que esté abierto o otro programa lo esté usando.')
        return None


def deserialize(input_path):
    data_frame = process_file(input_path)

    if data_frame is None:
        return

    data_frame.head()
    if 'PROCESO_ID' in data_frame.columns:
        radix_context = data_frame[['PROCESO_ID', 'RADICACION']]
    elif 'BASE_ID' in data_frame.columns:
        radix_context = data_frame[['BASE_ID', 'RADICACION']]
    else:
        print('Este archivo no tiene un formato válido.')
        return None
    return radix_context


def serialize(output_path, data_frame):
    try:
        with open(output_path, 'w') as file:
            file.close()
            data_frame.to_csv(output_path, sep=';', index=False)
    except PermissionError:
        return None
