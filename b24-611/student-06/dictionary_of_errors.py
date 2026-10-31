def count_error_codes(error_codes: list[int]) -> dict[int, int]:
    error_counts = {}

    for error_code in error_codes:
        if error_code in error_counts:
            error_counts[error_code] = error_counts[error_code] + 1
        else:
            error_counts[error_code] = 1

    return error_counts


codes_of_errors = (input("Введите коды ошибок через пробел: ")).split()
error_counts = count_error_codes(codes_of_errors)

print(error_counts)
