def count_error_codes(error_codes:list):
    error_counts =dict()
    for i in error_codes:
        if i in error_counts:
            error_counts[i]= error_counts[i]+1
        else:
            error_counts.update({i:1})
    return error_counts


error_codes = [101, 205, 101, 404, 205, 101]
print(count_error_codes(error_codes))