import time
from collections.abc import Callable


def make_report(zagolovok: str, *znacheniya: float, edinitsa: str = "В", **metadannye: str) -> str:
    if not znacheniya:
        srednee = "нет данных"
    else:
        srednee = f"{sum(znacheniya) / len(znacheniya):.2f}"

    stroki_otcheta = [
        f"Заголовок: {zagolovok}",
        f"Количество значений: {len(znacheniya)}",
        f"Среднее значение: {srednee} {edinitsa}"
    ]

    if metadannye:
        stroka_metadannyh = ", ".join(f"{klyuch}={znach}" for klyuch, znach in metadannye.items())
        stroki_otcheta.append(f"Дополнительно: {stroka_metadannyh}")

    return "\n".join(stroki_otcheta)


def measure_execution_time(funktsiya: Callable[..., object], *pozitsionnye, **imenovannye) -> tuple[object, float]:
    vremya_starta = time.time()
    rezultat = funktsiya(*pozitsionnye, **imenovannye)
    vremya_okonchaniya = time.time()
    return rezultat, vremya_okonchaniya - vremya_starta


if __name__ == "__main__":
    print("=== Вызов 1 ===")
    otchet_1 = make_report("Тест 1", 5.0, 6.0, 5.5, edinitsa="мВ", source="датчик", room="лаборатория")
    print(otchet_1)
    print()

    print("=== Вызов 2 ===")
    spisok_znacheniy = [10.0, 20.0, 30.0, 40.0]
    slovar_metadannyh = {"source": "измеритель", "room": "склад", "operator": "Иванов"}
    otchet_2 = make_report("Тест 2", *spisok_znacheniy, edinitsa="кВ", **slovar_metadannyh)
    print(otchet_2)
    print()

    print("=== Вызов 3 ===")
    rezultat_zamera, vremya_vypolneniya = measure_execution_time(
        make_report,
        "Тест 3 (без замеров)",
        edinitsa="А",
        source="система"
    )
    print(rezultat_zamera)
    print(f"Время выполнения: {vremya_vypolneniya:.6f} сек.")
