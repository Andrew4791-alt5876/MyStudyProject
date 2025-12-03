import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card_number, mask_card_number",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("2200 5436 5456 9080", "2200 54** **** 9080"),
        (1234234567894563, "Ошибка ввода номера карты!"),
        ("123456789012345", "Ошибка ввода номера карты!"),
        ("number3456 4556 65", "Ошибка ввода номера карты!"),
        ("", "Ошибка ввода номера карты!"),
        ((1, 2, 3), "Ошибка ввода номера карты!"),
    ],
)
def test_get_mask_card_number(card_number, mask_card_number):
    assert get_mask_card_number(card_number) == mask_card_number


@pytest.mark.parametrize(
    "account, mask_account",
    [
        ("73654108430135874305", "**4305"),
        ("12345 12345 12345 12345", "**2345"),
        (12345123451234512345, "Ошибка ввода номера счета!"),
        ("1234565432345676543", "Ошибка ввода номера счета!"),
        ("account1234 51231 2345", "Ошибка ввода номера счета!"),
        ("", "Ошибка ввода номера счета!"),
        ((1, 2, 3), "Ошибка ввода номера счета!"),
    ],
)
def test_get_mask_account(account, mask_account):
    assert get_mask_account(account) == mask_account
