def count_error_codes(codes):
    counts = {}
    for code in codes:
        counts[code] = counts.get(code, 0) + 1
    return counts
