"""Запускает упрощённую программу регистрации и входа."""

# System imports

# External imports

# User imports
from user_access import STATUS_ADMINISTRATOR_AUTH
from user_access import STATUS_USER_AUTH
from user_access import STATUS_AUTHENTICATION_FAILED
from user_access import authenticated_account
from user_access import register_user
from user_data import USERS, ADMINISTRATOR

#############################################

def print_menu() -> None:
    """Вывод меню пользователя."""

    print()
    print("Выберете действие:")
    print("1 - Зарегистрироваться.")
    print("2 - Войти в систему.")
    print("0 - Завершить работу.")

def process_registration(
    users: dict[str, str],
    admins: dict[str, str]
) -> None:
    """ Регистрация пользователя."""

    login = input("Введите логин: ")
    password = input("Введите пароль.")

    if register_user(users, admins, login, password):
        print(f" Пользователь {login} зарегистрирован.")
    else:
        print("Пользователь с таким логином уже существует.")

def process_login(
users: dict[str, str],
    admins: dict[str, str]
) -> None:
    """ Проверка логина и пароля и вход в систему. """

    login = input("Введите логин: ")
    password = input("Введите пароль.")

    status = authenticated_account( users, admins, login, password)

    if status == STATUS_USER_AUTH:
        print(f"Привет, {login}! Вы вошли как администратор. \n"
              f"арегестрированные пользователи."
              )
        for user_login, user_password in users.items():
            print(f"Логин: {user_login}, пароль: {user_password}")
    elif status == STATUS_ADMINISTRATOR_AUTH:
        print(f"Привет, {login}! Вы вошли в систему.")
    elif status == STATUS_AUTHENTICATION_FAILED:
        print("Неверный логин или пароль.")
    else:
        print(f"Неизвестный статус {status}! Завершение программы.")
        exit(1)

def main() -> None:
    """Запуск основного цикла программы"""

    while True:
        print_menu()
        menu_item = input("Выберите действие:")

        if menu_item == "1":
            process_registration(USERS, ADMINISTRATOR)
        elif menu_item == "2":
            process_login(USERS, ADMINISTRATOR)
        elif menu_item == "0":
            print("Завершение работы программы.")
            return
        else:
            print("Неизвестный ввод.")

if __name__ == "__main__":
    main()
