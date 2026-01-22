import pandas as pd


def read_csv_file(file_path_csv: str) -> list[dict]:
    """Функция, которая преобразует csv-файл в python базу данных"""
    df_csv_file = pd.read_csv(file_path_csv, sep=";")
    list_df_csv_file = df_csv_file.to_dict("records")
    return list_df_csv_file


def read_excel_file(file_path_excel: str) -> list[dict]:
    """Функция, которая преобразует excel-файл в python базу данных"""
    df_excel_file = pd.read_excel(file_path_excel)
    list_df_excel_file = df_excel_file.to_dict("records")
    return list_df_excel_file
