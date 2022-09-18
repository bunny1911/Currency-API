from flask import Flask
from flask_apispec import FlaskApiSpec


def register_all(app: Flask, doc: FlaskApiSpec) -> None:
    """
    Register all routes docs for app

    Args:
        app (Flask): App object, routes of which you want to register
        doc (FlaskApiSpec): Doc object for docs registration
    """

    for name, blueprint in app.blueprints.items():
        if name == "flask-apispec":
            # Skip
            continue

        for key, value in app.view_functions.items():
            key = key.split(".")[0]
            if key == name:
                # Found blueprint route
                doc.register(value, blueprint=name)


docs = FlaskApiSpec(document_options=False)
