import logging


logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/masks.log', encoding='utf-8')
file_formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_mask_card_number(user_card_number: str) -> str:
    """Функция, которая принимает на вход номер карты в виде числа и возвращает маску"""
    if isinstance(user_card_number, str):
        numbers = user_card_number.replace(" ", "")
        if len(numbers) == 16 and numbers.isdigit():
            logger.info(f'Маска номера карты клиента создана')
            mask_card_number = f"{numbers[:4]} " f"{numbers[4:6]}** **** {numbers[-4:]}"
            return mask_card_number
        else:
            logger.error(f'Ошибка ввода номера карты')
            return "Ошибка ввода номера карты!"
    else:
        logger.error(f'Ошибка ввода номера карты')
        return "Ошибка ввода номера карты!"


def get_mask_account(user_account: str) -> str:
    """Функция, которая принимает на вход номер счета в виде числа и возвращает маску"""
    if isinstance(user_account, str):
        numbers_of_account = user_account.replace(" ", "")
        if len(numbers_of_account) == 20 and numbers_of_account.isdigit():
            logger.info(f'Маска номера счета клиента создана')
            mask_account = "**" + numbers_of_account[-4:]
            return mask_account
        else:
            logger.error(f'Ошибка ввода номера счета')
            return "Ошибка ввода номера счета!"
    else:
        logger.error(f'Ошибка ввода номера счета')
        return "Ошибка ввода номера счета!"


print(get_mask_card_number('2234234523457891'))
print(get_mask_account('12345123451234512341'))