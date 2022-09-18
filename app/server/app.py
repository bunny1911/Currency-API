from flask import Flask
from .routes import history_blueprint, rates_blueprint
from .cache import cache
from .docs import docs, register_all

app = Flask(__name__)
cache.init_app(app)
docs.init_app(app)

app.register_blueprint(history_blueprint)
app.register_blueprint(rates_blueprint)

register_all(app, docs)
