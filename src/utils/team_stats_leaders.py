
from typing import List
from sqlalchemy import desc
from src.constants import (
    session,
    team_season_records_schema
)
from src.data_models.TeamInfoData import TeamInfoData
from src.data_models.TeamStatsData import TeamStatsData
from src.models.Teams import TeamSeasonRecord
from src.utils.team import _get_team_info_and_stats

def _get_team_season_records():

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

    # Defensive Team Records Data
    sacks_data = session.query(TeamInfoData, TeamStatsData).filter(
        TeamInfoData.id == TeamStatsData.team_id
    ).order_by(
        desc(TeamStatsData.sacks)
    ).limit(10)

    ints_data = session.query(TeamInfoData, TeamStatsData).filter(
        TeamInfoData.id == TeamStatsData.team_id
    ).order_by(
        desc(TeamStatsData.ints)
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

    turnovers_data = session.query(TeamInfoData, TeamStatsData).filter(
        TeamInfoData.id == TeamStatsData.team_id
    ).order_by(
        desc(TeamStatsData.turnovers)
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
    converted_ppg: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in ppg_data]
    converted_pass_yds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in pass_yds_data]
    converted_pass_tds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in pass_tds_data]
    converted_rush_yds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in rush_yds_data]
    converted_rush_tds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in rush_tds_data]
    # Defense
    converted_sacks: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in sacks_data]
    converted_ints: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in ints_data]
    converted_ff: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in ff_data]
    converted_fr: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in fr_data]
    converted_turnovers: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in turnovers_data]
    converted_pass_def: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in pass_def_data]
    converted_safeties: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in safeties_data]
    converted_blocked_kicks: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in blocked_kicks_data]
    converted_def_tds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in def_tds_data]
    # Special Teams
    converted_kr_yds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in kr_yds_data]
    converted_kr_tds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in kr_tds_data]
    converted_pr_yds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in pr_yds_data]
    converted_pr_tds: List[TeamSeasonRecord] = [_get_team_info_and_stats(team) for team in pr_tds_data]


    # Dump models to json for api response
    # Offense
    total_points_json = team_season_records_schema.dump(converted_total_points)
    total_yards_json = team_season_records_schema.dump(converted_total_yards)
    ppg_json = team_season_records_schema.dump(converted_ppg)
    pass_yds_json = team_season_records_schema.dump(converted_pass_yds)
    pass_tds_json = team_season_records_schema.dump(converted_pass_tds)
    rush_yds_json = team_season_records_schema.dump(converted_rush_yds)
    rush_tds_json = team_season_records_schema.dump(converted_rush_tds)
    # Defense
    sacks_json = team_season_records_schema.dump(converted_sacks)
    ints_json = team_season_records_schema.dump(converted_ints)
    ff_json = team_season_records_schema.dump(converted_ff)
    fr_json = team_season_records_schema.dump(converted_fr)
    turnovers_json = team_season_records_schema.dump(converted_turnovers)
    pass_def_json = team_season_records_schema.dump(converted_pass_def)
    safeties_json = team_season_records_schema.dump(converted_safeties)
    blocked_kicks_json = team_season_records_schema.dump(converted_blocked_kicks)
    def_tds_json = team_season_records_schema.dump(converted_def_tds)
    # Special Teams
    kr_yds_json = team_season_records_schema.dump(converted_kr_yds)
    kr_tds_json = team_season_records_schema.dump(converted_kr_tds)
    pr_yds_json = team_season_records_schema.dump(converted_pr_yds)
    pr_tds_json = team_season_records_schema.dump(converted_pr_tds)

    response = {
        'offense': {
            'points': total_points_json,
            'yards': total_yards_json,
            'ppg': ppg_json,
            'pass_yards': pass_yds_json,
            'pass_tds': pass_tds_json,
            'rush_yards': rush_yds_json,
            'rush_tds': rush_tds_json
        },
        'defense': {
            'sacks': sacks_json,
            'ints': ints_json,
            'ff': ff_json,
            'fr': fr_json,
            'turnovers': turnovers_json,
            'pass_def': pass_def_json,
            'safeties': safeties_json,
            'blocked_kicks': blocked_kicks_json,
            'def_td': def_tds_json
        },
        'special_teams': {
            'kr_yds': kr_yds_json,
            'kr_tds': kr_tds_json,
            'pr_yds': pr_yds_json,
            'pr_tds': pr_tds_json,
        }
    }

    return response
