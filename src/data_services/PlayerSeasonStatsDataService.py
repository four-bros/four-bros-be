from typing import List
from sqlalchemy import desc
from src.constants import session
from src.data_models.SeasonDefensiveStatsData import SeasonDefensiveStatsData
from src.data_models.SeasonOffensiveStatsData import SeasonOffensiveStatsData
from src.data_models.SeasonKickingStatsData import SeasonKickingStatsData
from src.data_models.SeasonReturnStatsData import SeasonReturnStatsData


class PlayerSeasonStatsDataService():
    def __init__(self) -> None:
        pass

    def get_offensive_stats_by_year(self, player_id: str, year: int) -> List[SeasonOffensiveStatsData]:
        return session.query(SeasonOffensiveStatsData).where(
            SeasonOffensiveStatsData.player_id == player_id,
            SeasonOffensiveStatsData.year == year
        ).scalar()

    def get_defensive_stats_by_year(self, player_id: str, year: int) -> List[SeasonDefensiveStatsData]:
        return session.query(SeasonDefensiveStatsData).where(
            SeasonDefensiveStatsData.player_id == player_id,
            SeasonDefensiveStatsData.year == year
        ).scalar()

    def get_return_stats_by_year(self, player_id: str, year: int) -> List[SeasonReturnStatsData]:
        return session.query(SeasonReturnStatsData).where(
            SeasonReturnStatsData.player_id == player_id,
            SeasonReturnStatsData.year == year
        ).scalar()

    def get_kicking_stats_by_year(self, player_id: str, year: int) -> List[SeasonKickingStatsData]:
        session.query(SeasonKickingStatsData).where(
            SeasonKickingStatsData.player_id == player_id,
            SeasonKickingStatsData.year == year
        ).scalar()

    def get_all_offensive_stats(self, player_id: str) -> List[SeasonOffensiveStatsData]:
        return session.query(SeasonOffensiveStatsData).where(
            SeasonOffensiveStatsData.player_id == player_id,
        ).order_by(desc(SeasonOffensiveStatsData.year)).all()

    def get_all_defensive_stats(self, player_id: str) -> List[SeasonDefensiveStatsData]:
        return session.query(SeasonDefensiveStatsData).where(
            SeasonDefensiveStatsData.player_id == player_id,
        ).order_by(desc(SeasonDefensiveStatsData.year)).all()

    def get_all_return_stats(self, player_id: str) -> List[SeasonReturnStatsData]:
        return session.query(SeasonReturnStatsData).where(
            SeasonReturnStatsData.player_id == player_id,
        ).order_by(desc(SeasonReturnStatsData.year)).all()

    def get_all_kicking_stats(self, player_id: str) -> List[SeasonKickingStatsData]:
        return session.query(SeasonKickingStatsData).where(
            SeasonKickingStatsData.player_id == player_id,
        ).order_by(desc(SeasonKickingStatsData.year)).all()
