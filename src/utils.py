import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    "C:/Users/User/PycharmProjects/PythonProject1/logs/utils.log", "w", encoding="utf-8"
)
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def read_json_file(path: str = "") -> list:
    """Функция, которая считывает и преобразует JSON-файл в Python-список"""
    if not isinstance(path, str):
        logger.error("Не верный путь к JSON-файлу")
        return []
    try:
        with open(path, "r", encoding="utf-8") as file:
            try:
                data_operations = json.load(file)
                logger.info("JSON-файл в Python-список преобразован успешно")
                if isinstance(data_operations, list):
                    return data_operations
                else:
                    return []
            except json.JSONDecodeError:
                logger.error("Не верный формат JSON-файла")
                return []
    except (FileNotFoundError, PermissionError, SyntaxError, TypeError, OSError):
        logger.error("Ошибка при считывании JSON-файла")
        return []
