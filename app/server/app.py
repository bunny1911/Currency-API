from flask import Flask
from .routes import rates_blueprint

app = Flask(__name__)

app.register_blueprint(rates_blueprint)
