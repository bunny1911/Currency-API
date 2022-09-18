import re


def validate_currency(currency_code: str) -> None:
    if not isinstance(currency_code, str) or not re.match(r"^[A-Za-z]{3}$", currency_code):
        raise ValueError
