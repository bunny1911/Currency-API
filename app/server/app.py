from flask import Flask

from .routes import *
from .cache import cache
from .docs import docs, register_all


# Init app and tools
app = Flask(__name__)
cache.init_app(app)
docs.init_app(app)

# Register blueprint
app.register_blueprint(history_blueprint)
app.register_blueprint(rates_blueprint)
app.register_blueprint(handler_blueprint)

# Register docs
register_all(app, docs)
