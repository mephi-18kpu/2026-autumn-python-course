from user_access import(
    STATUS_AUTH_FAILED,
    STATUS_USER_AUTH,
    STATUS_ADMIN_AUTH,
    register_user,
    auth_account
)
from user_data import USERS, ADMINS

def print_menu() -> None:
    """Вывод главного меню программы"""
    print()
    print("Выберите действие")
    print("1 - Зарегестрироваться")
    print("2 - Вход в систему")
    print("0 - Завершить работу")


def process_registration(
    users: dict[str, str],
    admins: dict[str, str]
) -> None:
    """Запрос данных пользователя и валидация"""
    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    if register_user(users, admins, login, password):
        print(f"Пользователь {login} зарегестрирован")
    else:
        print("Пользователь с таким логином уже существует")


def process_login(
    users: dict[str, str],
    admins: dict[str, str]
) -> None:
    """Запрос данных поьзователя и вход в систему"""
    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    auth_status = auth_account(users, admins, login, password)

    if auth_status == STATUS_ADMIN_AUTH:
        print(f"Привет, {login}! Вы вошли как администратор.\n"
              f"Зарегестрированные пользователи:")
        for user_login, user_password in users.items():
            print(f"Логин - {user_login}, пароль - {user_password}")
    elif auth_status == STATUS_USER_AUTH:
        print(f"Привет, {login}! Вы успешно вошли в систему.")

    elif auth_status == STATUS_AUTH_FAILED:
        print(f"Неверный логин или пароль")
    else:
        print(f"Неизвестный статус: {auth_status}")
        exit(1)

def main() -> None:
    while True:
        print_menu()
        menu_item = input("Выберите действие: ")

        if menu_item == "1":
            process_registration(USERS, ADMINS)
        elif menu_item == "2":
            process_login(USERS, ADMINS)
        elif menu_item == "0":
            print("Завершение работы программы")
            return
        else:
            print("Неизывестный пункт меню")

main()
