from typing import List

from src.constants import(
    session,
    player_schema_single,
    player_schema_list,
    player_hof_schema_list
)
from src.data_models.HallOfFame import HallOfFame
from src.data_models.PlayerInfoData import PlayerInfoData
from src.utils.player import _get_player_abilities_details_stats, _get_player_hof_info
from src.models.Player import PlayerAbilitiesDetailsStats, PlayerHofInfo
from src.schemas.Players import PlayerSchema


def get_all_players(request):
    
    players: List[PlayerInfoData] = session.query(PlayerInfoData).all()

    converted_players: List[PlayerAbilitiesDetailsStats] = [_get_player_abilities_details_stats(player) for player in players]

    players_json = player_schema_list.dump(converted_players)
    
    response = {
        'players': players_json
    }
    
    return response


def get_player_by_player_id(player_id: str) -> PlayerSchema:
    player: PlayerInfoData = session.query(PlayerInfoData).where(
        PlayerInfoData.id == player_id).one()

    converted_player: PlayerAbilitiesDetailsStats = _get_player_abilities_details_stats(player)

    print(converted_player)

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


def get_hof():

    hof: List[HallOfFame] = session.query(HallOfFame).all()

    player_ids: List[str] = [player.player_id for player in hof]

    players: List[PlayerInfoData] = session.query(PlayerInfoData).filter(PlayerInfoData.id.in_(player_ids)).all()

    converted_players: List[PlayerHofInfo] = [_get_player_hof_info(player) for player in players]

    players_json = player_hof_schema_list.dump(converted_players)
    
    response = {
        'players': players_json
    }
    
    return response
