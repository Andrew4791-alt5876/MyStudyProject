from datetime import datetime


def filter_by_state(users_info_state: list, state : str = "EXECUTED" ) -> list:
    """Функция возвращает новый список словарей у которых ключ state соответствует указанному значению"""
    filter_users_state = []
    for user_info_state in users_info_state:
        if isinstance(user_info_state, dict) and user_info_state.get("state") == state:
            filter_users_state.append(user_info_state)
    return filter_users_state


def sort_by_date(info_about_users: list) -> list:
    """Функция, которая сортирует входные данные по дате"""
    sort_by_date = sorted(
        info_about_users, reverse=True, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f")
    )
    return sort_by_date
