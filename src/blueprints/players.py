from flask import Blueprint, request

from src.schemas.Players import PlayerSchema
from src.blueprints.view_methods.players import(
    get_all_players,
    get_player_by_player_id,
    get_players_by_team_id_and_position,
    get_hof
)


players_bp = Blueprint('players', __name__)


@players_bp.route('', methods=['GET'])
def players_get_all():
    return get_all_players(request)


@players_bp.route('/<player_id>', methods=['GET'])
def players_get_by_player_id(player_id: int) -> PlayerSchema:
    return get_player_by_player_id(request, player_id)


@players_bp.route('team/<team_id>/<position>', methods=['GET'])
def players_get_by_team_id_and_position(team_id: int, position: str):
    return get_players_by_team_id_and_position(team_id, position)


@players_bp.route('hof', methods=['GET'])
def players_get_hof():
    return get_hof()
