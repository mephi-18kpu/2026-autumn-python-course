"""Шапка которую перепишу потом"""


#User imports
from user_access import (
    STATUS_FAILED_AUTH,
    STATUS_USER_AUTH,
    STATUS_ADMIN_AUTH,
    register_user,
    authenticate_account)
from user_data import USERS, ADMINISTRATOR

####################################

def print_menu() -> None:
    print("\nВыберите действие:\n"
          "1 - Зарегистрироваться\n"
          "2 - Войти в систему\n"
          "0 - Завершить работу")

def process_registration(
        users: dict[str, str],
        admins: dict[str, str]
) -> None:
    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    if register_user(users, admins, login, password):
        print(f"Пользователь {login} зарегистрирован")
    else:
        print(f"Пользователь {login} уже существует")


def process_login(
        users: dict[str, str],
        admins: dict[str, str]
) -> None:
    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    status = authenticate_account(users, admins, login, password)

    if status == STATUS_USER_AUTH:
        print(f"Привет, {login}. Вы успешно авторизовались")
    elif status == STATUS_ADMIN_AUTH:
        print(f"Привет, {login}. Вы вошли как администратор.\n"
              f"Зарегистрированные пользователи:")
        for user_login, user_pass in users.items():
            print(f"Логин: {user_login} Пароль: {user_pass}")
    elif status == STATUS_FAILED_AUTH:
        print("Неверный логин или пароль")
    else:
        print(f"Неизвестный статус {status}. Завершение работы")
        exit(1)

def main() -> None:
    while True:
        print_menu()
        command = int(input("Выберите действие: "))
        if command == 1:
            process_registration(USERS, ADMINISTRATOR)
        elif command == 2:
            process_login(USERS, ADMINISTRATOR)
        elif command == 0:
            exit(0)
        else:
            print("Неверная комманда. Повторите ввод")

main()