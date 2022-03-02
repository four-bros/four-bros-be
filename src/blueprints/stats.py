from flask import Blueprint, request

from src.blueprints.view_methods.stats import (
    get_season_stats_leaders
)


stats_bp = Blueprint('stats', __name__)


@stats_bp.route('season/leaders', methods=['GET'])
def stats_get_season_leaders():
    return get_season_stats_leaders(request, is_season_specific=True)
