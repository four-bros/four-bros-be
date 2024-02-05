from flask import Blueprint
from src.controllers.PlayersSeasonLeadersController import PlayersSeasonLeadersController
from src.controllers.TeamsSeasonLeadersController import TeamsSeasonLeadersController

stats_bp = Blueprint('stats', __name__)
PlayersSeasonLeadersController = PlayersSeasonLeadersController()
TeamsSeasonLeadersController = TeamsSeasonLeadersController()

@stats_bp.route('season/leaders/players', methods=['GET'])
def get_all_season_leaders():
    return PlayersSeasonLeadersController.get_all_season_stats_leaders(is_season_specific=True, is_users_only=False)

@stats_bp.route('season/leaders/players/defense', methods=['GET'])
def get_defensive_season_leaders():
    return PlayersSeasonLeadersController.get_defensive_season_stats_leaders(is_season_specific=True, is_users_only=False)

@stats_bp.route('season/leaders/players/kick_return', methods=['GET'])
def get_kick_return_season_leaders():
    return PlayersSeasonLeadersController.get_kick_return_season_stats_leaders(is_season_specific=True, is_users_only=False)

@stats_bp.route('season/leaders/players/kicking', methods=['GET'])
def get_kicking_season_leaders():
    return PlayersSeasonLeadersController.get_kicking_season_stats_leaders(is_season_specific=True, is_users_only=False)

@stats_bp.route('season/leaders/players/passing', methods=['GET'])
def get_passing_season_leaders():
    return PlayersSeasonLeadersController.get_passing_season_stats_leaders(is_season_specific=True, is_users_only=False)

@stats_bp.route('season/leaders/players/punt_return', methods=['GET'])
def get_punt_return_season_leaders():
    return PlayersSeasonLeadersController.get_punt_return_season_stats_leaders(is_season_specific=True, is_users_only=False)


@stats_bp.route('season/leaders/players/punting', methods=['GET'])
def get_punting_season_leaders():
    return PlayersSeasonLeadersController.get_punting_season_stats_leaders(is_season_specific=True, is_users_only=False)

@stats_bp.route('season/leaders/players/receiving', methods=['GET'])
def get_receiving_season_leaders():
    return PlayersSeasonLeadersController.get_receiving_season_stats_leaders(is_season_specific=True, is_users_only=False)

@stats_bp.route('season/leaders/players/rushing', methods=['GET'])
def get_rushing_season_leaders():
    return PlayersSeasonLeadersController.get_rushing_season_stats_leaders(is_season_specific=True, is_users_only=False)

@stats_bp.route('season/leaders/players/total', methods=['GET'])
def get_total_season_leaders():
    return PlayersSeasonLeadersController.get_total_season_stats_leaders(is_season_specific=True, is_users_only=False)

@stats_bp.route('season/leaders/teams', methods=['GET'])
def stats_get_team_season_leaders():
    return TeamsSeasonLeadersController.get_team_season_stats_leaders(is_season_specific=True, is_users_only=False)

@stats_bp.route('season/leaders/players/users', methods=['GET'])
def stats_get_user_season_leaders():
    return PlayersSeasonLeadersController.get_all_season_stats_leaders(is_season_specific=True, is_users_only=True)

@stats_bp.route('season/leaders/teams/users', methods=['GET'])
def stats_get_user_team_season_leaders():
    return TeamsSeasonLeadersController.get_team_season_stats_leaders(is_season_specific=True, is_users_only=True)
