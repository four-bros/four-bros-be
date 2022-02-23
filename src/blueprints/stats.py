from flask import Blueprint, request

from src.blueprints.view_methods.stats import(
    get_season_defense_stats_leaders,
    get_season_kicking_stats_leaders,
    get_season_passing_stats_leaders,
    get_season_receiving_stats_leaders,
    get_season_return_stats_leaders,
    get_season_rushing_stats_leaders
)


stats_bp = Blueprint('stats', __name__)


@stats_bp.route('season/leaders/defense', methods=['GET'])
def stats_get_season_defense_leaders():
    return get_season_defense_stats_leaders(request, is_season_specific=True)


@stats_bp.route('season/leaders/kicking', methods=['GET'])
def stats_get_season_kicking_leaders():
    return get_season_kicking_stats_leaders(request, is_season_specific=True)


@stats_bp.route('season/leaders/passing', methods=['GET'])
def stats_get_season_passing_leaders():
    return get_season_passing_stats_leaders(request, is_season_specific=True)


@stats_bp.route('season/leaders/receiving', methods=['GET'])
def stats_get_season_receiving_leaders():
    return get_season_receiving_stats_leaders(request, is_season_specific=True)


@stats_bp.route('season/leaders/return', methods=['GET'])
def stats_get_season_return_leaders():
    return get_season_return_stats_leaders(request, is_season_specific=True)


@stats_bp.route('season/leaders/rushing', methods=['GET'])
def stats_get_season_rushing_leaders():
    return get_season_rushing_stats_leaders(request, is_season_specific=True)
