import importlib.util

def load_module(file_name, module_name):
    spec = importlib.util.spec_from_file_location(module_name, file_name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

zad1 = load_module("Zad 1.py", "zad1")
zad2 = load_module("zad 2.py", "zad2")
zad3 = load_module("zad 3.py", "zad3")
zad4 = load_module("zad 4.py", "zad4")
zad5 = load_module("zad 5.py", "zad5")

def run_tests():
    assert zad1.count_positive([1, -2, 3, 0, 5]) == 3
    assert zad1.count_positive([-1, -2]) == 0
    print("Задание 1: OK")

    assert zad2.filter_above_threshold([1, 5, 2, 8, 3], 4) == [5, 8]
    assert zad2.filter_above_threshold([1, 2], 10) == []
    print("Задание 2: OK")

    assert zad3.count_error_codes(['A', 'B', 'A', 'C', 'A']) == {'A': 3, 'B': 1, 'C': 1}
    assert zad3.count_error_codes([]) == {}
    print("Задание 3: OK")

    assert zad4.count_unique_sensors([1, 2, 2, 3, 1]) == 3
    assert zad4.count_unique_sensors([]) == 0
    print("Задание 4: OK")

    assert zad5.add_item(1) == [1]
    assert zad5.add_item(2) == [2]
    assert zad5.add_item(3, [10]) == [10, 3]
    print("Задание 5: OK")

    print("\nВсе тесты успешно пройдены!")

if __name__ == "__main__":
    run_tests()
