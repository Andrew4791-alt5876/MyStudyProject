from time import time
from typing import Any


def log(filename: Any | None = None) -> Any:
    """Внешняя функция, которая принимает аргумент для декоратора и возвращает внутренний декоратор decorator."""
    def decorator(func: Any) -> Any:
        """Декоратор, который автоматически регистрирует детали выполнения функций. Возвращает wrapper."""
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Функция-обертка wrapper, которая определяет детали выполнения функции."""
            try:
                start_time = time()
                resalt = func(*args, **kwargs)
                end_of_time = time()
                time_of_work = end_of_time - start_time
                resalt_log = (
                    f"Функция {func.__name__} is OK\n"
                    f"Время работы функции: {time_of_work}\n"
                    f"Передаваемые аргументы: {args}, {kwargs}\n"
                    f"Результат функции: {resalt}"
                )
                if filename == "mylog.txt":
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(resalt_log)
                else:
                    print(resalt_log)
            except Exception as e:
                error_type = type(e).__name__
                log_message = f"Функция {func.__name__} error: {error_type}. Inputs: {args}, {kwargs}"
                if filename == "mylog.txt":
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(log_message)
                else:
                    print(log_message)
        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x: Any, y: Any) -> Any:
    '''Функция для декорирования.'''
    return x / y


my_function(20, 3)
