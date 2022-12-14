from ..db import session, Rate, Currency
from .validate import validate_currency


def get_rate(currency_code: str) -> dict:
    """
    Get last exchange rate for currency

    Args:
        currency_code (str): 3-letters code of currency

    Returns:
        dict: current exchange rate

    Raises:
        ValueError: if parameters are invalid
    """

    # Validate parameters
    validate_currency(currency_code)

    currency: Currency | None = session.query(Currency).filter(
        Currency.code.ilike(currency_code)
    ).first()

    if currency is None:
        # Not found
        raise ValueError("Currency not found")

    rate: Rate | None = session.query(Rate).filter(
        Rate.currency_id == currency.id
    ).order_by(Rate.created_at.desc()).first()

    if rate is None:
        raise ValueError("Rate not found for specified currency")

    return {
        "code": currency_code,
        "value": float(rate.value),
        "created_at": rate.created_at
    }
