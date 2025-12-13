from time import time


def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                start_time = time()
                resalt = func(*args, **kwargs)
                end_of_time = time()
                time_of_work = end_of_time - start_time
                resalt_log = (
                    f"Функция {func.__name__} is OK\n"
                    f"Начало работы функции {start_time}\n"
                    f"Конец работы функции {end_of_time}\n"
                    f"Время работы функции {time_of_work}\n"
                    f"Результат функции {resalt}"
                )
                if filename == "mylog.txt":
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(resalt_log)
                else:
                    return resalt_log
            except Exception as e:
                error_type = type(e).__name__
                log_message = f"Функция {func.__name__} error: {error_type}. Inputs: {args}, {kwargs}"
                if filename == "mylog.txt":
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(log_message)
                else:
                    return log_message
        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x / y


print(my_function(5, 5))
