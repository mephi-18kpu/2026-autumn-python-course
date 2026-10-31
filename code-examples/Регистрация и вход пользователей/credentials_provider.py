"""Получает учётные данные из выбранного источника."""

# System imports
import logging

# External imports

# User imports
from user_generator import generate_administrator
from user_generator import generate_users

#############################################


LOGGER = logging.getLogger(__name__)

CREDENTIALS_STATUS_SUCCESS = "success"
CREDENTIALS_STATUS_UNSUPPORTED_SOURCE = "unsupported_source"


def print_administrator_credentials(administrator: dict[str, str], administrator_password: str) -> None:
    """Один раз выводит учётные данные администратора.

    Args:
        administrator: Данные администратора.
        administrator_password: Исходный пароль администратора.
    """
    print(f"Учётная запись администратора:")
    print(
        f"Логин: {administrator['login']}; "
        f"пароль: {administrator_password}"
    )
    print()
    print(f"Исходные пароли показываются только один раз.")


def get_credentials(config: dict) -> tuple[str, dict[str, str], dict[str, str]]:
    """Получает пользователей и администратора.

    Args:
        config: Конфигурация программы.

    Returns:
        Статус, словарь пользователей и словарь администратора.
    """
    credentials_source = config["credentials"]["credentials_source"]

    LOGGER.info(
        f"Выбран источник учётных данных: {credentials_source}"
    )

    if credentials_source == "generated":
        administrator, administrator_password = generate_administrator(config)
        users = generate_users(config)

        print_administrator_credentials(
            administrator,
            administrator_password,
        )
    # Здесь через elif блоки можно предусмотреть другие методы получения пользователей
    else:
        LOGGER.error(
            f"Источник учётных данных не поддерживается: {credentials_source}"
        )
        return CREDENTIALS_STATUS_UNSUPPORTED_SOURCE, {}, {}

    return CREDENTIALS_STATUS_SUCCESS, users, administrator
