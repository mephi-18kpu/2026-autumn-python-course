"""Содержит конфигурацию консольной программы."""

# System imports

# External imports

# User imports

#############################################


CONFIG = {
    "credentials": {
        "credentials_source": "generated",
        "user_generation_params": {
            "user_count": 5,
            "login_prefix": "user_",
            "login_random_part_length": 6,
        },
        "password_generation_params": {
            "password_length": 12,
        },
    },
    "registration": {
        "minimum_password_length": 8,
    },
    "authentication": {
        "maximum_attempt_count": 3,
    },
    "administrator": {
        "login": "admin",
    },
    "logging": {
        "log_file": "user_authentication.log",
        "log_level": "INFO",
    },
}
