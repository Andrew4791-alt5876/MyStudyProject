from datetime import datetime


def filter_by_state(users_info_state: list, state: str) -> list:
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


# state = "CANCELED"
# users_info_state = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]
# print(filter_by_state(users_info_state, state))
#
#
# info_about_users = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]
# print(sort_by_date(info_about_users), state)
