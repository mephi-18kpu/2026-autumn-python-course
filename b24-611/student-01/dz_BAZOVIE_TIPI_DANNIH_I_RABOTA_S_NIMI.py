def count_positive_measurements(izmereniya: list[float]) -> int:
    kolichestvo_polozhitelnyh = 0
    for izmerenie in izmereniya:
        if izmerenie > 0.0:
            kolichestvo_polozhitelnyh = kolichestvo_polozhitelnyh + 1
    return kolichestvo_polozhitelnyh


def select_high_measurements(izmereniya: list[float], porog: float) -> list[float]:
    vysokie_izmereniya = []
    for izmerenie in izmereniya:
        if izmerenie > porog:
            vysokie_izmereniya.append(izmerenie)
    return vysokie_izmereniya


def count_error_codes(kody_oshibok: list[int]) -> dict[int, int]:
    schetchik_oshibok = {}
    for kod in kody_oshibok:
        if kod in schetchik_oshibok:
            schetchik_oshibok[kod] = schetchik_oshibok[kod] + 1
        else:
            schetchik_oshibok[kod] = 1
    return schetchik_oshibok


if __name__ == "__main__":
    izmereniya_1 = [-2.0, 0.0, 3.5, 7.1]
    rezultat_1 = count_positive_measurements(izmereniya_1)
    print("Задание 1:")
    print(rezultat_1)
    print()

    izmereniya_2 = [12.5, 31.0, 28.4, 35.2]
    rezultat_2 = select_high_measurements(izmereniya_2, 30.0)
    print("Задание 2:")
    print(rezultat_2)
    print()

    kody = [101, 205, 101, 404, 205, 101]
    rezultat_3 = count_error_codes(kody)
    print("Задание 3:")
    print(rezultat_3)
    print()

    nazvaniya_datchikov = [
        "температура",
        "давление",
        "температура",
        "скорость",
        "давление",
    ]
    unikalnye_datchiki = set(nazvaniya_datchikov)
    print("Задание 4:")
    print(unikalnye_datchiki)
    print(f"Количество различных датчиков: {len(unikalnye_datchiki)}")
    print()

    pervyy_spisok = [1, 2]
    vtoroy_spisok = pervyy_spisok.copy()
    vtoroy_spisok.append(3)
    print("Задание 5:")
    print(f"Первый список: {pervyy_spisok}")
    print(f"Второй список: {vtoroy_spisok}")
