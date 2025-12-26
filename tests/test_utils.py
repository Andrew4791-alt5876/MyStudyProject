from unittest.mock import mock_open, patch

from src.utils import read_json_file


def test_read_json_file_with_json_file() -> None:
    '''Тест функции преобразования JSON-файла при корректном файле и пути до него.'''
    test_data = '[{"id": 441945886, "state": "EXECUTED"}]'
    with patch('builtins.open', mock_open(read_data=test_data)):
        resalt = read_json_file('../data/operations.json')
    assert resalt == [{"id": 441945886, "state": "EXECUTED"}]


def test_read_json_file_with_not_right_json_file() -> None:
    """Тест функции преобразования JSON-файла при не корректном файле."""
    test_data = '{"id": 441945886, "state": "EXECUTED"}]'
    with patch('builtins.open', mock_open(read_data=test_data)):
        resalt = read_json_file('../data/operations.json')
    assert resalt == []


def test_read_json_file_with_not_found_json_file() -> None:
    """Тест функции преобразования JSON-файла при не найденном файле."""
    test_data = '{"id": 441945886, "state": "EXECUTED"}]'
    with patch('builtins.open', mock_open(read_data=test_data)):
        resalt = read_json_file('/data/operations.json')
    assert resalt == []
