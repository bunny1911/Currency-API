from flask import Blueprint, jsonify

handler_blueprint = Blueprint("handler", __name__)


@handler_blueprint.app_errorhandler(ValueError)
def handle_value_error(error: ValueError):
    return jsonify({"error": str(error)}), 400
