from typing import List
from src.constants import (session)
from src.data_models.CareerDefensiveStatsData import CareerDefensiveStatsData
from src.data_models.CareerOffensiveStatsData import CareerOffensiveStatsData
from src.data_models.CareerKickingStatsData import CareerKickingStatsData
from src.data_models.CareerReturnStatsData import CareerReturnStatsData


class PlayersCareerStatsDataService():
    def __init__(self) -> None:
        pass

    def get_offensive_stats(self, player_id: str) -> List[CareerOffensiveStatsData]:
        return session.query(CareerOffensiveStatsData).where(
            CareerOffensiveStatsData.player_id == player_id,
        ).scalar()

    def get_defensive_stats(self, player_id: str) -> List[CareerDefensiveStatsData]:
        return session.query(CareerDefensiveStatsData).where(
            CareerDefensiveStatsData.player_id == player_id,
        ).scalar()

    def get_return_stats(self, player_id: str) -> List[CareerReturnStatsData]:
        return session.query(CareerReturnStatsData).where(
            CareerReturnStatsData.player_id == player_id,
        ).scalar()

    def get_kicking_stats(self, player_id: str) -> List[CareerKickingStatsData]:
        session.query(CareerKickingStatsData).where(
            CareerKickingStatsData.player_id == player_id,
        ).scalar()
