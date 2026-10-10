"""Настраивает запись событий программы в файл."""

# System imports
import logging
from pathlib import Path

# External imports

# User imports

#############################################


CURRENT_DIR = Path(__file__).resolve().parent


def configure_logging(config: dict) -> None:
    """Настраивает корневой логгер программы.

    Args:
        config: Конфигурация программы.
    """
    logging_config = config["logging"]
    root_logger = logging.getLogger()
    root_logger.setLevel(logging_config["log_level"])

    file_handler = logging.FileHandler(CURRENT_DIR / logging_config["log_file"], "w", "utf-8")

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        "%Y-%m-%d %H:%M:%S",
    )

    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)
