import json


def read_json_file(path: str = "") -> list:
    """Функция, которая считывает и преобразует JSON-файл в Python-список"""
    if not isinstance(path, str):
        return []
    try:
        with open(path, "r", encoding="utf-8") as file:
            try:
                data_operations = json.load(file)
                if isinstance(data_operations, list):
                    return data_operations
                else:
                    return []
            except json.JSONDecodeError:
                return []
    except (FileNotFoundError, PermissionError, SyntaxError, TypeError, OSError):
        return []
