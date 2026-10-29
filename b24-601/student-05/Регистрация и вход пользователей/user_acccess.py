STATUS_USER_AUTH = "user_authenticated"
STATUS_ADMIN_AUTH = "admin_authenticated"
STATUS_AUTH_FAILED = "authentication_failed"
def register_user(
    users: dict[str, str],
    admins: dict[str, str],
    login: str,
    password: str,) -> bool:
    if login in users or login in admins:
        return False
    users[login] = password
    return True
def authenticate_account(
    users: dict[str, str],
    admins: dict[str, str],
    login: str,
    password: str
) -> str:
    if login in admins and admins[login] == password:
        return STATUS_ADMIN_AUTH
    if login in users and users[login] == password:
        return STATUS_USER_AUTH
    return STATUS_AUTH_FAILED
