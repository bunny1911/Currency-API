from datetime import date
from sqlalchemy import DATE

from ..db import session, Rate, Currency
from .validate import validate_currency


def get_history(
        currency_code: str,
        min_date: date,
        max_date: date
) -> list[dict]:
    """
    Get history of rates for specified currency and dates range

    Args:
        currency_code (str): 3-letters code of currency
        min_date (date): History range minimal date
        max_date (date): History range maximal date

    Returns:
        list[dict]: List of rates for specified period

    Raises:
        ValueError: if parameters are invalid
    """

    # Validate parameters
    if min_date > max_date:
        raise ValueError("Invalid date range")

    validate_currency(currency_code)

    # Search currency code
    currency: Currency | None = session.query(Currency).filter(
        Currency.code.ilike(currency_code)
    ).first()

    if currency is None:
        # Not found
        raise ValueError("Currency not found")

    rates: list[Rate] = session.query(Rate).filter(
        Rate.created_at.cast(DATE).between(min_date, max_date),
        Rate.currency_id == currency.id
    ).all()

    return [{
        "code": currency_code,
        "value": float(rate.value),
        "created_at": rate.created_at
    } for rate in rates]
