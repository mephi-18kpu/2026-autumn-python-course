"""Предоставляет функции хеширования и проверки паролей."""

# System imports
import logging

# External imports
from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError
from argon2.exceptions import VerificationError
from argon2.exceptions import VerifyMismatchError

# User imports

#############################################


LOGGER = logging.getLogger(__name__)
PASSWORD_HASHER = PasswordHasher()


def hash_password(password: str) -> str:
    """Создаёт хеш пароля.

    Args:
        password: Исходный пароль.

    Returns:
        Строка с хешем пароля и параметрами Argon2id.
    """
    return PASSWORD_HASHER.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    """Проверяет соответствие пароля сохранённому хешу.

    Args:
        password: Пароль, введённый пользователем.
        password_hash: Хеш, сохранённый программой.

    Returns:
        True, если пароль подходит, иначе False.
    """
    try:
        PASSWORD_HASHER.verify(password_hash, password)
        return True
    except VerifyMismatchError:
        return False
    except (VerificationError, InvalidHashError):
        LOGGER.error(f"Не удалось проверить хеш пароля")
        return False
