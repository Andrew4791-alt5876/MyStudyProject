import json
from typing import Any


def read_json_file(path: str) -> list[Any]:
    """Функция, которая считывает и преобразует JSON-файл в Python-список"""
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
    except FileNotFoundError:
        return []
