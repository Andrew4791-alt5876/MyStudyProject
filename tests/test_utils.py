from unittest.mock import mock_open, patch

from src.utils import read_json_file


def test_read_json_file_with_json_file() -> None:
    """Тест функции преобразования JSON-файла при корректном файле и пути до него."""
    test_data = '[{"id": 441945886, "state": "EXECUTED"}]'
    with patch("builtins.open", mock_open(read_data=test_data)):
        resalt = read_json_file("../data/operations.json")
    assert resalt == [{"id": 441945886, "state": "EXECUTED"}]


def test_read_json_file_with_not_right_json_file() -> None:
    """Тест функции преобразования JSON-файла при не корректном файле."""
    test_data = '[{"441945886id": , "state": "EXECUTED"}]'
    with patch("builtins.open", mock_open(read_data=test_data)):
        resalt = read_json_file("../data/operations.json")
    assert resalt == []


def test_read_json_file_with_empty_list() -> None:
    """Тест функции с пустым JSON списком."""
    test_data = "[]"
    with patch("builtins.open", mock_open(read_data=test_data)):
        result = read_json_file("../data/operations.json")
    assert result == []


def test_read_json_file_with_invalid_path_syntax() -> None:
    """Тест функции с некорректным синтаксисом пути."""
    resalt = read_json_file("C:\\invalid:path\\file.json")
    assert resalt == []


def test_read_json_file_with_no_path() -> None:
    """Тест функции преобразования JSON-файла при отсутствии пути."""
    result = read_json_file()
    assert result == []
