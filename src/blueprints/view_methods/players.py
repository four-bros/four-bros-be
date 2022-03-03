from typing import List

from src.constants import(
    session,
    player_schema_single,
    player_schema_list
)
from src.data_models.PlayerInfoData import PlayerInfoData
from src.utils.player import _get_player_abilities_details_stats
from src.models.Player import PlayerAbilitiesDetailsStats
from src.responses.Players import PlayerSchema


def get_all_players(request):
    
    players: List[PlayerInfoData] = session.query(PlayerInfoData).all()

    converted_players: List[PlayerAbilitiesDetailsStats] = [_get_player_abilities_details_stats(player) for player in players]

    players_json = player_schema_list.dump(converted_players)
    
    response = {
        'players': players_json
    }
    
    return response


def get_player_by_player_id(request, player_id) -> PlayerSchema:
    player: PlayerInfoData = session.query(PlayerInfoData).where(
        PlayerInfoData.id == player_id).one()

    converted_player: PlayerAbilitiesDetailsStats = _get_player_abilities_details_stats(player)

    response: PlayerSchema = player_schema_single.dump(converted_player)
    
    return response


def get_players_by_team_id_and_position(team_id: int, position: str):
    
    players: List[PlayerInfoData] = session.query(PlayerInfoData).filter(
        PlayerInfoData.team_id == team_id,
        PlayerInfoData.position == position.upper()
    ).all()
    
    converted_players: List[PlayerAbilitiesDetailsStats] = [_get_player_abilities_details_stats(player) for player in players]

    players_json = player_schema_list.dump(converted_players)
    
    response = {
        'players': players_json
    }
    
    return response
