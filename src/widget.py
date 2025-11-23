def mask_account_card(account_number_card: str) -> str:
    """Функция, которая принимает тип и номер карты или счета и возвращает данные с маской"""
    if account_number_card[-20:].isdigit():
        mask_account_card = account_number_card[:5] + "**" + account_number_card[-4:]
    else:
        card_number = account_number_card[-16:]
        name_card = account_number_card[:-16]
        card_number_mask = (card_number[:4] + " " +
                            card_number[4:6] + "** **** " + card_number[-4:])
        mask_account_card = name_card + card_number_mask
    return mask_account_card


def get_date():
    pess