def get_mask_card_number(user_card_number: str) -> str:
    """Функция, которая принимает на вход номер карты в виде числа и возвращает маску"""
    numbers = user_card_number.replace(" ", "")
    if len(numbers) == 16 and numbers.isdigit():
        mask_card_number = numbers[:4] + " " + numbers[4:6] + "** **** " + numbers[-4:]
        return mask_card_number
    else:
        return "Ошибка ввода номера карты!"


def get_mask_account(user_account: str) -> str:
    """Функция, которая принимает на вход номер счета в виде числа и возвращает маску"""
    numbers_of_account = user_account.replace(" ", "")
    if len(numbers_of_account) == 20 and numbers_of_account.isdigit():
        mask_account = "**" + numbers_of_account[-4:]
        return mask_account
    else:
        return "Ошибка ввода номера счета!"
