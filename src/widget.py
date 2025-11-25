from src import masks


def mask_account_card(account_number_card: str) -> str:
    """Функция, которая принимает тип и номер карты или счета и возвращает данные с маской"""
    if account_number_card[-20:].isdigit():
        mask_account_card = f"{account_number_card[:5]}" f"{masks.get_mask_account(account_number_card)}"
    else:
        mask_account_card = f"{account_number_card[:-16]}" f"{masks.get_mask_card_number(account_number_card[-16:])}"
    return mask_account_card


def get_date(date_time: str) -> str:
    """Функция, которая возвращает дату"""
    date_final_str = f"{date_time[8:10]}.{date_time[5:7]}.{date_time[:4]}"
    return date_final_str
