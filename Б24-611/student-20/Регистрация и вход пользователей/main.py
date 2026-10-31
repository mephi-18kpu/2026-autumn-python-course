# System imports

# External imports

# User imports
from User-data import USERS, ADMINS
from user_acsess import (
    STATUS_AUTH_FAILED,
    STATUS_ADMIN_AUTH,
    STATUS_USER_AUTH,
    register_user,
    auth_account
)

#############################################

def print_menu() -> None:
    """main menu of the programm"""
    print()
    print("Выберите действие")
    print("1 - зврегистрироваться")
    print("2 - вход в систему")
    print("3 - завершить работу")


def process_registration(
    users: dict[str, str],
    admins: dict[str, str],
) -> None:
    """Запрос данных пользователя и валидация"""
    login = input("Введите логин")
    password = input("Введите пароль")

    if register_user(users, admins, login, password):
        print(f"Пользователь {login} зарегистрирован")
    else:
        print("Пользователь с таким логином уже существует")


def process_login(
    users: dict[str, str],
    admins: dict[str, str],
) -> None:
    """Запрос данных пользователя и вход в систему"""
    login = input("Введите логин")
    password = input("Введите пароль")


    auth_status = auth_account(users, admins, login, password)
    if auth_status == STATUS_ADMIN_AUTH:
        print(f"Привет {login}! Вы воли как администратор. \n"
              f"Зарегистрированные пользователи:")
    for user_login, user_password in users.items():
        print(f"Логин - {user_login}, пароль - {user_password}")

    elif auth_status == STATUS_USER_AUTH:
        print("Привет")

    elif auth_status == STATUS_AUTH_FAILED:
        print("Регистрация провалена")

    else:
        print(f"Неизвестный статус: {auth_status}")
        exit(1)

def main() -> None:
    while True:
        print_menu()
        menu_item = input("Выберите действие")

        if menu_item == '1':
            process_registration(USERS, ADMINS)
        elif menu_item == '2':
            process_login(USERS, ADMINS)
        elif menu_item == '0':
            print("Завершение работы программы")
            return
        elif:
            print("Неизвестный пункт меню")

main()


