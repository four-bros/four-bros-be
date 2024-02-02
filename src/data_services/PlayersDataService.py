from typing import List
from src.constants import (session)
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.HallOfFame import HallOfFame

class PlayersDataService():
    def __init__(self) -> None:
        pass

    def get_all_players(self) -> List[PlayerInfoData]:
        return session.query(PlayerInfoData).all()
    
    def get_player_by_player_id(self, player_id: str) -> PlayerInfoData:
        return session.query(PlayerInfoData).where(PlayerInfoData.id == player_id).one()
    
    def get_hof(self) -> List[HallOfFame]:
        return session.query(HallOfFame).all()
    
    def get_hof_player_info(self, player_ids):
        return session.query(PlayerInfoData).filter(PlayerInfoData.id.in_(player_ids)).all()
