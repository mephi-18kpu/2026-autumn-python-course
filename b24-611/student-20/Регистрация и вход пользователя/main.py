import logging

from user_data import USERS, ADMINS
from user_access import *

def print_menu() -> None:
    """ввод главного меню программы"""
    print("Что будем делать?")
    print("1 — Зарегистрироваться")
    print("2 — Войти в систему")
    print("0 — Завершить работу")

def procces_regisration(
    users: dict[str, str],
    admins: dict[str, str]
) -> None:
    """Запрос данных пользователя"""
    login = input("Введите login:")
    password= input("Введите пароль:")

    if register_user(users, admins, login, password):
        print(f"Пользователь {login} зареган")
    else:
        print("Ник занят")

def procces_login(
    users: dict[str, str],
    admins: dict[str, str]
) -> None:
    """Запрос данных пользователя"""
    login = input("Введите login")
    password = input("Введите пароль")

    auth_status = auth_account(users, admins, login, password)

    if auth_status == STATUS_ADMIN_AUTH:
        print(f"Админ {login} в сети")
        for users_login, user_password in users.items():
            print(f"Login: {users_login}, parol: {user_password}")

    elif auth_status == STATUS_USER_AUTH:
        print(f"Zdarova {login}")

    elif auth_status == STATUS_AUTH_FAILED:
        print(f"Неверный логин или пароль")

    else:
        print(f"Error: {auth_status}")
        exit(1)

def main() -> None:
    while True:
        print_menu()
        menu_item = input("Выберите действие:")

        if menu_item == "1":
            procces_regisration(USERS, ADMINS)
        elif menu_item == "2":
            procces_login(USERS, ADMINS)
        elif menu_item == "0":
            print("Пока пока")
            break
        else:
            print("Я уже красный, культурно не получится")

if __name__ == "__main__":
    main()
