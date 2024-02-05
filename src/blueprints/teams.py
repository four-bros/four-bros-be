from flask import Blueprint
from src.controllers.TeamsController import TeamsController

teams_bp = Blueprint('teams', __name__)
TeamsController = TeamsController()

@teams_bp.route('', methods=['GET'])
def get_all_teams():
    return TeamsController.get_all_teams()

@teams_bp.route('/<team_id>/details', methods=['GET'])
def get_team_details_by_id(team_id: int):
    return TeamsController.get_team_details_by_id(team_id)

@teams_bp.route('/details/users', methods=['GET'])
def get_user_team_details():
    return TeamsController.get_user_teams_details()

@teams_bp.route('/<team_id>/roster', methods=['GET'])
def get_team_roster_by_id(team_id: int):
    return TeamsController.get_roster_by_team_id(team_id)

@teams_bp.route('/<team_id>/player/stats', methods=['GET'])
def get_team_player_stats(team_id: int):
    return TeamsController.get_players_stats_by_team_id(team_id)

@teams_bp.route('/player/stats/users', methods=['GET'])
def get_user_teams_player_stats():
    return TeamsController.get_user_teams_player_stats()

@teams_bp.route('/<team_id>/stats', methods=['GET'])
def get_team_stats(team_id: int):
    return TeamsController.get_team_stats_by_id(team_id)

@teams_bp.route('/stats/users', methods=['GET'])
def get_user_team_stats():
    return TeamsController.get_user_teams_stats()
