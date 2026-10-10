"""Предоставляет функции регистрации и проверки учётных данных."""

# System imports

# External imports

# User imports

#############################################

STATUS_USER_AUTHENTICATED = "user_authenticated"
STATUS_ADMINISTRATOR_AUTHENTICATED = "administrator_authenticated"
STATUS_AUTHENTICATION_FAILED = "authentication_failed"

def register_user(
    users: dict[str, str],
    administrators: dict[str, str],
    login: str,
    password: str,
) -> bool:
    """Добавляет нового пользователя.

    Args:
        users: Словарь обычных пользователей.
        administrators: Словарь администраторов.
        login: Новый логин.
        password: Новый пароль.

    Returns:
        True, если пользователь зарегистрирован, иначе False.
    """
    if login in users or login in administrators:
        return False

    users[login] = password
    return True

def authenticate_account(
    users: dict[str, str],
    administrators: dict[str, str],
    login: str,
    password: str,
) -> str:
    """Проверяет логин и пароль.

    Args:
        users: Словарь обычных пользователей.
        administrators: Словарь администраторов.
        login: Введённый логин.
        password: Введённый пароль.

    Returns:
        Строковый статус проверки учётных данных.
    """
    if login in administrators and administrators[login] == password:
        return STATUS_ADMINISTRATOR_AUTHENTICATED

    if login in users and users[login] == password:
        return STATUS_USER_AUTHENTICATED

    return STATUS_AUTHENTICATION_FAILED
