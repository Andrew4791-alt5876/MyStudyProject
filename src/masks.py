def get_mask_card_number(user_card_number: str) -> str:
    """Функция, которая принимает на вход номер карты в виде числа и возвращает маску"""
    mask_card_number = f"{user_card_number[:4]} " f"{user_card_number[4:6]}** **** {user_card_number[-4:]}"
    return mask_card_number


def get_mask_account(user_account: str) -> str:
    """Функция, которая принимает на вход номер счета в виде числа и возвращает маску"""
    mask_account = f"**{user_account[-4:]}"
    return mask_account
