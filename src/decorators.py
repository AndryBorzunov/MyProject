from functools import wraps
from typing import Any


def log(filename: str | None = None) -> Any:
    """Декоратор для записи логов выполнения фуекции"""

    def wrapper(function: Any) -> Any:
        """Обертка для функции"""

        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> Any:
            """Внутренняя функция, реализующая запись лога"""

            result = None
            try:
                result = function(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"INFO: {function.__name__} ok: Inputs: {args[0]}, {args[1]}. Outputs: {result}\n")
                else:
                    print(f"INFO: {function.__name__} ok: Inputs: {args[0]}, {args[1]}. Outputs: {result}")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(
                            f"ERROR: {function.__name__} error: {e}. Inputs: {args[0]}, {args[1]}. Outputs: {result}\n"
                        )
                else:
                    print(f"ERROR: {function.__name__} error: {e}. Inputs: {args[0]}, {args[1]}. Outputs: {result}")
                return result

        return inner

    return wrapper
