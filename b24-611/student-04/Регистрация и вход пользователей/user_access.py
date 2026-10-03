STATUS_USER_AUTH = "user_auth"
STATUS_ADMIN_AUTH = "admin_auth"
STATUS_AUTH_FAIL = "user_failed"

""""Функция регистрации нового пользователя"""

def register_user(
    users: dict[str,str],
    admins: dict[str, str],
    login: str,
    password: str
) -> bool:
    if login in users or login in admins:
        return False

    users[login] = password
    return True


""""Функция авторизации пользователя"""
def auth_account (
users: dict[str,str],
    admins: dict[str, str],
    login: str,
    password: str
) -> str:
    if login in admins and admins[login] == password:
        return STATUS_ADMIN_AUTH

    if login in users and users[login] == password:
        return STATUS_USER_AUTH

    return STATUS_AUTH_FAIL



