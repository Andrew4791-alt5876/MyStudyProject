from datetime import datetime
from src import widget


def filter_by_state(info_about_users: list, state: str = "EXECUTED") -> list:
    pass


def sort_by_date(info_about_users: list) -> list:
    info_sort = []
    info_users_date = [item.copy() for item in info_about_users]
    for info_date in info_users_date:
        info_only_date = widget.get_date(info_date["date"])
        info_date["date"] = info_only_date
    new_users_date_sort = sorted(info_users_date, reverse=True, key=lambda x: datetime.strptime(x["date"], "%d.%m.%Y"))
    for info_about_user in info_about_users:
        for new_user_date_sort in new_users_date_sort:
            if widget.get_date(info_about_user["date"]) == new_user_date_sort["date"]:
                new_user_date_sort["date"] = info_about_user["date"]
    return new_users_date_sort


info_about_users = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(sort_by_date(info_about_users))
