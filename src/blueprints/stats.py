from flask import Blueprint
from src.controllers.SeasonLeadersController import SeasonLeadersController
from src.blueprints.view_methods.stats import (
    get_player_season_stats_leaders,
    get_team_season_stat_leaders
)

stats_bp = Blueprint('stats', __name__)
SeasonLeadersController = SeasonLeadersController()


@stats_bp.route('season/leaders/players', methods=['GET'])
def stats_get_season_leaders():
    return get_player_season_stats_leaders(is_season_specific=True, is_users_only=False)


@stats_bp.route('season/leaders/teams', methods=['GET'])
def stats_get_team_season_leaders():
    return get_team_season_stat_leaders(is_season_specific=True, is_users_only=False)


@stats_bp.route('season/leaders/players/users', methods=['GET'])
def stats_get_user_season_leaders():
    return get_player_season_stats_leaders(is_season_specific=True, is_users_only=True)


@stats_bp.route('season/leaders/teams/users', methods=['GET'])
def stats_get_user_team_season_leaders():
    return get_team_season_stat_leaders(is_season_specific=True, is_users_only=True)
