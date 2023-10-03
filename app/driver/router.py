from flask import Blueprint

driver = Blueprint('driver', __name__)


@driver.route('/')
def test_driver():
    return "Test driver api"
