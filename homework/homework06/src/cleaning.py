import pandas as pd


def fill_missing_median(df, columns):
    df = df.copy()

    for column in columns:
        df[column] = df[column].fillna(df[column].median())

    return df

def drop_missing(df, threshold=0.5):
    df = df.copy()

    missing_fraction = df.isna().mean()
    columns_to_keep = missing_fraction[missing_fraction <= threshold].index

    return df[columns_to_keep]

def normalize_data(df, columns):
    df = df.copy()

    for column in columns:
        minimum = df[column].min()
        maximum = df[column].max()

        if maximum != minimum:
            df[column] = (df[column] - minimum) / (maximum - minimum)

    return df