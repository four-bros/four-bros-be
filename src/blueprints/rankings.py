from flask import Blueprint
from src.controllers.RankingsController import RankingsController

rankings_bp = Blueprint('rankings', __name__)
RankingsController = RankingsController()

@rankings_bp.route('/', methods=['GET'])
def get_rankings():
    return RankingsController.get_all_rankings()
