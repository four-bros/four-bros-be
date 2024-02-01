from flask import Blueprint
from src.blueprints.view_methods.teams import (
    get_all_teams,
    get_team_player_stats_by_id,
    get_team_details_by_id,
    get_team_roster_by_id,
    get_team_stats,
    get_user_teams_details,
    get_user_teams_player_stats
)

teams_bp = Blueprint('teams', __name__)

@teams_bp.route('', methods=['GET'])
def teams_get_all():
    return get_all_teams()

@teams_bp.route('/<team_id>/details', methods=['GET'])
def _get_team_details_by_id(team_id: int):
    return get_team_details_by_id(team_id)

@teams_bp.route('/details/users', methods=['GET'])
def _get_user_team_details():
    return get_user_teams_details()

@teams_bp.route('/<team_id>/roster', methods=['GET'])
def _get_team_roster_by_id(team_id: int):
    return get_team_roster_by_id(team_id)


@teams_bp.route('/<team_id>/player/stats', methods=['GET'])
def teams_get_player_stats(team_id: int):
    return get_team_player_stats_by_id(team_id)

@teams_bp.route('/player/stats/users', methods=['GET'])
def teams_get_user_player_stats():
    return get_user_teams_player_stats()

@teams_bp.route('/<team_id>/stats', methods=['GET'])
def teams_get_team_stats(team_id: int):
    return get_team_stats(team_id)
