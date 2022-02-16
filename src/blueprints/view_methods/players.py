from typing import List

from src.constants import(
    session,
    player_schema_single,
    player_schema_list
)
from src.data_models.PlayerInfo import PlayerInfo
from src.helpers import _get_player_details_and_abilities
from src.models.Player import Player
from src.responses.Players import PlayerSchema


def get_all_players(request):
    
    players: List[PlayerInfo] = session.query(PlayerInfo).all()

    players_json = []

    for player in players:

        converted_player = _get_player_details_and_abilities(player)

        player_json = player_schema_single.dump(converted_player)
        players_json.append(player_json)
    
    response = {
        'players': players_json
    }
    
    return response


def get_player_by_player_id(request, player_id) -> PlayerSchema:
    player: PlayerInfo = session.query(PlayerInfo).where(
        PlayerInfo.id == player_id).one()

    converted_player: Player = _get_player_details_and_abilities(player)

    response = player_schema_single.dump(converted_player)
    
    return response


def get_players_by_team_id_and_position(team_id: int, position: str):
    
    players: List[PlayerInfo] = session.query(PlayerInfo).filter(
        PlayerInfo.team_id == team_id,
        PlayerInfo.position == position.upper()
    ).all()
    
    converted_players: List[Player] = [_get_player_details_and_abilities(player) for player in players]

    players_json = player_schema_list.dump(converted_players)
    
    response = {
        'players': players_json
    }
    
    return response
