# functions.py

from exceptions import NegativeNumberError, ZeroDivisionCustomError, InvalidRangeError

# Шаг 1: функции без обработки исключений
def calculate_square_root(number):
    """Возвращает квадратный корень числа. Шаг 1."""
    if number < 0:
        raise NegativeNumberError("Нельзя вычислить квадратный корень отрицательного числа.")
    return number ** 0.5

def divide_numbers(a, b):
    """Выполняет деление чисел. Шаг 1."""
    if b == 0:
        raise ZeroDivisionCustomError("Деление на ноль невозможно.")
    return a / b

# Шаг 2: обработчик общего типа исключений
def process_division(a, b):
    """Обрабатывает исключения при делении. Шаг 2."""
    try:
        result = divide_numbers(a, b)
        return result
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

# Шаг 3: обработчик исключений с блоком finally
def validate_and_process(value):
    """Проверяет значение и возвращает результат. Шаг 3."""
    try:
        if value < 0:
            raise NegativeNumberError("Значение не может быть отрицательным.")
        return value ** 2
    except Exception as e:
        print(f"Ошибка: {e}")
        return None
    finally:
        print("Завершение проверки.")

# Шаг 4: обработка разных типов исключений
def check_value_range(value):
    """Проверяет значение в определённом диапазоне. Шаг 4."""
    try:
        if value < 0:
            raise NegativeNumberError("Значение меньше нуля.")
        elif value > 100:
            raise InvalidRangeError("Значение превышает допустимый диапазон.")
        elif value == 0:
            raise ZeroDivisionCustomError("Значение не может быть нулём.")
        return f"Значение {value} корректно."
    except NegativeNumberError as e:
        print(f"Ошибка: {e}")
    except InvalidRangeError as e:
        print(f"Ошибка: {e}")
    except ZeroDivisionCustomError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Проверка завершена.")

# Шаг 5: генерация исключений внутри функции
def generate_exceptions(value):
    """Генерация исключений для разных случаев. Шаг 5."""
    try:
        if value == 0:
            raise ZeroDivisionCustomError("Нельзя использовать ноль.")
        elif value < 0:
            raise NegativeNumberError("Отрицательное значение недопустимо.")
        elif value > 50:
            raise InvalidRangeError("Слишком большое значение.")
        return value * 2
    except ZeroDivisionCustomError as e:
        print(f"Обработано исключение: {e}")
    except NegativeNumberError as e:
        print(f"Обработано исключение: {e}")
    except InvalidRangeError as e:
        print(f"Обработано исключение: {e}")
    finally:
        print("Функция завершена.")

# Шаг 6: пользовательские исключения
# Исключения определены в exceptions.py

# Шаг 7: пользовательское исключение с обработчиком
def check_positive_value(value):
    """Проверяет, что значение положительное. Шаг 7."""
    try:
        if value <= 0:
            raise NegativeNumberError("Число должно быть положительным.")
        return f"Число {value} положительное."
    except NegativeNumberError as e:
        print(f"Обработка: {e}")
    finally:
        print("Функция завершена.")

# Шаг 8: демонстрация исключений
def demo_func1(value):
    """Пример 1: Проверка числа. Шаг 8."""
    return check_positive_value(value)

def demo_func2(a, b):
    """Пример 2: Деление. Шаг 8."""
    return process_division(a, b)

def demo_func3(value):
    """Пример 3: Проверка диапазона. Шаг 8."""
    return check_value_range(value)
