from typing import List
from sqlalchemy import desc
from src.constants import session, user_team_ids
from src.data_models.PlayerInfoData import PlayerInfoData
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

    # Player stats by team
    def get_defensive_stats_by_team_id(self, team_id: int, year):
        return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
            PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
            PlayerInfoData.team_id == team_id,
            PlayerInfoData.is_active == True,
            SeasonDefensiveStatsData.year == year,
            SeasonDefensiveStatsData.total_tkls > 0
        ).order_by(desc(SeasonDefensiveStatsData.total_tkls)).all()

    def get_def_to_stats_by_team_id(self, team_id: int, year):
        return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
            PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
            PlayerInfoData.team_id == team_id,
            PlayerInfoData.is_active == True,
            SeasonDefensiveStatsData.year == year,
            SeasonDefensiveStatsData.total_tkls > 0
        ).order_by(
            desc(SeasonDefensiveStatsData.ints_made),
            desc(SeasonDefensiveStatsData.fumbles_rec)
        ).all()

    def get_passing_stats_by_team_id(self, team_id: int, year):
        return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
            PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
            PlayerInfoData.team_id == team_id,
            PlayerInfoData.is_active == True,
            SeasonOffensiveStatsData.year == year,
            SeasonOffensiveStatsData.pass_att > 0
        ).order_by(desc(SeasonOffensiveStatsData.pass_yards)).all()

    def get_receiving_stats_by_team_id(self, team_id: int, year):
        return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
            PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
            PlayerInfoData.team_id == team_id,
            PlayerInfoData.is_active == True,
            SeasonOffensiveStatsData.year == year,
            SeasonOffensiveStatsData.receptions > 0
        ).order_by(desc(SeasonOffensiveStatsData.rec_yards)).all()


    def get_rushing_stats_by_team_id(self, team_id: int, year):
        return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
            PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
            PlayerInfoData.team_id == team_id,
            PlayerInfoData.is_active == True,
            SeasonOffensiveStatsData.year == year,
            SeasonOffensiveStatsData.rush_att > 0
        ).order_by(desc(SeasonOffensiveStatsData.rush_yards)).all()

    def get_total_off_stats_by_team_id(self, team_id: int, year):
        return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
            PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
            PlayerInfoData.team_id == team_id,
            PlayerInfoData.is_active == True,
            SeasonOffensiveStatsData.year == year,
            SeasonOffensiveStatsData.total_yards > 0
        ).order_by(desc(SeasonOffensiveStatsData.total_yards)).all()

    def get_kicking_stats_by_team_id(self, team_id: int, year):
        return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
            PlayerInfoData.id == SeasonKickingStatsData.player_id,
            PlayerInfoData.team_id == team_id,
            PlayerInfoData.is_active == True,
            SeasonKickingStatsData.year == year,
            SeasonKickingStatsData.fg_att > 0
        ).order_by(desc(SeasonKickingStatsData.fg_made)).all()

    def get_punting_stats_by_team_id(self, team_id: int, year):
        return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
            PlayerInfoData.id == SeasonKickingStatsData.player_id,
            PlayerInfoData.team_id == team_id,
            PlayerInfoData.is_active == True,
            SeasonKickingStatsData.year == year,
            SeasonKickingStatsData.number_punts > 0
        ).order_by(desc(SeasonKickingStatsData.total_punt_yards)).all()

    def get_kr_stats_by_team_id(self, team_id: int, year):
        return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
            PlayerInfoData.id == SeasonReturnStatsData.player_id,
            PlayerInfoData.team_id == team_id,
            PlayerInfoData.is_active == True,
            SeasonReturnStatsData.year == year,
            SeasonReturnStatsData.kick_returns > 0
        ).order_by(desc(SeasonReturnStatsData.kr_yds)).all()

    def get_pr_stats_by_team_id(self, team_id: int, year):
        return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
            PlayerInfoData.id == SeasonReturnStatsData.player_id,
            PlayerInfoData.team_id == team_id,
            PlayerInfoData.is_active == True,
            SeasonReturnStatsData.year == year,
            SeasonReturnStatsData.punt_returns > 0
        ).order_by(desc(SeasonReturnStatsData.pr_yds)).all()

    # Users only stats
    def get_users_defensive_stats(self, year: int):
        return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
            PlayerInfoData.team_id.in_(user_team_ids),
            PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
            PlayerInfoData.is_active == True,
            SeasonDefensiveStatsData.year == year,
            SeasonDefensiveStatsData.total_tkls > 0
        ).order_by(desc(SeasonDefensiveStatsData.total_tkls)).limit(10)

    def get_users_def_to_stats(self, year: int):
        return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
            PlayerInfoData.team_id.in_(user_team_ids),
            PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
            PlayerInfoData.is_active == True,
            SeasonDefensiveStatsData.year == year,
            SeasonDefensiveStatsData.total_tkls > 0
        ).order_by(
            desc(SeasonDefensiveStatsData.ints_made),
            desc(SeasonDefensiveStatsData.fumbles_rec)
        ).limit(10)
    
    def get_users_passing_stats(self, year: int):
        return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
            PlayerInfoData.team_id.in_(user_team_ids),
            PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
            PlayerInfoData.is_active == True,
            SeasonOffensiveStatsData.year == year,
            SeasonOffensiveStatsData.pass_att > 0
        ).order_by(desc(SeasonOffensiveStatsData.pass_yards)).limit(5)

    def get_users_receiving_stats(self, year: int):
        return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
            PlayerInfoData.team_id.in_(user_team_ids),
            PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
            PlayerInfoData.is_active == True,
            SeasonOffensiveStatsData.year == year,
            SeasonOffensiveStatsData.receptions > 0
        ).order_by(desc(SeasonOffensiveStatsData.rec_yards)).limit(10)

    def get_users_rushing_stats(self, year: int):
        return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
            PlayerInfoData.team_id.in_(user_team_ids),
            PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
            PlayerInfoData.is_active == True,
            SeasonOffensiveStatsData.year == year,
            SeasonOffensiveStatsData.rush_att > 0
        ).order_by(desc(SeasonOffensiveStatsData.rush_yards)).limit(10)

    def get_users_total_off_stats(self, year: int):
        return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
            PlayerInfoData.team_id.in_(user_team_ids),
            PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
            PlayerInfoData.is_active == True,
            SeasonOffensiveStatsData.year == year,
            SeasonOffensiveStatsData.total_yards > 0
        ).order_by(desc(SeasonOffensiveStatsData.total_yards)).limit(5)

    def get_users_kicking_stats(self, year: int):
        return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
            PlayerInfoData.team_id.in_(user_team_ids),
            PlayerInfoData.id == SeasonKickingStatsData.player_id,
            PlayerInfoData.is_active == True,
            SeasonKickingStatsData.year == year,
            SeasonKickingStatsData.fg_att > 0
        ).order_by(desc(SeasonKickingStatsData.fg_made)).limit(5)

    def get_users_punting_stats(self, year: int):
        return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
            PlayerInfoData.team_id.in_(user_team_ids),
            PlayerInfoData.id == SeasonKickingStatsData.player_id,
            PlayerInfoData.is_active == True,
            SeasonKickingStatsData.year == year,
            SeasonKickingStatsData.number_punts > 0
        ).order_by(desc(SeasonKickingStatsData.total_punt_yards)).limit(5)

    def get_users_kr_stats(self, year: int):
        return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
            PlayerInfoData.team_id.in_(user_team_ids),
            PlayerInfoData.id == SeasonReturnStatsData.player_id,
            PlayerInfoData.is_active == True,
            SeasonReturnStatsData.year == year,
            SeasonReturnStatsData.kick_returns > 0
        ).order_by(desc(SeasonReturnStatsData.kr_yds)).limit(5)

    def get_users_pr_stats(self, year: int):
        return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
            PlayerInfoData.team_id.in_(user_team_ids),
            PlayerInfoData.id == SeasonReturnStatsData.player_id,
            PlayerInfoData.is_active == True,
            SeasonReturnStatsData.year == year,
            SeasonReturnStatsData.punt_returns > 0
        ).order_by(desc(SeasonReturnStatsData.pr_yds)).limit(5)
