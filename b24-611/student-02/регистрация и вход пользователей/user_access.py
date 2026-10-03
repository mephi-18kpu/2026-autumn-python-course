STATUS_USER_AUTH = "user_auth"
STATUS_ADMIN_AUTH = "admin_auth"
STATUS_AUTH_FAILED = "auth_failed"


def register_user(
    users: dict[str, str],
    admins: dict[str, str],
    login: str,
    password: str
) -> bool:
    """функция регистрации нового пользователя"""
    if login in users or login in admins:
        return False

    users[login] = password
    return True


def auth_account(
    users: dict[str, str],
    admins: dict[str, str],
    login: str,
    password: str
) -> str:
    """проверка переданного логина и пароля"""
    if login in admins and admins[login] == password:
        return STATUS_ADMIN_AUTH

    if login in users and users[login] == password:
        return STATUS_USER_AUTH

    return STATUS_AUTH_FAILED
