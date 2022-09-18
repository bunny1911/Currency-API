from flask import Blueprint, Response, jsonify

handler_blueprint = Blueprint("handler", __name__)


@handler_blueprint.app_errorhandler(ValueError)
def handle_value_error(error: ValueError) -> tuple[Response, int]:
    """
    Default error handler

    Args:
        error (ValueError): Raised error

    Returns:
        Response: Formatted error response
    """

    return jsonify({"error": str(error)}), 400


@handler_blueprint.app_errorhandler(Exception)
def handle_any_error(error: Exception) -> tuple[Response, int]:
    """
    Internal errors handler

    Args:
        error (Exception): Unexpected error

    Returns:
        Response: Formatted error response
    """

    return jsonify({"error": str(error)}), 500
