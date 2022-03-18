from flask import Blueprint, request

from src.blueprints.view_methods.home import get_home_data


home_bp = Blueprint('home', __name__)


@home_bp.route('/', methods=['GET'])
def home():
    return get_home_data(request)
