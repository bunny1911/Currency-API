from ..db import session, Rate, Currency


def get_rate(currency_code: str) -> dict:

    currency: Currency | None = session.query(Currency).filter(
        Currency.code.ilike(currency_code)
    ).first()

    if currency is None:
        raise ValueError

    rate: Rate | None = session.query(Rate).filter(
        Rate.currency_id == currency.id
    ).order_by(Rate.created_at.desc()).first()

    if rate is None:
        raise ValueError
    return {
        "code": currency_code,
        "value": float(rate.value),
        "created_at": rate.created_at
    }
