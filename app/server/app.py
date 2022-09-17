from flask import Flask
from .routes import history_blueprint, rates_blueprint

app = Flask(__name__)

app.register_blueprint(history_blueprint)
app.register_blueprint(rates_blueprint)
