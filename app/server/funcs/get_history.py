import re
from datetime import date
from sqlalchemy import DATE
from ..db import session, Rate, Currency
from .validate import validate_currency


def get_history(
        currency_code: str,
        min_date: date,
        max_date: date
) -> list[dict]:
    if min_date > max_date:
        raise ValueError

    validate_currency(currency_code)

    currency: Currency | None = session.query(Currency).filter(
        Currency.code.ilike(currency_code)
    ).first()

    if currency is None:
        raise ValueError

    rates: list[Rate] = session.query(Rate).filter(
        Rate.created_at.cast(DATE).between(min_date, max_date),
        Rate.currency_id == currency.id
    ).all()

    return [{
        "code": currency_code,
        "value": float(rate.value),
        "created_at": rate.created_at
    } for rate in rates]
