from os import environ
import requests
from datetime import datetime
from urllib.parse import urlencode

from app.db import Rate, session, Currency


# Get API key
API_KEY:     str = environ.get("API_KEY")


def get_rates(
        currencies: list[str],
        date: datetime = None,
        base: str = "USD"
) -> dict[str, float]:
    date = date or datetime.utcnow()

    params: str = urlencode({
        "base": base,
        "symbols": ",".join(currencies)
    })
    request = requests.get(
        f"https://api.apilayer.com/exchangerates_data/{date.date().isoformat()}?" + params,
        headers={
            "APIKey": API_KEY
        }
    )

    if request.status_code != 200:
        raise ValueError

    rates: dict[str, float] = request.json()["rates"]

    for key, value in rates.items():
        currency: Currency | None = session.query(Currency).filter(
            Currency.code.ilike(key)
        ).first()

        if currency is None:
            raise ValueError

        rate: Rate = Rate(
            currency_id=currency.id,
            created_at=date,
            value=value
        )
        session.add(rate)

    session.commit()

    return rates


# if __name__ == "__main__":
    # get_rates(currencies=["UAH", "EUR"])
