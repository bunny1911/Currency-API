import re


def validate_currency(currency_code: str) -> None:
    """
    Validate currency code

    Args:
        currency_code (str): code of currency you want to validate

    Raises:
        ValueError: If code is invalid
    """

    if not isinstance(currency_code, str) or not re.match(r"^[A-Za-z]{3}$", currency_code):
        raise ValueError("Invalid currency format")
