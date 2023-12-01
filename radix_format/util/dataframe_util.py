def isvalid(df):
    if df is None:
        print('[!] El dataframe es nulo.')
        return False
    if df.empty:
        print('[!] El dataframe está vacío.')
        return False

    if 'BASE_ID' not in df.columns and 'ID_PROCESO' not in df.columns and 'ID_INCLUSION_CLIENTE' not in df.columns:
        print('[!] El dataframe no tiene las columnas necesarias.')
        return False

    if 'RADICACION' not in df.columns:
        print('[!] El dataframe no tiene la columna RADICACION.')
        return False
    return True


