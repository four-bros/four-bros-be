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
        
    def get_receptions_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
                ).order_by(desc(SeasonOffensiveStatsData.receptions)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.receptions)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.receptions)).limit(10)
    
    def get_rec_yards_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.rec_yards)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.rec_yards)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.rec_yards)).limit(10)

    def get_rec_tds_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.rec_tds)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.rec_tds)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.rec_tds)).limit(10)
    
    def get_yac_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.yac)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.yac)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.yac)).limit(10)

    def get_drops_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.drops)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.drops)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.drops)).limit(10)
    
    def get_rec_ypc_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.rec_ypc)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.rec_ypc)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.rec_ypc)).limit(10)
    
    def get_rec_ypg_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.rec_ypg)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.rec_ypg)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.rec_ypg)).limit(10)

    def get_rush_att_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.rush_att)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.rush_att)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.rush_att)).limit(10)

    def get_rush_yards_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.rush_yards)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.rush_yards)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.rush_yards)).limit(10)
    
    def get_ya_contact_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.ya_contact)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.ya_contact)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.ya_contact)).limit(10)

    def get_broke_tkls_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.broke_tkls)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.broke_tkls)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.broke_tkls)).limit(10)

    def get_fumbles_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.fumbles)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.fumbles)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.fumbles)).limit(10)

    def get_twenty_plus_yd_runs_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.twenty_plus_yd_runs)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.twenty_plus_yd_runs)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.twenty_plus_yd_runs)).limit(10)

    def get_rush_ypc_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.rush_ypc)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.rush_ypc)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.rush_ypc)).limit(10)
        
    def get_rush_ypg_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.rush_ypg)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.rush_ypg)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.rush_ypg)).limit(10)

    def get_rush_tds_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.rush_tds)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.rush_tds)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.rush_tds)).limit(10)

    def get_total_yards_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.total_yards)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.total_yards)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.total_yards)).limit(10)
    
    def get_total_tds_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.total_tds)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.total_tds)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.total_tds)).limit(10)

    def get_total_ypg_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.total_ypg)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.total_ypg)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.total_ypg)).limit(10)

    def get_turnovers_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.turnovers)).limit(10)
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
                PlayerInfoData.team_id.in_(user_team_ids),
                SeasonOffensiveStatsData.year == year,
            ).order_by(desc(SeasonOffensiveStatsData.turnovers)).limit(10)
        else:
            return session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
                SeasonOffensiveStatsData.player_id == PlayerInfoData.id,
            ).order_by(desc(SeasonOffensiveStatsData.turnovers)).limit(10)
