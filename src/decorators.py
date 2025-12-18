from time import time
from typing import Any, Callable


def log(filename: Any | None = None) -> Any:
    """Внешняя функция, которая принимает аргумент для декоратора и возвращает внутренний декоратор."""

    def decorator(func: Callable) -> Callable:
        """Декоратор, который автоматически регистрирует детали выполнения функций."""

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Функция-обертка, которая логирует детали выполнения функции."""
            try:
                start_time = time()
                resalt = func(*args, **kwargs)
                end_time = time()
                time_of_work = end_time - start_time
                resalt_log = f"Функция {func.__name__} is OK\n" f"Время выполнения функции: {time_of_work}"
                if filename == "mylog.txt":
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(resalt_log + "\n")
                else:
                    print(resalt_log)
                return resalt
            except Exception as e:
                error_type = type(e).__name__
                log_message = (
                    f"Функция {func.__name__}, " f"Ошибка: {error_type}, " f"Входные аргументы: {args}, {kwargs}"
                )
                if filename == "mylog.txt":
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message + "\n")
                    return log_message
                else:
                    print(log_message)

        return wrapper

    return decorator
