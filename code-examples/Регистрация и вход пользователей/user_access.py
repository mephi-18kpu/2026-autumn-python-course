"""Регистрирует пользователей и проверяет учётные данные."""

# System imports
import logging

# External imports

# User imports
from password_tools import hash_password
from password_tools import verify_password

#############################################


LOGGER = logging.getLogger(__name__)

STATUS_SUCCESS = "success"
STATUS_EMPTY_LOGIN = "empty_login"
STATUS_EMPTY_PASSWORD = "empty_password"
STATUS_LOGIN_ALREADY_EXISTS = "login_already_exists"
STATUS_PASSWORD_TOO_SHORT = "password_too_short"
STATUS_USER_NOT_FOUND = "user_not_found"
STATUS_INVALID_PASSWORD = "invalid_password"
STATUS_USER_AUTHENTICATED = "user_authenticated"
STATUS_ADMINISTRATOR_AUTHENTICATED = "administrator_authenticated"


def register_user(
    config: dict,
    users: dict[str, str],
    administrator: dict[str, str],
    login: str,
    password: str,
) -> str:
    """Регистрирует пользователя в текущем запуске программы.

    Args:
        config: Конфигурация программы.
        users: Словарь обычных пользователей.
        administrator: Данные администратора.
        login: Новый логин.
        password: Новый пароль.

    Returns:
        Строковый статус операции.
    """
    if len(login) == 0:
        return STATUS_EMPTY_LOGIN

    if login in users or login == administrator["login"]:
        LOGGER.warning(
            f"Попытка регистрации занятого логина: {login}"
        )
        return STATUS_LOGIN_ALREADY_EXISTS

    if len(password) == 0:
        return STATUS_EMPTY_PASSWORD

    minimum_password_length = config["registration"][
        "minimum_password_length"
    ]

    if len(password) < minimum_password_length:
        return STATUS_PASSWORD_TOO_SHORT

    users[login] = hash_password(password)
    LOGGER.info(f"Пользователь зарегистрирован: {login}")
    return STATUS_SUCCESS


def authenticate_user(
    users: dict[str, str],
    login: str,
    password: str,
) -> str:
    """Проверяет учётные данные обычного пользователя.

    Args:
        users: Словарь обычных пользователей.
        login: Введённый логин.
        password: Введённый пароль.

    Returns:
        Строковый статус проверки.
    """
    if login not in users:
        LOGGER.warning(f"Неудачная попытка входа: {login}")
        return STATUS_USER_NOT_FOUND

    if not verify_password(password, users[login]):
        LOGGER.warning(f"Неудачная попытка входа: {login}")
        return STATUS_INVALID_PASSWORD

    LOGGER.info(f"Успешный вход пользователя: {login}")
    return STATUS_USER_AUTHENTICATED


def authenticate_administrator(
    administrator: dict[str, str],
    login: str,
    password: str,
) -> str:
    """Проверяет учётные данные администратора.

    Args:
        administrator: Данные администратора.
        login: Введённый логин.
        password: Введённый пароль.

    Returns:
        Строковый статус проверки.
    """
    if login != administrator["login"]:
        return STATUS_USER_NOT_FOUND

    if not verify_password(password, administrator["password_hash"]):
        LOGGER.warning(f"Неудачная попытка входа администратора")
        return STATUS_INVALID_PASSWORD

    LOGGER.info(f"Успешный вход администратора")
    return STATUS_ADMINISTRATOR_AUTHENTICATED
