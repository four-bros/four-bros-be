from flask import Blueprint
from src.controllers.CommitsController import CommitsController

commits_bp = Blueprint('commits', __name__)
CommitsController = CommitsController()

@commits_bp.route('/', methods=['GET'])
def get_commits():
    return CommitsController.get_all_commits()
