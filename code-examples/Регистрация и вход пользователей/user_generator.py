"""Генерирует пользователей, логины и пароли."""

# System imports
import logging
import secrets
import string

# External imports

# User imports
from password_tools import hash_password

#############################################


LOGGER = logging.getLogger(__name__)

LOGIN_ALPHABET = (
    string.ascii_lowercase
    + string.ascii_uppercase
    + string.digits
)
PASSWORD_ALPHABET = string.ascii_letters + string.digits + "!@#$%^&*"


def generate_login(config: dict) -> str:
    """Генерирует логин со случайной частью.

    Args:
        config: Конфигурация программы.

    Returns:
        Сгенерированный логин.
    """
    user_generation_params = config["credentials"]["user_generation_params"]
    login_prefix = user_generation_params["login_prefix"]
    random_part_length = user_generation_params["login_random_part_length"]

    random_part = "".join(secrets.choice(LOGIN_ALPHABET) for _ in range(random_part_length))
    return login_prefix + random_part


def generate_password(config: dict) -> str:
    """Генерирует случайный пароль.

    Args:
        config: Конфигурация программы.

    Returns:
        Сгенерированный пароль.
    """
    password_length = config["credentials"]["password_generation_params"]["password_length"]

    return "".join(secrets.choice(PASSWORD_ALPHABET) for _ in range(password_length))


def generate_users(config: dict) -> dict[str, str]:
    """Генерирует пользователей и хеширует их пароли.

    Args:
        config: Конфигурация программы.

    Returns:
        Словарь пользователей с хешами паролей.
    """
    user_count = config["credentials"]["user_generation_params"]["user_count"]

    users = {}
    generated_logins = set()

    print(f"Сгенерированные пользователи:")

    while len(users) < user_count:
        login = generate_login(config)

        if login in generated_logins:
            continue

        password = generate_password(config)
        password_hash = hash_password(password)

        users[login] = password_hash
        generated_logins.add(login)
        print(f"Логин: {login}; пароль: {password}")

    print()
    LOGGER.info(f"Сгенерировано пользователей: {len(users)}")
    return users


def generate_administrator(config: dict) -> tuple[dict[str, str], str]:
    """Создаёт учётные данные администратора.

    Args:
        config: Конфигурация программы.

    Returns:
        Словарь администратора и его исходный пароль.
    """
    administrator_login = config["administrator"]["login"]
    password = generate_password(config)
    administrator = {
        "login": administrator_login,
        "password_hash": hash_password(password),
    }

    LOGGER.info(f"Учётная запись администратора сгенерирована")
    return administrator, password
