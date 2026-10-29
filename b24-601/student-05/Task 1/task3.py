def error_code_counter(error_codes: [int]) -> dict[int, int]:
    errors = {}
    for error_code in error_codes:
        if error_code in errors:
            errors[error_code] += 1
        else:
            errors[error_code] = 1
    return errors
error_codes = [101, 205, 101, 404, 205, 101]
print(error_code_counter(error_codes))
