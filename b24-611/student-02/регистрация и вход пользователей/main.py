from user_data import USERS, ADMINS
from user_access import (
    STATUS_AUTH_FAILED,
    STATUS_USER_AUTH,
    STATUS_ADMIN_AUTH,
    register_user,
    auth_account
)

def print_menu() -> None:
    """Вывод главного меню программы"""
    print()
    print("выбрать действие")
    print("1 - зарегистрироваться")
    print("2 - вход в систему")
    print("0 - завершить работу")


def process_registration(
    users: dict[str, str],
    admins: dict[str, str]
) -> None:
    """запрос данных пользователя и валидация"""
    login = input("введите логин")
    password = input("Введите пароль")

    if register_user(users, admins, login, password):
        print(f"пользователь {login} зарегистрирован")
    else:
        print(f'пользователь с таким именем уже существует')

def process_login(
    users: dict[str, str],
    admins: dict[str, str]
) -> None:
    """запрос данных пользователя и вход в систему"""
    login = input("введите логин: ")
    password = input("ведите пароль: ")

    auth_status = auth_account(users, admins, login, password)
    if auth_status == STATUS_ADMIN_AUTH
