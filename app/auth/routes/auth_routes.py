from flask import Blueprint
from app.database import conn
auth_router = Blueprint('auth', __name__)


@auth_router.route('/')
def auth_test():

    return "Test auth is running"
