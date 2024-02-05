from typing import List
from sqlalchemy import desc
from src.constants import session, user_team_ids
from src.data_models.TeamInfoData import TeamInfoData
from src.data_models.TeamSeasonStatsData import TeamSeasonStatsData

class TeamSeasonStatsDataService():
    def __init__(self) -> None:
        pass

    def get_team_stats_by_id(self, team_id: int, year: int):
        return session.query(TeamSeasonStatsData).where(
            TeamSeasonStatsData.team_id == team_id,
            TeamSeasonStatsData.year == year
        ).scalar()

    # Offensive methods
    def get_total_points_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.total_points)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.total_points)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.total_points)).limit(10)

    def get_total_yards_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.total_yards)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.total_yards)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.total_yards)).limit(10)

    def get_ppg_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.ppg)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.ppg)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.ppg)).limit(10)

    def get_pass_yards_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.pass_yds)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.pass_yds)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.pass_yds)).limit(10)

    def get_pass_tds_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.pass_tds)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.pass_tds)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.pass_tds)).limit(10)

    def get_pass_ints_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.ints)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.ints)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.ints)).limit(10)

    def get_sacked_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.sacked)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.sacked)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.sacked)).limit(10)

    def get_rush_yards_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.rush_yds)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.rush_yds)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.rush_yds)).limit(10)

    def get_rush_tds_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.rush_tds)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.rush_tds)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.rush_tds)).limit(10)

    def get_fumbles_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.fumbles)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.fumbles)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.fumbles)).limit(10)

    def get_drops_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.drops)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.drops)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.drops)).limit(10)

    def get_off_turnovers_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.off_turnovers)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.off_turnovers)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.off_turnovers)).limit(10)

    def get_off_yards_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.off_yards)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.off_yards)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.off_yards)).limit(10)

    def get_off_ypg_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.off_ypg)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.off_ypg)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.off_ypg)).limit(10)

    def get_total_yards_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.total_yards)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.total_yards)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.total_yards)).limit(10)

    def get_total_ypg_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.total_ypg)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.total_ypg)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.total_ypg)).limit(10)

    # Defensive methods
    def get_sacks_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.sacks)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.sacks)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.sacks)).limit(10)

    def get_tfl_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.tfl)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.tfl)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.tfl)).limit(10)

    def get_ints_made_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.ints_made)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.ints_made)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.ints_made)).limit(10)

    def get_ff_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.ff)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.ff)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.ff)).limit(10)

    def get_fr_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.fr)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.fr)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.fr)).limit(10)

    def get_def_turnovers_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.def_turnovers)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.def_turnovers)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.def_turnovers)).limit(10)

    def get_pass_def_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.pass_def)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.pass_def)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.pass_def)).limit(10)

    def get_safeties_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.safeties)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.safeties)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.safeties)).limit(10)

    def get_blocked_kicks_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.blocked_kicks)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.blocked_kicks)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.blocked_kicks)).limit(10)

    def get_def_tds_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.def_tds)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.def_tds)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.def_tds)).limit(10)

    def get_to_margin_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.to_margin)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.to_margin)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.to_margin)).limit(10)

    # Special Teams methods
    def get_kr_yards_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.kr_yds)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.kr_yds)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.kr_yds)).limit(10)

    def get_kr_tds_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.kr_tds)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.kr_tds)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.kr_tds)).limit(10)

    def get_pr_yards_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.pr_yds)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.pr_yds)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.pr_yds)).limit(10)

    def get_pr_tds_leaders(self, year: int, is_season_specific: bool, is_users_only: bool) -> List[TeamInfoData]:
        if is_season_specific and not is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.pr_tds)).limit(10)
        if is_season_specific and is_users_only:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id.in_(user_team_ids),
                TeamInfoData.id == TeamSeasonStatsData.team_id,
                TeamSeasonStatsData.year == year
            ).order_by(desc(TeamSeasonStatsData.pr_tds)).limit(10)
        else:
            return session.query(TeamInfoData, TeamSeasonStatsData).filter(
                TeamInfoData.id == TeamSeasonStatsData.team_id,
            ).order_by(desc(TeamSeasonStatsData.pr_tds)).limit(10)
