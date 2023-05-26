from flask import Blueprint
from src.blueprints.view_methods.teams import (
    get_all_teams,
    get_team_player_stats,
    get_team_details,
    get_team_game_stats,
    get_team_roster,
    get_team_season_stats
)

teams_bp = Blueprint('teams', __name__)

@teams_bp.route('', methods=['GET'])
def teams_get_all():
    return get_all_teams()


@teams_bp.route('/<team_id>/details', methods=['GET'])
def get_team_details_by_id(team_id: int):
    return get_team_details(team_id)


@teams_bp.route('/<team_id>/roster', methods=['GET'])
def get_team_roster_by_id(team_id: int):
    return get_team_roster(team_id)

@teams_bp.route('/<team_id>/stats/game', methods=['GET'])
def teams_get_team_game_stats(team_id: int):
    return get_team_game_stats(team_id)

@teams_bp.route('/<team_id>/stats/player', methods=['GET'])
def teams_get_player_stats(team_id: int):
    return get_team_player_stats(team_id)

@teams_bp.route('/<team_id>/stats/season', methods=['GET'])
def teams_get_team_season_stats(team_id: int):
    return get_team_season_stats(team_id)
