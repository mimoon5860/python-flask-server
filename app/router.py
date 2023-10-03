from flask import Blueprint
from app.auth.router import auth
from app.driver.router import driver
from app.rider.router import rider

app_router = Blueprint('app', __name__)

app_router.register_blueprint(auth, url_prefix='/auth')
app_router.register_blueprint(driver, url_prefix='/driver')
app_router.register_blueprint(rider, url_prefix='/rider')
