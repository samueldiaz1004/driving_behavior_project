import pandas as pd
import numpy as np

def drop_cols(df: pd.DataFrame, columns: list):
    df.drop(columns=columns, inplace=True)

def drop_atypical_data(df: pd.DataFrame, columns: list):
    for column in columns:
        Q1v = np.percentile(df[column], 25)
        Q3v = np.percentile(df[column], 75)
        IQRv = Q3v - Q1v
        Lsv = Q3v + 1.5 * IQRv
        Liv = Q1v - 1.5 * IQRv

        Lsuperior = df[df[column] > Lsv].index
        Linferior = df[df[column] < Liv].index

        df.drop(Lsuperior, inplace=True)
        df.drop(Linferior, inplace=True)

def feature_training_diff_past(df: pd.DataFrame, columns: list):
    for column in columns:
        df[f"Diff{column}"] = df[column] - df[column].shift(1)
        df[f"Diff{column}"] = df[f"Diff{column}"].fillna(0)

if __name__ == "__main__":
    drop_columns = ["AccZ", "GyroX", "GyroY", "GyroZ", "Timestamp"]
    atypical_columns = []
    diff_feature_train = ["AccX", "AccY"]

    url_train = "data/train_motion_data.csv"
    url_test = "data/test_motion_data.csv"
    url_train_clean = "data_mod/train_motion_data.csv"
    url_test_clean = "data_mod/test_motion_data.csv"

    df_train = pd.read_csv(url_train)
    df_test = pd.read_csv(url_test)

    drop_cols(df_train, drop_columns)
    drop_cols(df_test, drop_columns)

    feature_training_diff_past(df_train, diff_feature_train)
    feature_training_diff_past(df_test, diff_feature_train)

    drop_atypical_data(df_train, atypical_columns)

    df_train.to_csv(url_train_clean, index=False)
    df_test.to_csv(url_test_clean, index=False)
   