import pandas as pd


def clean_column_names(df):
    """
    Standardize DataFrame column names.

    Converts column names to lowercase, removes leading/trailing
    whitespace, and replaces spaces with underscores.

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame.

    Returns
    -------
    pandas.DataFrame
        DataFrame with cleaned column names.
    """
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df
