from flask import Flask
from .routes import history_blueprint, rates_blueprint
from .cache import cache

app = Flask(__name__)
cache.init_app(app)

app.register_blueprint(history_blueprint)
app.register_blueprint(rates_blueprint)
