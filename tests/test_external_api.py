from typing import Any
from unittest.mock import MagicMock, Mock, patch

import requests

from src.external_api import amount_of_transactions, convert_amount_of_transactions


def test_with_monkeypatch(monkeypatch: Any) -> None:
    """Тест с использованием monkeypatch фикстуры"""
    monkeypatch.setattr("src.external_api.os.getenv", lambda x: "test-api-key")
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = '{"result": 7500.50}'
    mock_response.raise_for_status.return_value = None
    monkeypatch.setattr("src.external_api.requests.request", lambda *args, **kwargs: mock_response)
    result = convert_amount_of_transactions(100.0, "USD")
    assert result == 7500.50


def test_api_key_not_found() -> None:
    """Тест отсутствия API ключа"""
    with patch("src.external_api.os.getenv", return_value=None), patch("src.external_api.load_dotenv"):
        result = convert_amount_of_transactions(100.0, "USD")
        assert result == "API ключ не найден"


def test_http_error() -> None:
    """Тест HTTP ошибки от API"""
    with patch("src.external_api.os.getenv", return_value="test-key"), patch("src.external_api.load_dotenv"), patch(
        "src.external_api.requests.request"
    ) as mock_request:
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("401 Client Error: Unauthorized")
        mock_request.return_value = mock_response
        result = convert_amount_of_transactions(100.0, "USD")
        assert isinstance(result, str)
        assert "Ошибка запроса:" in result
        assert "401" in result


def test_network_timeout() -> None:
    """Тест таймаута сети"""
    with patch("src.external_api.os.getenv", return_value="test-key"), patch("src.external_api.load_dotenv"), patch(
        "src.external_api.requests.request"
    ) as mock_request:
        mock_request.side_effect = requests.exceptions.Timeout("Таймаут")
        result = convert_amount_of_transactions(100.0, "USD")
        assert isinstance(result, str)
        assert "Ошибка запроса:" in result
        assert "Таймаут" in result


def test_invalid_json_response() -> Any:
    """Тест некорректного JSON в ответе"""
    with patch("src.external_api.os.getenv", return_value="test-key"), patch("src.external_api.load_dotenv"), patch(
        "src.external_api.requests.request"
    ) as mock_request:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "Не валидный JSON {"
        mock_response.raise_for_status.return_value = None
        mock_request.return_value = mock_response
        result = convert_amount_of_transactions(100.0, "USD")
        assert isinstance(result, str)
        assert "Ошибка обработки данных:" in result


# Мокируем функцию конвертации для тестов
@patch("src.external_api.convert_amount_of_transactions")
class TestAmountOfTransactions:
    """Тесты для функции amount_of_transactions"""

    def test_rub_transaction(self, mock_convert: Any) -> None:
        """Тест транзакции в рублях"""
        transaction = {"operationAmount": {"amount": "1500.50", "currency": {"code": "RUB"}}}
        result = amount_of_transactions(transaction)
        assert result == 1500.50
        mock_convert.assert_not_called()

    def test_usd_transaction(self, mock_convert: Any) -> None:
        """Тест транзакции в долларах"""
        mock_convert.return_value = 75000.0
        transaction = {"operationAmount": {"amount": "1000.00", "currency": {"code": "USD"}}}
        result = amount_of_transactions(transaction)
        assert result == 75000.0
        mock_convert.assert_called_once_with(1000.0, "USD")

    def test_eur_transaction(self, mock_convert: Any) -> None:
        """Тест транзакции в евро"""
        mock_convert.return_value = 85000.0
        transaction = {"operationAmount": {"amount": "1000.00", "currency": {"code": "EUR"}}}
        result = amount_of_transactions(transaction)
        assert result == 85000.0
        mock_convert.assert_called_once_with(1000.0, "EUR")

    def test_invalid_currency(self, mock_convert: Any) -> None:
        """Тест недопустимой валюты"""
        transaction = {"operationAmount": {"amount": "1000.00", "currency": {"code": "GBP"}}}
        result = amount_of_transactions(transaction)
        assert result == "Не допустимая валюта"
        mock_convert.assert_not_called()
