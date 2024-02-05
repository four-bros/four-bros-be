from typing import List
from sqlalchemy import desc
from src.constants import (session, user_team_ids)
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.SeasonReturnStatsData import SeasonReturnStatsData


class ReturnSeasonLeadersDataService():
    def __init__(self) -> None:
        pass

    def get_kick_return_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[SeasonReturnStatsData]:
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == year
            ).order_by(desc(SeasonReturnStatsData.kick_returns)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == year,
            ).order_by(desc(SeasonReturnStatsData.kick_returns)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
            ).order_by(desc(SeasonReturnStatsData.kick_returns)).limit(10)

    def get_long_kr_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[SeasonReturnStatsData]:
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == year
            ).order_by(desc(SeasonReturnStatsData.long_kr)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == year,
            ).order_by(desc(SeasonReturnStatsData.long_kr)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
            ).order_by(desc(SeasonReturnStatsData.long_kr)).limit(10)

    def get_kr_tds_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[SeasonReturnStatsData]:
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == year
            ).order_by(desc(SeasonReturnStatsData.kr_tds)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == year,
            ).order_by(desc(SeasonReturnStatsData.kr_tds)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
            ).order_by(desc(SeasonReturnStatsData.kr_tds)).limit(10)
    
    def get_kr_yards_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[SeasonReturnStatsData]:
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == year
            ).order_by(desc(SeasonReturnStatsData.kr_yds)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == year,
            ).order_by(desc(SeasonReturnStatsData.kr_yds)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
            ).order_by(desc(SeasonReturnStatsData.kr_yds)).limit(10)

    def get_kr_avg_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[SeasonReturnStatsData]:
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == year
            ).order_by(desc(SeasonReturnStatsData.kr_avg)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == year,
            ).order_by(desc(SeasonReturnStatsData.kr_avg)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
            ).order_by(desc(SeasonReturnStatsData.kr_avg)).limit(10)

    def get_pr_returns_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == year
            ).order_by(desc(SeasonReturnStatsData.punt_returns)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == year
            ).order_by(desc(SeasonReturnStatsData.punt_returns)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
            ).order_by(desc(SeasonReturnStatsData.punt_returns)).limit(10)
        
    def get_pr_long_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == year
            ).order_by(desc(SeasonReturnStatsData.long_pr)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == year
            ).order_by(desc(SeasonReturnStatsData.long_pr)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
            ).order_by(desc(SeasonReturnStatsData.long_pr)).limit(10)

    def get_pr_tds_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == year
            ).order_by(desc(SeasonReturnStatsData.pr_tds)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == year
            ).order_by(desc(SeasonReturnStatsData.pr_tds)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
            ).order_by(desc(SeasonReturnStatsData.pr_tds)).limit(10)
    
    def get_pr_yds_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == year
            ).order_by(desc(SeasonReturnStatsData.pr_yds)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == year
            ).order_by(desc(SeasonReturnStatsData.pr_yds)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
            ).order_by(desc(SeasonReturnStatsData.pr_yds)).limit(10)
    
    def get_pr_avg_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == year
            ).order_by(desc(SeasonReturnStatsData.pr_avg)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
                SeasonReturnStatsData.year == year
            ).order_by(desc(SeasonReturnStatsData.pr_avg)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonReturnStatsData).filter(
                PlayerInfoData.id == SeasonReturnStatsData.player_id,
            ).order_by(desc(SeasonReturnStatsData.pr_avg)).limit(10)
