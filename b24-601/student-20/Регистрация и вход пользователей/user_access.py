"""Предоставляет функции регистрации и проверки учётных данных."""

# System imports

# External imports

# User imports

#############################################

STATUS_USER_AUTH = "user_authenticated"
STATUS_ADMINISTRATOR_AUTH = "administrator_authenticated"
STATUS_AUTHENTICATION_FAILED = "authentication_failed"

def register_user(
    users: dict[str, str],
    admins: dict[str, str],
    login: str,
    password: str,
) -> bool:
    """" Функция добовляет нового пользователя."""

    if login in users or login in admins:
        return False

    users[login] = password
    return True

def authenticated_account(
    users: dict[str, str],
    admins: dict[str, str],
    login: str,
    password: str,
)-> str:
    """ Проверка логина и пароля."""

    if login in admins and admins[login] == password:
        return STATUS_ADMINISTRATOR_AUTH

    if login in users and users[login] == password:
        return STATUS_USER_AUTH

    return STATUS_AUTHENTICATION_FAILED
