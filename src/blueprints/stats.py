from flask import Blueprint, request

from src.responses.Players import PlayerSchema
from src.blueprints.view_methods.stats import(
    get_season_passing_stats,
)


stats_bp = Blueprint('stats', __name__)


@stats_bp.route('/season/passing', methods=['GET'])
def stats_get_season_passing():
    return get_season_passing_stats(request)
