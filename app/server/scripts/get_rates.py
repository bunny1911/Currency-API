from os import environ
import requests
from datetime import datetime
from urllib.parse import urlencode

from ..db import Rate, session, Currency
from ..cache import cache
from ..funcs import validate_currency

# Get API key
API_KEY: str = environ.get("API_KEY")


def get_rates(
        currencies: list[str],
        date: datetime = None,
        base: str = "USD"
) -> dict[str, float]:
    """
    Get actual exchange rates for specified parameters

    Args:
        currencies (list[str]): List of currencies, exchange rates of which you want to get
        date (datetime): Rate date
        base (str): Base currency

    Returns:
        dict[str, float]: Dictionary of rates, where key is currency code and value is their exchange rate

    Raises:
        ValueError: If failed to connect to the API
    """

    # Use current date if empty
    date = date or datetime.utcnow()

    # Validate parameters
    validate_currency(base)

    for currency_code in currencies:
        validate_currency(currency_code)

    # Perform request
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
        # Request failed
        raise ValueError("Failed to get rates from API")

    rates: dict[str, float] = request.json()["rates"]

    for key, value in rates.items():
        # Check if already exists
        currency: Currency | None = session.query(Currency).filter(
            Currency.code.ilike(key)
        ).first()

        if currency is None:
            # Not found
            continue

        rate: Rate = Rate(
            currency_id=currency.id,
            created_at=date,
            value=value
        )
        session.add(rate)

    session.commit()

    # Delete cached values
    for currency_code in currencies:
        cache.delete("get_rate_" + currency_code.lower())

    return rates
