from flask import Blueprint, request

from src.blueprints.view_methods.stats import (
    get_player_season_stats_leaders,
    get_team_season_stat_leaders
)


stats_bp = Blueprint('stats', __name__)


@stats_bp.route('season/leaders/players', methods=['GET'])
def stats_get_season_leaders():
    return get_player_season_stats_leaders(is_season_specific=True)


@stats_bp.route('season/leaders/teams', methods=['GET'])
def stats_get_team_season_leaders():
    return get_team_season_stat_leaders(request, is_season_specific=True)
