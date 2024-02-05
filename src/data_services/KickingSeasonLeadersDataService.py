from typing import List
from sqlalchemy import desc
from src.constants import session, user_team_ids
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.SeasonKickingStatsData import SeasonKickingStatsData

class KickingSeasonLeadersDataService():
    def __init__(self) -> None:
        pass

    def get_fg_made_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.fg_made)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.fg_made)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonKickingStatsData.fg_made)).limit(10)
    
    def get_fg_att_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.fg_att)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.fg_att)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonKickingStatsData.fg_att)).limit(10)
    
    def get_fg_pct_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.fg_pct)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.fg_pct)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonKickingStatsData.fg_pct)).limit(10)
        
    def get_fg_long_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.long_fg)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.long_fg)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonKickingStatsData.long_fg)).limit(10)
    
    def get_fg_made_50_plus_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.fg_made_50_plus)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.fg_made_50_plus)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonKickingStatsData.fg_made_50_plus)).limit(10)
    
    def get_fg_50_plus_pct_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.fg_50_plus_pct)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.fg_50_plus_pct)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonKickingStatsData.fg_50_plus_pct)).limit(10)
    
    def get_punting_long_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.long_punt)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.long_punt)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonKickingStatsData.long_punt)).limit(10)
    
    def get_number_punts_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.number_punts)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.number_punts)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonKickingStatsData.number_punts)).limit(10)

    def get_total_punt_yards_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.total_punt_yards)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.total_punt_yards)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonKickingStatsData.total_punt_yards)).limit(10)
    
    def get_punt_avg_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.punt_avg)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.punt_avg)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonKickingStatsData.punt_avg)).limit(10)

    def get_net_punting_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.net_punting)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.net_punting)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonKickingStatsData.net_punting)).limit(10)
        
    def get_inside_20_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.inside_twenty)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.inside_twenty)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonKickingStatsData.inside_twenty)).limit(10)

    def get_inside_20_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.inside_twenty)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.inside_twenty)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonKickingStatsData.inside_twenty)).limit(10)
    
    def get_net_avg_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.net_avg)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonKickingStatsData.year == year
            ).order_by(desc(SeasonKickingStatsData.net_avg)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonKickingStatsData).filter(
                SeasonKickingStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonKickingStatsData.net_avg)).limit(10)
