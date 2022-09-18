from flask import Flask
from flask_apispec import FlaskApiSpec


def register_all(app: Flask, doc: FlaskApiSpec) -> None:
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
