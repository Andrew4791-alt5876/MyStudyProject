import os
from typing import Any

from src.decorators import log


def test_log_print_console_with_data(capsys: Any) -> None:
    """Тест декоратора при выводе результата работы декоратора с результатом функции в консоль
    при отсутствии файла вывода."""

    @log(filename="")
    def my_function(a: Any, b: Any) -> Any:
        return a / b

    result_dec = my_function(20, 2)
    captured = capsys.readouterr()
    output = captured.out
    assert result_dec == 10.0
    assert "my_function" in output.lower()


def test_log_write_to_file_with_data() -> None:
    """Тест для декоратора, когда результат работы функции и декоратора выводится в заданный файл."""
    filename = "mylog.txt"
    if os.path.exists(filename):
        os.remove(filename)

    @log(filename=filename)
    def my_function(a: Any, b: Any) -> Any:
        return a / b

    result = my_function(20, 5)
    assert result == 4.0
    assert os.path.exists(filename)
    with open(filename, "r") as f:
        f.read()
    os.remove(filename)


def test_log_print_console_with_zero_devision_data(capsys: Any) -> None:
    '''hai'''
    """Тест декоратора при выводе результата работы декоратора с результатом функции
    в консоль при отсутствии файла вывода при попытке деления на ноль."""

    @log(filename="")
    def my_function(a: Any, b: Any) -> Any:
        return a / b

    my_function(20, 0)
    captured = capsys.readouterr()
    output = captured.out
    assert "ZeroDivisionError" in output
    assert "my_function" in output.lower()


def test_log_print_console_no_data(capsys: Any) -> None:
    """Тест декоратора при выводе результата работы декоратора с результатом функции в консоль
    при отсутствии файла вывода и отсутствии данных ввода."""

    @log(filename="")
    def my_function(a: Any, b: Any) -> Any:
        return a / b

    my_function()
    captured = capsys.readouterr()
    output = captured.out
    assert "TypeError" in output
    assert "my_function" in output.lower()


def test_log_print_console_with_wrong_data(capsys: Any) -> None:
    """Тест декоратора при выводе результата работы декоратора с результатом функции в консоль
    при отсутствии файла вывода при не верных входных данных для функции."""

    @log(filename="")
    def my_function(a: Any, b: Any) -> Any:
        return a / b

    my_function(1, "20")
    captured = capsys.readouterr()
    output = captured.out
    assert "TypeError" in output
    assert "my_function" in output.lower()


def test_log_write_to_file_with_zero_devision_data() -> None:
    """Тест для декоратора, когда результат работы функции и декоратора выводится в заданный
    файл при попытке деления на ноль."""
    filename = "mylog.txt"
    if os.path.exists(filename):
        os.remove(filename)

    @log(filename=filename)
    def my_function(a: Any, b: Any) -> Any:
        return a / b

    result = my_function(10, 0)
    assert result == "Функция my_function, Ошибка: ZeroDivisionError, Входные аргументы: (10, 0), {}"
    assert os.path.exists(filename)
    with open(filename, "r") as f:
        f.read()
    os.remove(filename)


def test_log_write_to_file_no_data() -> None:
    """Тест для декоратора, когда результат работы функции и декоратора выводится в заданный файл."""
    filename = "mylog.txt"
    if os.path.exists(filename):
        os.remove(filename)

    @log(filename=filename)
    def my_function(a: Any, b: Any) -> Any:
        return a / b

    result = my_function()
    assert result == "Функция my_function, Ошибка: TypeError, Входные аргументы: (), {}"
    assert os.path.exists(filename)
    with open(filename, "r") as f:
        f.read()
    os.remove(filename)
