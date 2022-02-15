from flask import Blueprint, request

from src.blueprints.view_methods.teams import(
    get_all_teams,
    get_team_by_team_id,
    get_team_defensive_leaders,
    get_team_passing_leaders,
    get_team_receiving_leaders,
    get_team_rushing_leaders
)
from src.responses.Teams import TeamSchema


teams_bp = Blueprint('teams', __name__)


@teams_bp.route('', methods=['GET'])
def teams_get_all():
    return get_all_teams(request)


@teams_bp.route('/<team_id>', methods=['GET'])
def teams_get_by_team_id(team_id: int) -> TeamSchema:
    return get_team_by_team_id(request, team_id)


@teams_bp.route('/<team_id>/leaders/defense', methods=['GET'])
def teams_get_defensive_leaders(team_id: int):
    return get_team_defensive_leaders(request, team_id)


@teams_bp.route('/<team_id>/leaders/passing', methods=['GET'])
def teams_get_passing_leaders(team_id: int):
    return get_team_passing_leaders(request, team_id)


@teams_bp.route('/<team_id>/leaders/receiving', methods=['GET'])
def teams_get_receiving_leaders(team_id: int):
    return get_team_receiving_leaders(request, team_id)


@teams_bp.route('/<team_id>/leaders/rushing', methods=['GET'])
def teams_get_rushing_leaders(team_id: int):
    return get_team_rushing_leaders(request, team_id)
