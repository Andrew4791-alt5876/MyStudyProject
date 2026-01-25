from typing import Any
from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from src.read_file import read_csv_file, read_excel_file


class TestReadCSVFile:
    """Тесты для функции read_csv_file"""

    @pytest.mark.parametrize("invalid_input", [123, None, [], {}, 3.14])
    def test_non_string_input(self, invalid_input: Any) -> None:
        """Тест: возвращает [] при передаче не строки"""
        result = read_csv_file(invalid_input)
        assert result == []

    @patch("pandas.read_csv")
    def test_file_not_found(self, mock_read_csv: Any) -> None:
        """Тест: обрабатывает FileNotFoundError"""
        mock_read_csv.side_effect = FileNotFoundError
        result = read_csv_file("fake_file.csv")
        assert result == []
        mock_read_csv.assert_called_once_with("fake_file.csv", sep=";")

    @patch("pandas.read_csv")
    def test_permission_error(self, mock_read_csv: Any) -> None:
        """Тест: обрабатывает PermissionError"""
        mock_read_csv.side_effect = PermissionError
        result = read_csv_file("restricted.csv")
        assert result == []

    @patch("pandas.read_csv")
    def test_syntax_error(self, mock_read_csv: Any) -> None:
        """Тест: обрабатывает SyntaxError"""
        mock_read_csv.side_effect = SyntaxError
        result = read_csv_file("bad.csv")
        assert result == []

    @patch("pandas.read_csv")
    def test_type_error(self, mock_read_csv: Any) -> None:
        """Тест: обрабатывает TypeError"""
        mock_read_csv.side_effect = TypeError
        result = read_csv_file("wrong_type.csv")
        assert result == []

    @patch("pandas.read_csv")
    def test_os_error(self, mock_read_csv: Any) -> None:
        """Тест: обрабатывает OSError"""
        mock_read_csv.side_effect = OSError
        result = read_csv_file("os_error.csv")
        assert result == []

    @patch("pandas.read_csv")
    def test_successful_read(self, mock_read_csv: Any) -> None:
        """Тест: успешное чтение файла"""
        mock_df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
        mock_read_csv.return_value = mock_df
        result = read_csv_file("test.csv")
        expected = [{"col1": 1, "col2": "a"}, {"col1": 2, "col2": "b"}, {"col1": 3, "col2": "c"}]
        assert result == expected
        mock_read_csv.assert_called_once_with("test.csv", sep=";")

    @patch("pandas.read_csv")
    def test_empty_file(self, mock_read_csv: Any) -> None:
        """Тест: чтение пустого файла"""
        mock_df = pd.DataFrame()
        mock_read_csv.return_value = mock_df
        result = read_csv_file("empty.csv")
        assert result == []

    @patch("pandas.read_csv")
    def test_to_dict_returns_non_list(self, mock_read_csv: Any) -> None:
        """Тест: to_dict возвращает не список"""
        mock_df = mock_read_csv.return_value
        mock_df.to_dict.return_value = {"not": "a list"}
        result = read_csv_file("weird.csv")
        assert result == []
        mock_df.to_dict.assert_called_once_with("records")

    def test_real_csv_reading(self, tmp_path: Any) -> None:
        """Интеграционный тест с реальным файлом"""
        csv_content = """col1;col2;col3
    1;test1;value1
    2;test2;value2
    3;test3;value3"""
        file_path = tmp_path / "test.csv"
        file_path.write_text(csv_content, encoding="utf-8")
        result = read_csv_file(str(file_path))
        expected = [
            {"col1": 1, "col2": "test1", "col3": "value1"},
            {"col1": 2, "col2": "test2", "col3": "value2"},
            {"col1": 3, "col2": "test3", "col3": "value3"},
        ]
        assert result == expected

    @patch("pandas.read_csv")
    def test_custom_separator(self, mock_read_csv: Any) -> None:
        """Тест: проверяем использование правильного разделителя"""
        mock_df = pd.DataFrame({"a": [1], "b": [2]})
        mock_read_csv.return_value = mock_df
        read_csv_file("test.csv")
        mock_read_csv.assert_called_once_with("test.csv", sep=";")


class TestReadExcelFile:
    """Тесты для функции read_excel_file"""

    @pytest.mark.parametrize("invalid_input", [123, None, [], {}, 3.14, True])
    def test_non_string_input(self, invalid_input: Any) -> None:
        """Тест: возвращает [] при передаче не строки"""
        result = read_excel_file(invalid_input)
        assert result == []

    @patch("pandas.read_excel")
    def test_file_not_found(self, mock_read_excel: Any) -> None:
        """Тест: обрабатывает FileNotFoundError"""
        mock_read_excel.side_effect = FileNotFoundError
        result = read_excel_file("fake_file.xlsx")
        assert result == []
        mock_read_excel.assert_called_once_with("fake_file.xlsx")

    @patch("pandas.read_excel")
    def test_permission_error(self, mock_read_excel: Any) -> None:
        """Тест: обрабатывает PermissionError"""
        mock_read_excel.side_effect = PermissionError
        result = read_excel_file("restricted.xlsx")
        assert result == []

    @patch("pandas.read_excel")
    def test_syntax_error(self, mock_read_excel: Any) -> None:
        """Тест: обрабатывает SyntaxError (например, битый файл)"""
        mock_read_excel.side_effect = SyntaxError
        result = read_excel_file("corrupted.xlsx")
        assert result == []

    @patch("pandas.read_excel")
    def test_type_error(self, mock_read_excel: Any) -> None:
        """Тест: обрабатывает TypeError"""
        mock_read_excel.side_effect = TypeError
        result = read_excel_file("wrong_type.xlsx")
        assert result == []

    @patch("pandas.read_excel")
    def test_os_error(self, mock_read_excel: Any) -> None:
        """Тест: обрабатывает OSError"""
        mock_read_excel.side_effect = OSError
        result = read_excel_file("os_error.xlsx")
        assert result == []

    @patch("pandas.read_excel")
    def test_successful_read(self, mock_read_excel: Any) -> None:
        """Тест: успешное чтение Excel файла"""
        mock_df = pd.DataFrame({"id": [1, 2, 3], "name": ["Алиса", "Боб", "Чарли"], "age": [25, 30, 35]})
        mock_read_excel.return_value = mock_df
        result = read_excel_file("test.xlsx")
        expected = [
            {"id": 1, "name": "Алиса", "age": 25},
            {"id": 2, "name": "Боб", "age": 30},
            {"id": 3, "name": "Чарли", "age": 35},
        ]
        assert result == expected
        mock_read_excel.assert_called_once_with("test.xlsx")

    @patch("pandas.read_excel")
    def test_empty_dataframe(self, mock_read_excel: Any) -> None:
        """Тест: чтение пустого Excel файла"""
        mock_df = pd.DataFrame()
        mock_read_excel.return_value = mock_df
        result = read_excel_file("empty.xlsx")
        assert result == []

    @patch("pandas.read_excel")
    def test_single_row_dataframe(self, mock_read_excel: Any) -> None:
        """Тест: Excel файл с одной строкой"""
        mock_df = pd.DataFrame({"id": [1], "name": ["Андрей"]})
        mock_read_excel.return_value = mock_df
        result = read_excel_file("single.xlsx")
        expected = [{"id": 1, "name": "Андрей"}]
        assert result == expected

    @patch("pandas.read_excel")
    def test_to_dict_returns_non_list(self, mock_read_excel: Any) -> None:
        """Тест: to_dict возвращает не список"""
        mock_df = MagicMock(spec=pd.DataFrame)
        mock_df.to_dict.return_value = {"key": "value"}
        mock_read_excel.return_value = mock_df
        result = read_excel_file("weird.xlsx")
        assert result == []
        mock_df.to_dict.assert_called_once_with("records")

    @patch("pandas.read_excel")
    def test_read_excel_with_specific_parameters(self, mock_read_excel: Any) -> None:
        """Тест: проверяем что read_excel вызывается без дополнительных параметров"""
        mock_df = pd.DataFrame({"test": [1]})
        mock_read_excel.return_value = mock_df
        result = read_excel_file("test.xlsx")
        mock_read_excel.assert_called_once_with("test.xlsx")
        assert result == [{"test": 1}]

    def test_real_excel_reading_xlsx(self, tmp_path: Any) -> None:
        """Интеграционный тест с реальным .xlsx файлом"""
        df = pd.DataFrame(
            {"product": ["Яблоки", "Бананы", "Апельсины"], "quantity": [10, 20, 15], "price": [100.0, 50.0, 75.0]}
        )
        file_path = tmp_path / "test.xlsx"
        df.to_excel(file_path, index=False)
        result = read_excel_file(str(file_path))
        for item in result:
            if "price" in item:
                item["price"] = float(item["price"])
        expected = [
            {"product": "Яблоки", "quantity": 10, "price": 100.0},
            {"product": "Бананы", "quantity": 20, "price": 50.0},
            {"product": "Апельсины", "quantity": 15, "price": 75.0},
        ]
        assert result == expected

    @patch("pandas.read_excel")
    def test_excel_with_special_characters(self, mock_read_excel: Any) -> None:
        """Тест: Excel со специальными символами и разными типами данных"""
        mock_df = pd.DataFrame(
            {
                "text": ["Привет", "Hello", "123"],
                "number": [1.5, 2.7, 3.0],
                "boolean": [True, False, True],
                "datetime": pd.to_datetime(["2023-01-01", "2023-02-01", "2023-03-01"]),
            }
        )
        mock_read_excel.return_value = mock_df
        result = read_excel_file("special.xlsx")
        assert len(result) == 3
        assert result[0]["text"] == "Привет"
        assert result[0]["number"] == 1.5
        assert result[0]["boolean"] is True

    @pytest.mark.parametrize(
        "exception",
        [
            FileNotFoundError,
            PermissionError,
            SyntaxError,
            TypeError,
            OSError,
            ValueError,
        ],
    )
    @patch("pandas.read_excel")
    def test_all_exceptions_parametrized(self, mock_read_excel: Any, exception: Any) -> None:
        """Параметризованный тест для всех исключений"""
        mock_read_excel.side_effect = exception
        if exception == ValueError:
            with pytest.raises(ValueError):
                read_excel_file("test.xlsx")
        else:
            result = read_excel_file("test.xlsx")
            assert result == []

    @patch("pandas.read_excel")
    def test_large_excel_file(self, mock_read_excel: Any) -> None:
        """Тест: чтение большого Excel файла (много строк)"""
        data = {"id": list(range(1, 1001)), "value": [f"Value_{i}" for i in range(1, 1001)]}
        mock_df = pd.DataFrame(data)
        mock_read_excel.return_value = mock_df
        result = read_excel_file("large.xlsx")
        assert len(result) == 1000
        assert result[0]["id"] == 1
        assert result[0]["value"] == "Value_1"
        assert result[-1]["id"] == 1000
        assert result[-1]["value"] == "Value_1000"

    @patch("pandas.read_excel")
    def test_excel_with_multiple_datatypes(self, mock_read_excel: Any) -> None:
        """Тест: Excel файл со смешанными типами данных в столбце"""
        mock_df = pd.DataFrame({"mixed": [1, "text", 3.14, True, None]})
        mock_read_excel.return_value = mock_df
        result = read_excel_file("mixed.xlsx")
        assert len(result) == 5
        assert result[0]["mixed"] == 1
        assert result[1]["mixed"] == "text"
        assert result[2]["mixed"] == 3.14
        assert result[3]["mixed"] is True
        assert result[4]["mixed"] is None

    def test_file_path_with_spaces_and_special_chars(self, tmp_path: Any) -> None:
        """Тест: путь к файлу с пробелами и специальными символами"""
        df = pd.DataFrame({"col": ["test"]})
        file_path = tmp_path / "file with spaces.xlsx"
        df.to_excel(file_path, index=False)
        result = read_excel_file(str(file_path))
        assert result == [{"col": "test"}]

    @patch("pandas.read_excel")
    def test_read_excel_engine_parameter(self, mock_read_excel: Any) -> None:
        """Тест: проверяем что read_excel вызывается без указания engine"""
        mock_df = pd.DataFrame({"test": [1]})
        mock_read_excel.return_value = mock_df
        read_excel_file("test.xlsx")
        mock_read_excel.assert_called_once_with("test.xlsx")
        call_kwargs = mock_read_excel.call_args[1]
        assert "engine" not in call_kwargs


class TestReadExcelFileEdgeCases:
    """Тесты для граничных случаев"""

    def test_empty_string_path(self: Any) -> None:
        """Тест: пустая строка как путь"""
        result = read_excel_file("")
        assert result == []

    @patch("pandas.read_excel")
    def test_none_values_in_dataframe(self, mock_read_excel: Any) -> None:
        """Тест: None значения в DataFrame"""
        mock_df = pd.DataFrame({"a": [None, None], "b": [1, 2]})
        mock_read_excel.return_value = mock_df
        result = read_excel_file("none_values.xlsx")
        assert result == [{"a": None, "b": 1}, {"a": None, "b": 2}]

    @patch("pandas.read_excel")
    def test_unicode_characters(self, mock_read_excel: Any) -> None:
        """Тест: Unicode символы в данных"""
        mock_df = pd.DataFrame({"text": ["🎉 Emoji", "русский текст", "中文", "مرحبا"]})
        mock_read_excel.return_value = mock_df
        result = read_excel_file("unicode.xlsx")
        assert result == [{"text": "🎉 Emoji"}, {"text": "русский текст"}, {"text": "中文"}, {"text": "مرحبا"}]
