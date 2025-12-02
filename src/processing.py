from datetime import datetime


def filter_by_state(users_info_state: list, state: str = "EXECUTED") -> list:
    """Функция, которая возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению"""
    filter_users_state = []
    for user_info_state in users_info_state:
        if user_info_state["state"] == "EXECUTED" and state != "CANCELED":
            filter_users_state.append(user_info_state)
        elif user_info_state["state"] == "CANCELED" and state == "CANCELED":
            filter_users_state.append(user_info_state)
    return filter_users_state


def sort_by_date(info_about_users: list) -> list:
    """Функция, которая сортирует входные данные по дате"""
    sort_by_date = sorted(
        info_about_users, reverse=True, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f")
    )
    return sort_by_date
