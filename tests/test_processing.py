from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_canceled(info_users_state: list, filter_users_state_canceled: list) -> None:
    """Тест для статуса 'CANCELED'."""
    assert filter_by_state(info_users_state, state="CANCELED") == filter_users_state_canceled


def test_filter_by_state_executed(info_users_state: list, filter_users_state_executed: list) -> None:
    """Тест для статуса 'EXECUTED'."""
    assert filter_by_state(info_users_state, state="EXECUTED") == filter_users_state_executed


def test_filter_by_state_executed_empty(info_users_state: list, filter_users_state_executed: list) -> None:
    """Тест для неопределенного статуса."""
    assert filter_by_state(info_users_state, state="") == filter_users_state_executed


def test_filter_by_state_executed_wrong(info_users_state: list, filter_users_state_executed: list) -> None:
    """Тест для не верного статуса."""
    assert filter_by_state(info_users_state, state="hfwhvfWH") == filter_users_state_executed


def test_sort_by_date(sort_by_date_enter: list, sort_by_date_exit: list) -> None:
    """Тест для преобразования даты."""
    assert sort_by_date(sort_by_date_enter) == sort_by_date_exit
