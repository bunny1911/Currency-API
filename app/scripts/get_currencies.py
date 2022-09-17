from os import environ
import requests
from app.db import session, Currency


# Get API key
API_KEY: str = environ.get("API_KEY")


def get_currencies() -> dict[str, str]:
    request = requests.get(
        "https://api.apilayer.com/exchangerates_data/symbols",
        headers={
            "APIKey": API_KEY
        })

    if request.status_code != 200:
        raise ValueError

    currencies: dict[str, str] = request.json()["symbols"]

    for code, title in currencies.items():
        currency: Currency | None = session.query(Currency).filter(
            Currency.code.ilike(code)
        ).first()

        if currency is None:
            currency = Currency(
                code=code,
                title=title,
            )
            session.add(currency)

    session.commit()

    return currencies
