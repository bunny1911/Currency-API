from os import environ
import requests

from ..db import session, Currency


# Get API key
API_KEY: str = environ.get("API_KEY")


def get_currencies() -> dict[str, str]:
    """
    Get all available currencies

    Returns:
        dict[str, str]: Currencies dictionary, where key is code and value is title

    Raises:
        ValueError: If failed to connect to the API
    """

    request = requests.get(
        "https://api.apilayer.com/exchangerates_data/symbols",
        headers={
            "APIKey": API_KEY
        }
    )

    if request.status_code != 200:
        # Request failed
        raise ValueError("Failed to get currencies from API")

    currencies: dict[str, str] = request.json()["symbols"]

    for code, title in currencies.items():
        # Check if already exists
        currency: Currency | None = session.query(Currency).filter(
            Currency.code.ilike(code)
        ).first()

        if currency is None:
            # Not exists
            currency = Currency(
                code=code,
                title=title,
            )
            session.add(currency)

    session.commit()

    return currencies
