import pytest

from src.widget import get_date, mask_account_card_fun


@pytest.mark.parametrize(
    "account_number_card, mask_account_card",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет fghsgjhjhs4534567655", "Не верный номер счета или карты!"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        (12341234134344555464, "Не верный номер счета или карты!"),
        ("Visa Classic 68319824767376567", "Не верный номер счета или карты!"),
        ("Счет 7365410843013587430", "Не верный номер счета или карты!"),
        ("Visa Gold 599941422842635", "Не верный номер счета или карты!"),
    ],
)
def test_mask_account_card(account_number_card: str, mask_account_card: str) -> None:
    assert mask_account_card_fun(account_number_card) == mask_account_card


@pytest.mark.parametrize(
    "date_time, get_date_str",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("03-11T02:26:18.671407", "Не верный формат даты!"),
        (19800405687787977, "Не верный формат даты!"),
    ],
)
def test_get_date(date_time: str, get_date_str: str) -> None:
    assert get_date(date_time) == get_date_str
