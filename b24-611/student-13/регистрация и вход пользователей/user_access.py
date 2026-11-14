# System imports
# External imports
# User imports

####################################

STATUS_USER_AUTH = "USER_AUTH"
STATUS_ADMIN_AUTH = "ADMIN_AUTH"
AUTH_FAILED = "AUTH_FAILED"

def sign_in(users: dict[str,str], admin: dict[str, str], login: str, pasword: str) -> bool:
    if login in users or login in admin:
        return False

    users[login] = pasword
    return True

def log_in(users: dict[str,str], admin: dict[str, str], login: str, pasword: str) -> str:
    if login in admin and admin[login] == pasword:
        return STATUS_ADMIN_AUTH
    if login in users and users[login] == pasword:
        return STATUS_USER_AUTH

    return AUTH_FAILED

