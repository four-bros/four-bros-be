from flask import Blueprint
from src.controllers.UsersController import UsersController

home_bp = Blueprint('home', __name__)
UsersController = UsersController()

@home_bp.route('/', methods=['GET'])
def home():
    return UsersController.get_users_and_week()
