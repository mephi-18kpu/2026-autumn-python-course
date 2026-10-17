# System imports

# External imports

# User imports
import generation
import measure_time_execution as time_measure
import sort_algorithms as sa
import bin_search as bs

#############################################

def main() ->None:
    """ Сортировка пузырьком """
    numbers = generation.generate_values(50,0, 100)
    bubble_sorted_numbers, bubble_execution_time = time_measure.measure_execution(sa.bubble_sort, numbers.copy())
    print(f"===== СОРТИРОВКА ПУЗЫРЬКОМ =====\n"
          f"Неотсортированный список: {numbers}\n"
          f"Отсортированный список: {bubble_sorted_numbers}\n"
          f"Время выполнения: {bubble_execution_time}\n")

    """ Шейкерная сортировка """
    cocktail_sorted_numbers, cocktail_execution_time = time_measure.measure_execution(sa.cocktail_sort, numbers.copy())
    print(f"===== ШЕЙКЕРНАЯ СОРТИРОВКА =====\n"
          f"Неотсортированный список: {numbers}\n"
          f"Отсортированный список: {cocktail_sorted_numbers}\n"
          f"Время выполнения: {cocktail_execution_time}\n")

    """ Гномья сортировка """
    gnome_sorted_numbers, gnome_execution_time = time_measure.measure_execution(sa.gnome_sort, numbers.copy())
    print(f"===== ГНОМЬЯ СОРТИРОВКА =====\n"
          f"Неотсортированный список: {numbers}\n"
          f"Отсортированный список: {gnome_sorted_numbers}\n"
          f"Время выполнения: {gnome_execution_time}\n")

    """ Глупая сортировка """
    stupid_sorted_numbers, stupid_execution_time = time_measure.measure_execution(sa.stupid_sort, numbers.copy())
    print(f"===== ГЛУПАЯ СОРТИРОВКА =====\n"
          f"Неотсортированный список: {numbers}\n"
          f"Отсортированный список: {stupid_sorted_numbers}\n"
          f"Время выполнения: {stupid_execution_time}\n")

    """ Чётная-нечётная сортировка """
    odd_even_sorted_numbers, odd_even_execution_time = time_measure.measure_execution(sa.odd_even_sort, numbers.copy())
    print(f"===== ЧЁТНАЯ-НЕЧЁТНАЯ СОРТИРОВКА =====\n"
          f"Неотсортированный список: {numbers}\n"
          f"Отсортированный список: {odd_even_sorted_numbers}\n"
          f"Время выполнения: {odd_even_execution_time}\n")

    """ Сортировка расчёской """
    comb_sorted_numbers, comb_execution_time = time_measure.measure_execution(sa.comb_sort, numbers.copy())
    print(f"===== СОРТИРОВКА РАСЧЁСКОЙ =====\n"
          f"Неотсортированный список: {numbers}\n"
          f"Отсортированный список: {comb_sorted_numbers}\n"
          f"Время выполнения: {comb_execution_time}\n")

    """ Сортировка вставками """
    insertion_sorted_numbers, insertion_execution_time = time_measure.measure_execution(sa.insertion_sort, numbers.copy())
    print(f"===== СОРТИРОВКА ВСТАВКАМИ =====\n"
          f"Неотсортированный список: {numbers}\n"
          f"Отсортированный список: {insertion_sorted_numbers}\n"
          f"Время выполнения: {insertion_execution_time}\n")

    """ Сортировка Шелла """
    shell_sorted_numbers, shell_execution_time = time_measure.measure_execution(sa.shell_sort,numbers.copy())
    print(f"===== СОРТИРОВКА ШЕЛЛА =====\n"
          f"Неотсортированный список: {numbers}\n"
          f"Отсортированный список: {shell_sorted_numbers}\n"
          f"Время выполнения: {shell_execution_time}\n")

    """ Бинарный поиск """
    target_index, execution_time = time_measure.measure_execution(bs.bin_search,
                                                                                shell_sorted_numbers,
                                                                                int(input("Введите число которое необходимо найти: ")))
    print(f"===== БИНАРНЫЙ ПОИСК =====\n"
          f"Число: {shell_sorted_numbers[target_index]} находится на {target_index + 1} месте\n"
          f"Время выполнения: {execution_time}\n")
main()
