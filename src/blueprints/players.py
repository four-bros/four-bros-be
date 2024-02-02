from flask import Blueprint
from src.controllers.PlayersController import PlayersController

players_bp = Blueprint('players', __name__)
PlayersController = PlayersController()

@players_bp.route('', methods=['GET'])
def players_get_all():
    return PlayersController.get_all_players()

@players_bp.route('/<player_id>', methods=['GET'])
def players_get_by_player_id(player_id: str) -> dict:
    return PlayersController.get_player_by_player_id(player_id)


@players_bp.route('hof', methods=['GET'])
def players_get_hof() -> dict:
    return PlayersController.get_hof()
