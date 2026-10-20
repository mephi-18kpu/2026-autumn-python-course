"""Запуск упрощённой программы регистрации и входа пользователей."""

# System imports

# External imports

# User imports
from users_data import ADMINISTRATORS, USERS
from user_access import (
    STATUS_ADMINISTRATOR_AUTHENTICATED,
    STATUS_USER_AUTHENTICATED,
    authenticate_account,
    register_user
)

#############################################


def print_menu() -> None:
    """Выводит главное меню программы."""
    print()
    print(f"Выберите действие:")
    print(f"1 — Зарегистрироваться")
    print(f"2 — Войти в систему")
    print(f"0 — Завершить работу")


def process_registration(users: dict[str, str], administrators: dict[str, str]) -> None:
    """Запрашивает данные и регистрирует пользователя.

    Args:
        users: Словарь обычных пользователей.
        administrators: Словарь администраторов.
    """
    login = input(f"Введите новый логин: ")
    password = input(f"Введите новый пароль: ")

    if register_user(users, administrators, login, password):
        print(f"Пользователь {login} зарегистрирован.")
    else:
        print(f"Пользователь с таким логином уже существует.")


def process_login(users: dict[str, str], administrators: dict[str, str]) -> None:
    """Запрашивает данные и выполняет вход в систему.

    Args:
        users: Словарь обычных пользователей.
        administrators: Словарь администраторов.
    """
    login = input(f"Введите логин: ")
    password = input(f"Введите пароль: ")

    authentication_status = authenticate_account(
        users,
        administrators,
        login,
        password,
    )

    if authentication_status == STATUS_ADMINISTRATOR_AUTHENTICATED:
        print(f"Привет, {login}! Вы вошли как администратор.")
        print(f"Зарегистрированные пользователи:")

        for user_login in users:
            print(f"- {user_login}")
    elif authentication_status == STATUS_USER_AUTHENTICATED:
        print(f"Привет, {login}! Вы успешно вошли в систему.")
    else:
        print(f"Неверный логин или пароль.")


def main() -> None:
    """Запускает основной цикл программы."""
    while True:
        print_menu()
        menu_item = input(f"Выберите действие: ")

        if menu_item == "1":
            process_registration(USERS, ADMINISTRATORS)
        elif menu_item == "2":
            process_login(USERS, ADMINISTRATORS)
        elif menu_item == "0":
            print(f"Работа программы завершена.")
            return
        else:
            print(f"Неизвестный пункт меню.")


if __name__ == "__main__":
    main()
