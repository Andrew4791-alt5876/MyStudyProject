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


list_info_data_users = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
]
for item in list_info_data_users:
    print(mask_account_card(item))


date_time = "2024-03-11T02:26:18.671407"
print(get_date(date_time))
