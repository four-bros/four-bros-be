from typing import List
from sqlalchemy import desc
from src.constants import (session, user_team_ids)
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.SeasonDefensiveStatsData import SeasonDefensiveStatsData


class DefensiveSeasonLeadersDataService():
    def __init__(self) -> None:
        pass

    def get_long_int_ret_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[SeasonDefensiveStatsData]:
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.sacks)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.long_int_ret)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
            ).order_by(desc(SeasonDefensiveStatsData.long_int_ret)).limit(10)

    def get_sacks_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.long_int_ret)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.sacks)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
            ).order_by(desc(SeasonDefensiveStatsData.sacks)).limit(10)

    def get_ff_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.forced_fumbles)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.forced_fumbles)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
            ).order_by(desc(SeasonDefensiveStatsData.forced_fumbles)).limit(10)

    def get_safeties_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.safeties)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.safeties)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
            ).order_by(desc(SeasonDefensiveStatsData.safeties)).limit(10)

    def get_pass_def_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.pass_def)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.pass_def)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
            ).order_by(desc(SeasonDefensiveStatsData.pass_def)).limit(10)

    def get_blocked_kicks_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.blocked_kicks)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.blocked_kicks)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
            ).order_by(desc(SeasonDefensiveStatsData.blocked_kicks)).limit(10)

    def get_tfl_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.tfl)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.tfl)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
            ).order_by(desc(SeasonDefensiveStatsData.tfl)).limit(10)

    def get_ints_made_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.ints_made)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.ints_made)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
            ).order_by(desc(SeasonDefensiveStatsData.ints_made)).limit(10)

    def get_fr_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.fumbles_rec)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.fumbles_rec)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
            ).order_by(desc(SeasonDefensiveStatsData.fumbles_rec)).limit(10)

    def get_fr_yards_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.fum_rec_yards)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.fum_rec_yards)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
            ).order_by(desc(SeasonDefensiveStatsData.fum_rec_yards)).limit(10)

    def get_def_td_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.def_tds)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.def_tds)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
            ).order_by(desc(SeasonDefensiveStatsData.def_tds)).limit(10)

    def get_int_ret_yards_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.int_ret_yards)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.int_ret_yards)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
            ).order_by(desc(SeasonDefensiveStatsData.int_ret_yards)).limit(10)

    def get_total_tackles_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.total_tkls)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.total_tkls)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
            ).order_by(desc(SeasonDefensiveStatsData.total_tkls)).limit(10)

    def get_total_sacks_leaders(self, year: int, is_season_specific: bool, is_users_only: bool):
        # returns all players for a specific season
        if is_season_specific and not is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.total_sacks)).limit(10)
        # returns all user players for a specific season
        elif is_season_specific and is_users_only:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.team_id.in_(user_team_ids),
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
                SeasonDefensiveStatsData.year == year
            ).order_by(desc(SeasonDefensiveStatsData.total_sacks)).limit(10)
        # returns all players for all seasons
        else:
            return session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
                PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
            ).order_by(desc(SeasonDefensiveStatsData.total_sacks)).limit(10)
