import json


def read_json_file(path: str) -> list:
    """Функция, которая считывает и преобразует JSON-файл в Python-список"""
    try:
        with open(path, "r", encoding="utf-8") as file:
            try:
                data_operations = json.load(file)
                return data_operations
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
