
from typing import List
from sqlalchemy import desc
from src.constants import (
    session,
    team_season_records_schema
)
from src.data_models.TeamInfoData import TeamInfoData
from src.data_models.TeamStatsData import TeamStatsData
from src.data_models.WeekYearData import WeekYearData
from src.models.Teams import TeamSeasonRecord
from src.utils.team import _get_team_info_and_stats

def _get_team_season_stats_leaders(is_season_specific: bool):
    # If it is season specific, filter data by current year
    if is_season_specific:
        # Query Week/Year to get the current year
        week_year: WeekYearData = session.query(WeekYearData).order_by(
            desc(WeekYearData.year)
        ).first()
        # Offensive Team Records Data
        total_points_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.total_points)
        ).limit(10)

        total_yards_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.total_yards)
        ).limit(10)

        ppg_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.ppg)
        ).limit(10)

        pass_yds_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.pass_yds)
        ).limit(10)

        pass_tds_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.pass_tds)
        ).limit(10)

        ints_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.ints)
        ).limit(10)

        sacked_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.sacked)
        ).limit(10)

        rush_yds_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.rush_yds)
        ).limit(10)

        rush_tds_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.rush_tds)
        ).limit(10)

        fumbles_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.fumbles)
        ).limit(10)

        drops_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.drops)
        ).limit(10)

        off_turnovers_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.off_turnovers)
        ).limit(10)

        off_yards_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.off_yards)
        ).limit(10)

        off_ypg_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.off_ypg)
        ).limit(10)

        total_yards_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.total_yards)
        ).limit(10)

        total_ypg_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.total_ypg)
        ).limit(10)

        # Defensive Team Records Data
        sacks_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.sacks)
        ).limit(10)

        tfl_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.tfl)
        ).limit(10)

        ints_made_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.ints_made)
        ).limit(10)

        ff_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.ff)
        ).limit(10)

        fr_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.fr)
        ).limit(10)

        def_turnovers_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.def_turnovers)
        ).limit(10)

        pass_def_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.pass_def)
        ).limit(10)

        safeties_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.safeties)
        ).limit(10)

        blocked_kicks_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.blocked_kicks)
        ).limit(10)

        def_tds_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.def_tds)
        ).limit(10)

        to_margin_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.to_margin)
        ).limit(10)

        # Special Teams Team Records Data
        kr_yds_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.kr_yds)
        ).limit(10)

        kr_tds_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.kr_tds)
        ).limit(10)

        pr_yds_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.pr_yds)
        ).limit(10)

        pr_tds_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id,
            TeamStatsData.year == week_year.year
        ).order_by(
            desc(TeamStatsData.pr_tds)
        ).limit(10)

        # Convert data over to models to dump into json
        # Offense
        converted_total_points: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in total_points_data]
        converted_total_yards: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in total_yards_data]
        converted_total_ypg: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in total_ypg_data]
        converted_off_yards: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in off_yards_data]
        converted_off_ypg: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in off_ypg_data]
        converted_ppg: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in ppg_data]
        converted_pass_yds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in pass_yds_data]
        converted_pass_tds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in pass_tds_data]
        converted_ints: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in ints_data]
        converted_sacked: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in sacked_data]
        converted_rush_yds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in rush_yds_data]
        converted_rush_tds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in rush_tds_data]
        converted_fumbles: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in fumbles_data]
        converted_drops: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in drops_data]
        converted_off_turnovers: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in off_turnovers_data]
        # Defense
        converted_sacks: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in sacks_data]
        converted_tfl: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in tfl_data]
        converted_ints_made: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in ints_made_data]
        converted_ff: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in ff_data]
        converted_fr: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in fr_data]
        converted_def_turnovers: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in def_turnovers_data]
        converted_pass_def: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in pass_def_data]
        converted_safeties: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in safeties_data]
        converted_blocked_kicks: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in blocked_kicks_data]
        converted_def_tds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in def_tds_data]
        converted_to_margin: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in to_margin_data]
        # Special Teams
        converted_kr_yds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in kr_yds_data]
        converted_kr_tds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in kr_tds_data]
        converted_pr_yds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in pr_yds_data]
        converted_pr_tds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in pr_tds_data]

        # Dump models to json for api response
        # Offense
        total_points_json = team_season_records_schema.dump(converted_total_points)
        total_yards_json = team_season_records_schema.dump(converted_total_yards)
        total_ypg_json = team_season_records_schema.dump(converted_total_ypg)
        off_yards_json = team_season_records_schema.dump(converted_off_yards)
        off_ypg_json = team_season_records_schema.dump(converted_off_ypg)
        ppg_json = team_season_records_schema.dump(converted_ppg)
        pass_yds_json = team_season_records_schema.dump(converted_pass_yds)
        pass_tds_json = team_season_records_schema.dump(converted_pass_tds)
        ints_json = team_season_records_schema.dump(converted_ints)
        sacked_json = team_season_records_schema.dump(converted_sacked)
        rush_yds_json = team_season_records_schema.dump(converted_rush_yds)
        rush_tds_json = team_season_records_schema.dump(converted_rush_tds)
        fumbles_json = team_season_records_schema.dump(converted_fumbles)
        drops_json = team_season_records_schema.dump(converted_drops)
        off_turnovers_json = team_season_records_schema.dump(converted_off_turnovers)
        # Defense
        sacks_json = team_season_records_schema.dump(converted_sacks)
        tfl_json = team_season_records_schema.dump(converted_tfl)
        ints_made_json = team_season_records_schema.dump(converted_ints_made)
        ff_json = team_season_records_schema.dump(converted_ff)
        fr_json = team_season_records_schema.dump(converted_fr)
        def_turnovers_json = team_season_records_schema.dump(converted_def_turnovers)
        pass_def_json = team_season_records_schema.dump(converted_pass_def)
        safeties_json = team_season_records_schema.dump(converted_safeties)
        blocked_kicks_json = team_season_records_schema.dump(converted_blocked_kicks)
        def_tds_json = team_season_records_schema.dump(converted_def_tds)
        to_margin_json = team_season_records_schema.dump(converted_to_margin)
        # Special Teams
        kr_yds_json = team_season_records_schema.dump(converted_kr_yds)
        kr_tds_json = team_season_records_schema.dump(converted_kr_tds)
        pr_yds_json = team_season_records_schema.dump(converted_pr_yds)
        pr_tds_json = team_season_records_schema.dump(converted_pr_tds)

        response = {
            'offense': {
                'points': total_points_json,
                'off_yards': off_yards_json,
                'off_ypg': off_ypg_json,
                'total_yards': total_yards_json,
                'total_ypg': total_ypg_json,
                'ppg': ppg_json,
                'pass_yards': pass_yds_json,
                'pass_tds': pass_tds_json,
                'ints': ints_json,
                'sacked': sacked_json,
                'rush_yards': rush_yds_json,
                'rush_tds': rush_tds_json,
                'fumbles': fumbles_json,
                'drops': drops_json,
                'turnovers': off_turnovers_json
            },
            'defense': {
                'sacks': sacks_json,
                'tfl': tfl_json,
                'ints_made': ints_made_json,
                'ff': ff_json,
                'fr': fr_json,
                'turnovers': def_turnovers_json,
                'pass_def': pass_def_json,
                'safeties': safeties_json,
                'blocked_kicks': blocked_kicks_json,
                'def_td': def_tds_json,
                'to_margin': to_margin_json
            },
            'special_teams': {
                'kr_yds': kr_yds_json,
                'kr_tds': kr_tds_json,
                'pr_yds': pr_yds_json,
                'pr_tds': pr_tds_json,
            }
        }

        return response

    # If not season specific, get all time records (do not filter by year)
    else:
        # Offensive Team Records Data
        total_points_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.total_points)
        ).limit(10)

        total_yards_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.total_yards)
        ).limit(10)

        ppg_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.ppg)
        ).limit(10)

        pass_yds_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.pass_yds)
        ).limit(10)

        pass_tds_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.pass_tds)
        ).limit(10)

        ints_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.ints)
        ).limit(10)

        sacked_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.sacked)
        ).limit(10)

        rush_yds_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.rush_yds)
        ).limit(10)

        rush_tds_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.rush_tds)
        ).limit(10)

        fumbles_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.fumbles)
        ).limit(10)

        drops_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.drops)
        ).limit(10)

        off_turnovers_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.off_turnovers)
        ).limit(10)

        off_yards_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.off_yards)
        ).limit(10)

        off_ypg_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.off_ypg)
        ).limit(10)

        total_yards_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.total_yards)
        ).limit(10)

        total_ypg_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.total_ypg)
        ).limit(10)

        # Defensive Team Records Data
        sacks_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.sacks)
        ).limit(10)

        tfl_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.tfl)
        ).limit(10)

        ints_made_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.ints_made)
        ).limit(10)

        ff_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.ff)
        ).limit(10)

        fr_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.fr)
        ).limit(10)

        def_turnovers_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.def_turnovers)
        ).limit(10)

        pass_def_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.pass_def)
        ).limit(10)

        safeties_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.safeties)
        ).limit(10)

        blocked_kicks_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.blocked_kicks)
        ).limit(10)

        def_tds_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.def_tds)
        ).limit(10)

        to_margin_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.to_margin)
        ).limit(10)

        # Special Teams Team Records Data
        kr_yds_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.kr_yds)
        ).limit(10)

        kr_tds_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.kr_tds)
        ).limit(10)

        pr_yds_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.pr_yds)
        ).limit(10)

        pr_tds_data = session.query(TeamInfoData, TeamStatsData).filter(
            TeamInfoData.id == TeamStatsData.team_id
        ).order_by(
            desc(TeamStatsData.pr_tds)
        ).limit(10)

        # Convert data over to models to dump into json
        # Offense
        converted_total_points: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in total_points_data]
        converted_total_yards: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in total_yards_data]
        converted_total_ypg: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in total_ypg_data]
        converted_off_yards: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in off_yards_data]
        converted_off_ypg: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in off_ypg_data]
        converted_ppg: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in ppg_data]
        converted_pass_yds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in pass_yds_data]
        converted_pass_tds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in pass_tds_data]
        converted_ints: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in ints_data]
        converted_sacked: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in sacked_data]
        converted_rush_yds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in rush_yds_data]
        converted_rush_tds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in rush_tds_data]
        converted_fumbles: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in fumbles_data]
        converted_drops: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in drops_data]
        converted_off_turnovers: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in off_turnovers_data]
        # Defense
        converted_sacks: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in sacks_data]
        converted_tfl: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in tfl_data]
        converted_ints_made: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in ints_made_data]
        converted_ff: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in ff_data]
        converted_fr: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in fr_data]
        converted_def_turnovers: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in def_turnovers_data]
        converted_pass_def: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in pass_def_data]
        converted_safeties: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in safeties_data]
        converted_blocked_kicks: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in blocked_kicks_data]
        converted_def_tds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in def_tds_data]
        converted_to_margin: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in to_margin_data]
        # Special Teams
        converted_kr_yds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in kr_yds_data]
        converted_kr_tds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in kr_tds_data]
        converted_pr_yds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in pr_yds_data]
        converted_pr_tds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in pr_tds_data]

        # Dump models to json for api response
        # Offense
        total_points_json = team_season_records_schema.dump(converted_total_points)
        total_yards_json = team_season_records_schema.dump(converted_total_yards)
        total_ypg_json = team_season_records_schema.dump(converted_total_ypg)
        off_yards_json = team_season_records_schema.dump(converted_off_yards)
        off_ypg_json = team_season_records_schema.dump(converted_off_ypg)
        ppg_json = team_season_records_schema.dump(converted_ppg)
        pass_yds_json = team_season_records_schema.dump(converted_pass_yds)
        pass_tds_json = team_season_records_schema.dump(converted_pass_tds)
        ints_json = team_season_records_schema.dump(converted_ints)
        sacked_json = team_season_records_schema.dump(converted_sacked)
        rush_yds_json = team_season_records_schema.dump(converted_rush_yds)
        rush_tds_json = team_season_records_schema.dump(converted_rush_tds)
        fumbles_json = team_season_records_schema.dump(converted_fumbles)
        drops_json = team_season_records_schema.dump(converted_drops)
        off_turnovers_json = team_season_records_schema.dump(converted_off_turnovers)
        # Defense
        sacks_json = team_season_records_schema.dump(converted_sacks)
        tfl_json = team_season_records_schema.dump(converted_tfl)
        ints_made_json = team_season_records_schema.dump(converted_ints_made)
        ff_json = team_season_records_schema.dump(converted_ff)
        fr_json = team_season_records_schema.dump(converted_fr)
        def_turnovers_json = team_season_records_schema.dump(converted_def_turnovers)
        pass_def_json = team_season_records_schema.dump(converted_pass_def)
        safeties_json = team_season_records_schema.dump(converted_safeties)
        blocked_kicks_json = team_season_records_schema.dump(converted_blocked_kicks)
        def_tds_json = team_season_records_schema.dump(converted_def_tds)
        to_margin_json = team_season_records_schema.dump(converted_to_margin)
        # Special Teams
        kr_yds_json = team_season_records_schema.dump(converted_kr_yds)
        kr_tds_json = team_season_records_schema.dump(converted_kr_tds)
        pr_yds_json = team_season_records_schema.dump(converted_pr_yds)
        pr_tds_json = team_season_records_schema.dump(converted_pr_tds)

        response = {
            'offense': {
                'points': total_points_json,
                'off_yards': off_yards_json,
                'off_ypg': off_ypg_json,
                'total_yards': total_yards_json,
                'total_ypg': total_ypg_json,
                'ppg': ppg_json,
                'pass_yards': pass_yds_json,
                'pass_tds': pass_tds_json,
                'ints': ints_json,
                'sacked': sacked_json,
                'rush_yards': rush_yds_json,
                'rush_tds': rush_tds_json,
                'fumbles': fumbles_json,
                'drops': drops_json,
                'turnovers': off_turnovers_json
            },
            'defense': {
                'sacks': sacks_json,
                'tfl': tfl_json,
                'ints_made': ints_made_json,
                'ff': ff_json,
                'fr': fr_json,
                'turnovers': def_turnovers_json,
                'pass_def': pass_def_json,
                'safeties': safeties_json,
                'blocked_kicks': blocked_kicks_json,
                'def_td': def_tds_json,
                'to_margin': to_margin_json
            },
            'special_teams': {
                'kr_yds': kr_yds_json,
                'kr_tds': kr_tds_json,
                'pr_yds': pr_yds_json,
                'pr_tds': pr_tds_json,
            }
        }

        return response