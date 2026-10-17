#System imports

#External imports

#User imports
from user_access import(
    STATUS_ADMIN_AUTH
    STATUS_USER_AUTH
    STATUS_AUTH_FAILED
    register_user
    auth_account
)
from user_data import users, admins

###########################

def print_menu()->None:
    print()
    print('Выберите действия')
    print('1 - Зарегистрироваться')
    print('2 - Вход в систему')
    print('3 - Завершить работу')

def process_registration(
    users: dict[str, str],
    admins: dict[str, str],
) -> None:
    login = input('Введите логин: ')
    password = input('Введите пароль: ')

    if register_users(users, admins, login, password):
        print(f"Пользователь {login} зарегестрирован")
    else:
        print ("Такой логин уже существует")

def proccess_login(
    users: dict[str, str],
    admins: dict[str, str],
) -> None:
    auth_status = auth_account(users, admins, login, password)
    if auth_status == STATUS_ADMIN_AUTH:
        print(f'Привет {login} вы вошли как администратор')
        for user_login, user_password in users.items():
            print(f'Login {login}  Password {password}')
    elif auth_status == STATUS_USER_AUTH:
        print(f'Привет {login} вы вошли как пользователь')
    elif auth_status == STATUS_AUTH_FAILED:
        print(f'Неверный логин или пароль')
    else:
        print(f'Unknown status {admin_status}')
        exit(1)
    def main()-> None:
        while True:
            print_menu()
            menu.item = input()

        if menu.item == 1:
            process_registration(users, admins)
        elif menu.item == 2:
            process_login(users, admins)
        elif menu.item == 0:
            print('Завершение работы программы')
        else:
           print ('Неизвестный пункт меню')
main()
