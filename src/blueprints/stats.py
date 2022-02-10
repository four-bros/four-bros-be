from flask import Blueprint, request

from src.blueprints.view_methods.stats import(
    get_season_passing_stats,
    get_season_passing_leaders_stats
)


stats_bp = Blueprint('stats', __name__)


@stats_bp.route('/season/passing', methods=['GET'])
def stats_get_season_passing():
    return get_season_passing_stats(request)


@stats_bp.route('season/leaders/passing', methods=['GET'])
def stats_get_season_passing_leaders():
    return get_season_passing_leaders_stats(request)
