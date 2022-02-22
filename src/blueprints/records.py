from flask import Blueprint, request

from src.blueprints.view_methods.records import(
    get_season_records
)
from src.blueprints.view_methods.stats import(
    get_season_defense_stats_leaders
)

records_bp = Blueprint('records', __name__)


@records_bp.route('season/', methods=['GET'])
def records_get_season_records():
    return get_season_defense_stats_leaders(request, is_season_specific=False)
