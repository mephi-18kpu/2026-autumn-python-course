"""Шапка которую перепишу потом"""





####################################

STATUS_USER_AUTH = "user_authenticated"
STATUS_ADMIN_AUTH = "admin_authenticated"
STATUS_FAILED_AUTH = "authentication_failed"

def register_user(
        users: dict[str, str],
        admin: dict[str, str],
        login: str,
        password:str
) -> bool:
    """ Добавление нового пользователя """

    if login in users or login in admin:
        return False

    users[login] = password
    return True

def authenticate_account(
        users: dict[str, str],
        admin: dict[str, str],
        login: str,
        password:str
) -> str:

    if login in admin and admin[login] == password:
        return STATUS_ADMIN_AUTH

    if login in users and users[login] == password:
        return STATUS_USER_AUTH

    return STATUS_FAILED_AUTH


