
def isvalid(df):
    if df is None:
        return False
    if df.empty:
        return False

    if 'ID_BASE' not in df.columns:
        return False
    if 'ID_PROCESO' not in df.columns:
        return False
    if 'ID_INCLUSION_CLIENTE' not in df.columns:
        return False
    if 'RADICACION' not in df.columns:
        return False
    return True


