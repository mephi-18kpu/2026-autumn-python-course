"""Запускает консольную регистрацию и проверку пользователей."""

# System imports
import logging

# External imports

# User imports
from config import CONFIG
from credentials_provider import CREDENTIALS_STATUS_SUCCESS
from credentials_provider import get_credentials
from logging_config import configure_logging
from user_access import (
    STATUS_ADMINISTRATOR_AUTHENTICATED,
    STATUS_EMPTY_LOGIN,
    STATUS_EMPTY_PASSWORD,
    STATUS_LOGIN_ALREADY_EXISTS,
    STATUS_PASSWORD_TOO_SHORT,
    STATUS_SUCCESS,
    STATUS_USER_AUTHENTICATED,
    authenticate_administrator,
    authenticate_user,
    register_user
)

#############################################


LOGGER = logging.getLogger(__name__)


def print_menu() -> None:
    """Выводит главное меню программы."""
    print()
    print(f"Выберите действие:")
    print(f"1 — Зарегистрироваться")
    print(f"2 — Войти в систему")
    print(f"0 — Завершить работу")


def process_registration(
    config: dict,
    users: dict[str, str],
    administrator: dict[str, str],
) -> None:
    """Запрашивает данные и регистрирует пользователя.

    Args:
        config: Конфигурация программы.
        users: Словарь обычных пользователей.
        administrator: Данные администратора.
    """
    login = input(f"Введите новый логин: ")
    password = input(f"Введите новый пароль: ")

    registration_status = register_user(
        config,
        users,
        administrator,
        login,
        password,
    )

    if registration_status == STATUS_SUCCESS:
        print(
            f"Пользователь {login} зарегистрирован. "
            f"Учётная запись будет доступна до завершения программы."
        )
    elif registration_status == STATUS_EMPTY_LOGIN:
        print(f"Логин не должен быть пустым.")
    elif registration_status == STATUS_LOGIN_ALREADY_EXISTS:
        print(f"Пользователь с таким логином уже существует.")
    elif registration_status == STATUS_EMPTY_PASSWORD:
        print(f"Пароль не должен быть пустым.")
    elif registration_status == STATUS_PASSWORD_TOO_SHORT:
        minimum_password_length = config["registration"]["minimum_password_length"]
        print(f"Пароль должен содержать не менее {minimum_password_length} символов.")


def request_credentials() -> tuple[str, str]:
    """Запрашивает логин и пароль.

    Returns:
        Кортеж с введёнными логином и паролем.
    """
    login = input(f"Введите логин: ")
    password = input(f"Введите пароль: ")
    return login, password


def process_login(
    users: dict[str, str],
    administrator: dict[str, str],
    login: str,
    password: str,
) -> str:
    """Проверяет введённые учётные данные.

    Args:
        users: Словарь обычных пользователей.
        administrator: Данные администратора.
        login: Введённый логин.
        password: Введённый пароль.

    Returns:
        Строковый статус проверки учётных данных.
    """
    if login == administrator["login"]:
        return authenticate_administrator(
            administrator,
            login,
            password,
        )

    return authenticate_user(
        users,
        login,
        password,
    )


def handle_authentication_status(
    authentication_status: str,
    users: dict[str, str],
    login: str,
) -> None:
    """Выполняет действие для полученного статуса входа.

    Args:
        authentication_status: Статус проверки учётных данных.
        users: Словарь обычных пользователей.
        login: Введённый логин.
    """
    if authentication_status == STATUS_USER_AUTHENTICATED:
        print(
            f"Привет, {login}! Вы успешно вошли в систему. "
            f"Пока здесь ничего нет, но, возможно, "
            f"когда-нибудь появится =)"
        )
    elif authentication_status == STATUS_ADMINISTRATOR_AUTHENTICATED:
        print(f"Вход администратора выполнен.")
        print(f"Логины и хеши пользователей:")

        if len(users.keys()) == 0:
            print(f"Пользователи отсутствуют.")
        else:
            for user_login, password_hash in users.items():
                print(f"{user_login}: {password_hash}")
    else:
        print(f"Не удалось войти: неверный логин или пароль.")


def main(config: dict) -> None:
    """Запускает основной цикл программы.

    Args:
        config: Конфигурация программы.
    """
    configure_logging(config)
    LOGGER.info(f"Программа запущена")

    credentials_status, users, administrator = get_credentials(config)

    if credentials_status != CREDENTIALS_STATUS_SUCCESS:
        print(f"Не удалось запустить программу: источник учётных данных не поддерживается.")
        return

    maximum_attempt_count = config["authentication"]["maximum_attempt_count"]
    failed_attempt_count = 0

    while True:
        print_menu()
        menu_item = input(f"Выберите действие: ")

        if menu_item == "0":
            print(f"Работа программы завершена.")
            LOGGER.info(f"Программа завершена пользователем")
            return

        elif menu_item == "1":
            process_registration(config, users, administrator)

        elif menu_item == "2":
            login, password = request_credentials()
            authentication_status = process_login(users, administrator, login, password)
            handle_authentication_status(authentication_status, users, login)

            if authentication_status in (STATUS_USER_AUTHENTICATED, STATUS_ADMINISTRATOR_AUTHENTICATED):
                failed_attempt_count = 0
                continue

            failed_attempt_count = failed_attempt_count + 1
            remaining_attempt_count = (maximum_attempt_count - failed_attempt_count)

            if remaining_attempt_count > 0:
                print(f"Осталось попыток: {remaining_attempt_count}.")
            else:
                print(f"Допустимое количество неудачных попыток исчерпано.")
                print(f"Работа программы принудительно завершена.")
                LOGGER.warning(
                    f"Программа принудительно завершена после неудачных попыток входа"
                )
                return

        else:
            print(f"Неизвестный пункт меню.")


if __name__ == "__main__":
    main(CONFIG)
