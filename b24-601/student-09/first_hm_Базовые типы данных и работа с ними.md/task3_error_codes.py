"""Подсчёт количества появлений каждого кода ошибки."""

def count_error_codes(error_codes: list[int]) -> dict[int, int]:
    """Возвращает словарь: код ошибки — количество появлений."""
    error_counts = {}

    for error_code in error_codes:
        if error_code in error_counts:
            error_counts[error_code] += 1
        else:
            error_counts[error_code] = 1

    return error_counts


raw_error_codes = input("Введите коды ошибок через пробел: ")
error_codes = [int(value) for value in raw_error_codes.split()]

error_counts = count_error_codes(error_codes)
print("Количество появлений кодов:")
print(error_counts)
