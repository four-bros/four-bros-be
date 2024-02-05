from typing import List
from sqlalchemy import desc
from src.constants import session, user_team_ids
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.SeasonOffensiveStatsData import SeasonOffensiveStatsData

class OffensiveSeasonLeadersDataService():
    def __init__(self) -> None:
        pass

    def get_completions_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year
                ).order_by(desc(SeasonOffensiveStatsData.completions)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year
            ).order_by(desc(SeasonOffensiveStatsData.completions)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.completions)).limit(10)
        
    def get_pass_att_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year
                ).order_by(desc(SeasonOffensiveStatsData.completions)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year
            ).order_by(desc(SeasonOffensiveStatsData.completions)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.completions)).limit(10)
    
    def get_comp_pct_leaders(self, year: int, min_pass_attempts: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
                SeasonOffensiveStatsData.pass_att > min_pass_attempts
                ).order_by(desc(SeasonOffensiveStatsData.comp_pct)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
                SeasonOffensiveStatsData.pass_att > min_pass_attempts
            ).order_by(desc(SeasonOffensiveStatsData.comp_pct)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                SeasonOffensiveStatsData.pass_att > min_pass_attempts
            ).order_by(desc(SeasonOffensiveStatsData.comp_pct)).limit(10)
        
    def get_longest_pass_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year
                ).order_by(desc(SeasonOffensiveStatsData.longest_pass)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year
            ).order_by(desc(SeasonOffensiveStatsData.longest_pass)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.longest_pass)).limit(10)
        
    def get_pass_yards_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year
                ).order_by(desc(SeasonOffensiveStatsData.pass_yards)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year
            ).order_by(desc(SeasonOffensiveStatsData.pass_yards)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.pass_yards)).limit(10)
    
    def get_pass_tds_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year
                ).order_by(desc(SeasonOffensiveStatsData.pass_tds)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year
            ).order_by(desc(SeasonOffensiveStatsData.pass_tds)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.pass_tds)).limit(10)
        
    def get_ints_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year
                ).order_by(desc(SeasonOffensiveStatsData.ints)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year
            ).order_by(desc(SeasonOffensiveStatsData.ints)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.ints)).limit(10)
    
    def get_pass_ypa_leaders(self, year: int, min_pass_attempts: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
                SeasonOffensiveStatsData.pass_att > min_pass_attempts
                ).order_by(desc(SeasonOffensiveStatsData.pass_ypa)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,

            ).order_by(desc(SeasonOffensiveStatsData.pass_ypa)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                SeasonOffensiveStatsData.pass_att > min_pass_attempts
            ).order_by(desc(SeasonOffensiveStatsData.pass_ypa)).limit(10)
    
    def get_pass_ypg_leaders(self, year: int, min_pass_attempts: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
                SeasonOffensiveStatsData.pass_att > min_pass_attempts
                ).order_by(desc(SeasonOffensiveStatsData.pass_ypg)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
                SeasonOffensiveStatsData.pass_att > min_pass_attempts
            ).order_by(desc(SeasonOffensiveStatsData.pass_ypg)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                SeasonOffensiveStatsData.pass_att > min_pass_attempts
            ).order_by(desc(SeasonOffensiveStatsData.pass_ypg)).limit(10)
        
    def get_pass_rating_leaders(self, year: int, min_pass_attempts: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
                SeasonOffensiveStatsData.pass_att > min_pass_attempts
                ).order_by(desc(SeasonOffensiveStatsData.pass_ypg)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
                SeasonOffensiveStatsData.pass_att > min_pass_attempts
            ).order_by(desc(SeasonOffensiveStatsData.pass_ypg)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                SeasonOffensiveStatsData.pass_att > min_pass_attempts
            ).order_by(desc(SeasonOffensiveStatsData.pass_ypg)).limit(10)
