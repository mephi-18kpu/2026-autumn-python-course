# search_linear.py
def linear_search(values: list[int], target: int) -> int | None:
    for index, value in enumerate(values):
        if value == target:
            return index
    return None