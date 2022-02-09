from typing import List

from src.constants import session
from src.data_models.PlayerInfo import PlayerInfo
from src.responses.Players import PlayerSchema


player_schema_single = PlayerSchema()
player_schema_list = PlayerSchema(many=True)


def get_all_players(request):
    
    players: List[PlayerInfo] = session.query(PlayerInfo).all()
    players_json = player_schema_list.dump(players)
    
    response = {
        'players': players_json
    }
    
    return response


def get_player_by_player_id(request, player_id) -> PlayerSchema:
    player: PlayerInfo = session.query(PlayerInfo).where(
        PlayerInfo.player_id == player_id).one()
    response = player_schema_single.dump(player)
    
    return response


def get_players_by_team_id(request, team_id):
    players: List[PlayerInfo] = session.query(PlayerInfo).where(
        PlayerInfo.team_id == team_id).all()
    players.sort(key=lambda p: p.overall, reverse=True)
    players_json = player_schema_list.dump(players)
    
    response = {
        'players': players_json
    }
    
    return response


def get_players_by_team_id_and_position(team_id: int, position: str):
    
    players: List[PlayerInfo] = session.query(PlayerInfo).filter(
        PlayerInfo.team_id == team_id,
        PlayerInfo.position == position.upper()
    ).all()
    
    players_json = player_schema_list.dump(players)
    
    response = {
        'players': players_json
    }
    
    return response
