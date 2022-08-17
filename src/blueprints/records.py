from flask import Blueprint, request

from src.blueprints.view_methods.records import(
    get_player_career_records_cache,
    get_player_game_records_cache,
    get_player_season_records_cache,
    get_team_season_records
)


records_bp = Blueprint('records', __name__)


@records_bp.route('career', methods=['GET'])
def records_get_career_records():
    return get_player_career_records_cache()


@records_bp.route('game', methods=['GET'])
def records_get_player_game_records():
    return get_player_game_records_cache()


@records_bp.route('season', methods=['GET'])
def records_get_season_records():
    return get_player_season_records_cache()


@records_bp.route('team', methods=['GET'])
def records_get_team_records():
    return get_team_season_records(request)
