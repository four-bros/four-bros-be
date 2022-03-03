from flask import Blueprint, request

from src.blueprints.view_methods.records import(
    get_career_records,
    get_game_records,
    get_season_records
)


records_bp = Blueprint('records', __name__)


@records_bp.route('career/', methods=['GET'])
def records_get_career_records():
    return get_career_records(request)


@records_bp.route('game/', methods=['GET'])
def records_get_game_records():
    return get_game_records(request)


@records_bp.route('season/', methods=['GET'])
def records_get_season_records():
    return get_season_records(request)
