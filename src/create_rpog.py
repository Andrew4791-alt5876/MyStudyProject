# from typing import Any, Generator
#
#
# def card_number_generator(start_number: int, finish_number: int) -> Generator[str, Any, None]:
#     """Генератор, который выдает номера банковских карт в заданном диапазоне."""
#     for number in range(start_number, finish_number + 1):
#         zero_str = "".join(["0" for z in range(16 - len(str(number))) if len(str(number)) <= 16])
#         card_number_str = zero_str + str(number)
#         card_number_exit = (
#             f"{card_number_str[:4]} {card_number_str[4:8]} {card_number_str[8:12]} {card_number_str[12:]}"
#         )
#         yield card_number_exit
#
#
# generator_card = card_number_generator(9000800070006000, 9000800070006020)
# for i in range(5):
#     print(list(generator_card))
#
# ['9000 8000 7000 6000', '9000 8000 7000 6001', '9000 8000 7000 6002', '9000 8000 7000 6003', '9000 8000 7000 6004']