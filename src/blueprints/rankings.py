from flask import Blueprint

from src.blueprints.view_methods.rankings import get_all_rankings


rankings_bp = Blueprint('rankings', __name__)


@rankings_bp.route('/', methods=['GET'])
def get_rankings():
    return get_all_rankings()
