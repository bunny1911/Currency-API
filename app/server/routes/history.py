from datetime import date
from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with, doc
from marshmallow import fields

from ..funcs import get_history as funcs
from ..schemas import RateSchema

history_blueprint = Blueprint("history", __name__)


@history_blueprint.get("/<string:currency_code>/history")
@doc(
    summary="Get history of rates for currency"
)
@use_kwargs({
    "min_date": fields.Date(
        required=True,
        allow_none=False,
        validate=lambda value: date(day=1, month=1, year=2000) <= value <= date.today()
    ),
    "max_date": fields.Date(
        required=True,
        allow_none=False,
        validate=lambda value: date(day=1, month=1, year=2000) <= value <= date.today()
    )
}, location="query")
@marshal_with(RateSchema(many=True))
def get_history(
        currency_code: str,
        min_date: date,
        max_date: date
):
    return funcs.get_history(
        currency_code=currency_code,
        min_date=min_date,
        max_date=max_date
    )
