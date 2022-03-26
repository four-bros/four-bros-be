from flask import Blueprint, request

from src.blueprints.view_methods.teams import(
    get_all_teams,
    get_team_by_team_id,
    get_team_player_stats
)


teams_bp = Blueprint('teams', __name__)


@teams_bp.route('', methods=['GET'])
def teams_get_all():
    return get_all_teams(request)


@teams_bp.route('/<team_id>', methods=['GET'])
def teams_get_by_team_id(team_id: int):
    return get_team_by_team_id(request, team_id)


@teams_bp.route('/<team_id>/stats', methods=['GET'])
def teams_get_player_stats(team_id: int):
    return get_team_player_stats(request, team_id)
