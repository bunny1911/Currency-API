from flask import Blueprint
from flask_apispec import marshal_with, doc

from ..funcs import get_rate as funcs
from ..schemas import RateSchema
from ..cache import cache, make_key

rates_blueprint = Blueprint("rates", __name__)


@rates_blueprint.get("/<string:currency_code>/rate")
@doc(
    summary="Get current rate for currency",
    tags=["Rate"]
)
@marshal_with(RateSchema(many=False))
@cache.cached(timeout=3600, key_prefix=make_key("get_rate"))  # 1 hour
def get_rate(
        currency_code: str,
):
    return funcs.get_rate(
        currency_code=currency_code
    )
