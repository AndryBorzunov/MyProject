from functools import wraps
from typing import Any


def log(filename: str | None = None) -> Any:
    """Декоратор для записи логов выполнения фуекции"""

    def wrapper(function: Any) -> Any:
        """Обертка для функции"""

        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> Any:
            """Внутренняя функция, реализующая запись лога"""

            try:
                result = function(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{function.__name__} ok: {function(*args, **kwargs)}")
                else:
                    print(f"{function.__name__} ok: {function(*args, **kwargs)}")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{function.__name__} error: {e}. Inputs: {function(*args, **kwargs)}")
                else:
                    print(f"{function.__name__} error: {e}. Inputs: {function(*args, **kwargs)}")
                raise e

        return inner

    return wrapper
