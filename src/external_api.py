import json
import os
from typing import Any, Dict, Union

import requests
from dotenv import load_dotenv


def convert_amount_of_transactions(amount: float, currency: str) -> Union[float, str]:
    """Функция конвертирования валюты из долларов или евро в рубли."""
    load_dotenv()
    API_KEY: str | None = os.getenv("API_KEY")
    if not API_KEY:
        return "API ключ не найден"
    url = "https://api.apilayer.com/currency_data/convert"
    headers = {"apikey": API_KEY}
    params: Dict[str, Union[str, float]] = {"to": "RUB", "from": currency, "amount": amount}
    try:
        response = requests.request("GET", url, headers=headers, params=params, timeout=10)
        response.raise_for_status()  # Проверка HTTP ошибок
        result = json.loads(response.text)
        # Проверяем структуру ответа
        if "result" in result and isinstance(result["result"], (int, float)):
            return round(float(result["result"]), 2)
        else:
            return "Неверный формат ответа от API"
    except requests.exceptions.RequestException as e:
        return f"Ошибка запроса: {str(e)}"
    except (json.JSONDecodeError, KeyError, ValueError) as e:
        return f"Ошибка обработки данных: {str(e)}"


def amount_of_transactions(transaction: Dict[str, Any]) -> Union[float, str]:
    """Функция возвращения суммы транзакции в рублях, даже при входных данных в долларах или евро."""
    try:
        operation_amount = transaction["operationAmount"]
        amount = float(operation_amount["amount"])
        currency_code = operation_amount["currency"]["code"]
        if currency_code == "USD":
            return convert_amount_of_transactions(amount, "USD")
        elif currency_code == "EUR":
            return convert_amount_of_transactions(amount, "EUR")
        elif currency_code == "RUB":
            return amount
        else:
            return "Не допустимая валюта"
    except (KeyError, ValueError, TypeError) as e:
        return f"Ошибка в данных транзакции: {str(e)}"
