# System imports
# External imports
# User imports
from user_access import *
from user_data import USERS, ADMIN
####################################

def start_menu() -> None:
    print("Выберите желаемое действие")
    print("0 - выход")
    print("1 - регистрация")
    print("2 - авторизация")

def user_sing_in(users: dict[str,str], admin: dict[str, str]) -> None:
    print("Выбрано: регистрация")
    print("Введите желаемый логин: ")
    login = input()
    print("Введите желаемый пароль: ")
    pasword = input()

    if sign_in(USERS, ADMIN, login, pasword):
        print(f"Регистрация пользователя {login} успешна")
    else:
        print(f"Пользователь зарегистрирован ранее")

def user_log_in(users: dict[str,str], admin: dict[str, str]) -> None:
    print("Выбрано: аторизация")
    print("Введите логин: ")
    login = input()
    print("Введите пароль: ")
    pasword = input()

    if log_in(USERS, ADMIN, login, pasword) == "USER_AUTH" :
        print(f"Aвторизация пользователя {login} успешна")
    elif log_in(USERS, ADMIN, login, pasword) == "AUTH_AUTH":
        print(f"Aвторизация администратора успешна")
        for user_login, user_pasword in users:
            print(f"Логин: {user_login}  Пароль: {user_pasword}")
    else:
        print(f"Неизвестный пользователь")


def main() -> None:
    start_menu()
    i = int(input("Выберите пункт "))
    while True:
        if i == 0:
            print("Завершение....")
            return
        elif i == 1:
            user_sing_in(USERS, ADMIN)
        elif i == 2:
            user_log_in(USERS, ADMIN)
        else:
            print("Неизвестное действие")

main()
