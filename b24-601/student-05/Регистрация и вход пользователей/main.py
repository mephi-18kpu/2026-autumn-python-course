from user_acccess import (STATUS_ADMIN_AUTH, STATUS_AUTH_FAILED, STATUS_USER_AUTH, register_user, authenticate_account)
from user_data import USER, ADMINISTRATOR
def print_menu() -> None:
    print()
    print("Выберите действие:")
    print("1 - Зарегистрироваться")
    print("2 - Войти в систему")
    print("0 - Завершить работу")
def process_registration(
    users: dict[str, str],
    admins: dict[str, str]) -> None:
    login = input("Введите логин:")
    password = input("Введите пароль:")
    if register_user(users, admins, login, password):
        print(f'Пользователь {login} зарегестрирован')
    else:
        print('Пользователь уже существует!')
def process_login(
    users: dict[str, str],
    admins: dict[str, str]
) -> None:
    login = input("Введите логин:")
    password = input("Введите пароль:")
    status = authenticate_account(users, admins, login, password)
    if status == STATUS_ADMIN_AUTH:
        print(f'Привет, {login}! Вы вошли как администратор.\n'
              f'Зарегестрированные пользователи:')
        for user_login, user_password in users.items():
            print(f'Логин: {user_login}, пароль: {user_password}')
    elif status == STATUS_USER_AUTH:
        print(f'Привет, {login}! Вы вошли в систему.')
    elif status == STATUS_AUTH_FAILED:
        print('Неверный логин или пароль.')
    else:
        print(f"Неизвестный статус {status}! Завершение программы")
        exit(1)
def main() -> None:
    while True:
        print_menu()
        menu_item = input('Выберите действие:')
        if menu_item == '1':
            process_registration(USER, ADMINISTRATOR)
        if menu_item == '2':
            process_login(USER, ADMINISTRATOR)
        if menu_item == '0':
            print("Завершение работы программы.")
            break
        else:
            print('Неизвстный ввод')
main()
