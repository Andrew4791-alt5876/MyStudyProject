from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card_fun(account_number_card: str) -> str:
    """Функция, которая принимает тип и номер карты или счета и возвращает данные с маской"""
    if isinstance(account_number_card, str) and account_number_card[-16:].isdigit():
        if account_number_card[-20:].isdigit() and len(account_number_card) <= 25:
            mask_account_card = f"{account_number_card[:4]} {get_mask_account(account_number_card[-20:])}"
            return mask_account_card
        elif account_number_card[-19:-17].isalpha():
            mask_account_card = f"{account_number_card[:-17]} {get_mask_card_number(account_number_card[-16:])}"
            return mask_account_card
        else:
            return "Не верный номер счета или карты!"
    else:
        return "Не верный номер счета или карты!"


def get_date(date_time: str) -> str:
    """Функция, которая возвращает дату"""
    if isinstance(date_time, str):
        try:
            dt = datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%S.%f")
            date_final_str = f"{dt.day:02d}.{dt.month:02d}.{dt.year}"
            return date_final_str
        except ValueError:
            return "Не верный формат даты!"
    else:
        return "Не верный формат даты!"
