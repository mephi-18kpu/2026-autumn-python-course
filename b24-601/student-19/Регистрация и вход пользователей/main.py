"""Запускает упрощённую программу регистрации и входа."""

# System imports

# External imports

# User imports
from user_access import (
    STATUS_ADMINISTRATOR_AUTHENTICATED,
    STATUS_USER_AUTHENTICATED,
    STATUS_AUTHENTICATION_FAILED,
    register_user,
    authenticate_account,
)
from user_data import ADMIN, USER


#############################################


def print_menu() -> None:
    """Выводит главное меню программы."""
    print()
    print("Выберите действие:")
    print("1 — Зарегистрироваться")
    print("2 — Войти в систему")
    print("0 — Завершить работу")


def process_registration(
    users: dict[str, str],
    administrators: dict[str, str],
) -> None:
    login = input("Введите новый логин: ")
    password = input("Введите новый пароль: ")

    if register_user(users, administrators, login, password):
        print(f"Пользователь {login} зарегистрирован.")
    else:
        print("Пользователь с таким логином уже существует.")


def process_login(
    users: dict[str, str],
    administrators: dict[str, str],
) -> None:

    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    status = authenticate_account(
        users,
        administrators,
        login,
        password,
    )

    if status == STATUS_ADMINISTRATOR_AUTHENTICATED:
        print(f"Привет, {login}! Вы вошли как администратор.\n" f"Зарегистрированные пользователи:")
        for user_login, user_password in users.items():
            print(f"Логин: {user_login}, пароль: {user_password}")
    elif status == STATUS_USER_AUTHENTICATED:
        print(f"Привет, {login}! Вы успешно вошли в систему.")
    elif status == STATUS_AUTHENTICATION_FAILED:
        print("Неверный логин или пароль.")
    else:
        print(f"Неизвестный статус {status}! Завершение программы")
        exit(1)


def main() -> None:
    """Запускает основной цикл программы."""
    while True:
        print_menu()
        menu_item = input("Выберите действие: ")

        if menu_item == "1":
            process_registration(USER, ADMIN)
        elif menu_item == "2":
            process_login(USER, ADMIN)
        elif menu_item == "0":
            print("Работа программы завершена.")
            return
        else:
            print("Неизвестный пункт меню.")


main()
