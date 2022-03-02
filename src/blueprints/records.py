from flask import Blueprint, request

from src.blueprints.view_methods.records import(
    get_season_records,
    get_career_records
)


records_bp = Blueprint('records', __name__)


@records_bp.route('season/', methods=['GET'])
def records_get_season_records():
    return get_season_records(request)


@records_bp.route('career/', methods=['GET'])
def records_get_career_records():
    return get_career_records(request)
