from flask import Blueprint

rider = Blueprint('rider', __name__)


@rider.route('/')
def test_rider():
    return "Test rider api"
