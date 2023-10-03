from flask import Flask
from .router import app_router


app = Flask(__name__)


@app.route('/')
def init_func():
    return "Ride 360 Server running"


def create_app():
    app.register_blueprint(app_router, url_prefix='/api/v1')

    return app
