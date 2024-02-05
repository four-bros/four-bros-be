from typing import List
from sqlalchemy import desc
from src.constants import session
from src.data_models.GameDefensiveStatsData import GameDefensiveStatsData
from src.data_models.GameOffensiveStatsData import GameOffensiveStatsData
from src.data_models.GameKickingStatsData import GameKickingStatsData
from src.data_models.GameReturnStatsData import GameReturnStatsData


class PlayersGameStatsDataService():
    def __init__(self) -> None:
        pass

    def get_offensive_stats(self, player_id: str, year: int) -> List[GameOffensiveStatsData]:
        return session.query(GameOffensiveStatsData).where(
            GameOffensiveStatsData.player_id == player_id,
            GameOffensiveStatsData.year == year
        ).order_by(desc(GameOffensiveStatsData.week)).all()

    def get_defensive_stats(self, player_id: str, year: int) -> List[GameDefensiveStatsData]:
        return session.query(GameDefensiveStatsData).where(
            GameDefensiveStatsData.player_id == player_id,
            GameDefensiveStatsData.year == year
        ).order_by(desc(GameDefensiveStatsData.week)).all()

    def get_return_stats(self, player_id: str, year: int) -> List[GameReturnStatsData]:
        return session.query(GameReturnStatsData).where(
            GameReturnStatsData.player_id == player_id,
            GameReturnStatsData.year == year
        ).order_by(desc(GameReturnStatsData.week)).all()

    def get_kicking_stats(self, player_id: str, year: int) -> List[GameKickingStatsData]:
        session.query(GameKickingStatsData).where(
            GameKickingStatsData.player_id == player_id,
            GameKickingStatsData.year == year
        ).order_by(desc(GameKickingStatsData.week)).all()
