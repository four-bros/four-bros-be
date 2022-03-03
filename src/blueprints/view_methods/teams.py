from typing import List
from sqlalchemy.sql.expression import desc

from src.constants import(
    defensive_stats_schema,
    kicking_stats_schema,
    passing_stats_schema,
    receiving_stats_schema,
    return_stats_schema,
    rushing_stats_schema,
    session,
    team_details_schema,
    team_schema
)
from src.data_models.SeasonDefensiveStatsData import SeasonDefensiveStatsData
from src.data_models.SeasonKickingStatsData import SeasonKickingStatsData
from src.data_models.SeasonOffensiveStatsData import SeasonOffensiveStatsData
from src.data_models.SeasonReturnStatsData import SeasonReturnStatsData
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.TeamInfoData import TeamInfoData
from src.data_models.TeamStatsData import TeamStatsData
from src.data_models.WeekYearData import WeekYearData
from src.utils.player import (
    _get_player_defensive_stats,
    _get_player_kicking_stats,
    _get_player_passing_stats,
    _get_player_receiving_stats,
    _get_player_return_stats,
    _get_player_rushing_stats
)
from src.utils.team_stats import (
    _get_team_details,
    _get_team_roster,
    _get_team_stats
)
from src.models.Stats import (
    PlayerDefensiveStats,
    PlayerKickingStats,
    PlayerPassingStats,
    PlayerReceivingStats,
    PlayerReturnStats,
    PlayerRushingStats
)
from src.models.Teams import TeamDetails, TeamInfo, TeamRoster, TeamStats
from src.responses.Teams import TeamDetailsSchema, TeamInfoSchema


def get_all_teams(request):
    
    teams: List[TeamInfoData] = session.query(TeamInfoData).order_by(desc(TeamInfoData.is_user)).all()
    teams_json = team_details_schema.dump(teams)
    
    response = {
        'teams': teams_json
    }
    
    return response


def get_team_by_team_id(request, team_id) -> TeamDetailsSchema:
    
    team_info_data: TeamInfoData = session.query(TeamInfoData).where(TeamInfoData.id == team_id).one()
    team_stats_data: TeamStatsData = session.query(TeamStatsData).where(TeamStatsData.id == team_id).one()

    players: List[PlayerInfoData] = session.query(PlayerInfoData).where(
        PlayerInfoData.team_id == team_id).order_by(desc(PlayerInfoData.overall)).all()

    team_details: TeamDetails = _get_team_details(team_info=team_info_data, players=players)
    team_roster: TeamRoster = [_get_team_roster(player) for player in players]
    team_stats: TeamStats = _get_team_stats(team_stats_data=team_stats_data)

    team_info: TeamInfo = TeamInfo(
        team_details=team_details,
        team_roster=team_roster,
        team_stats=team_stats
    )

    response: TeamInfoSchema = team_schema.dump(team_info)
    
    return response


def get_team_player_stats(request, team_id):
    # Query the year to filter out irrelevant years
    week_year: WeekYearData = session.query(WeekYearData).order_by(
        desc(WeekYearData.year),
        desc(WeekYearData.week)
    ).first()
    # Query the team to get the team_id
    team: TeamInfoData = session.query(TeamInfoData).where(TeamInfoData.id == team_id).one()

    # Get defensive stats
    defense_data = session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
        PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
        PlayerInfoData.team_id == team.id,
        SeasonDefensiveStatsData.year == week_year.year,
        SeasonDefensiveStatsData.total_tkls > 0
    ).order_by(desc(SeasonDefensiveStatsData.total_tkls)).all()

    # Get offensive stats
    passing_data = session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
        PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
        PlayerInfoData.team_id == team.id,
        SeasonOffensiveStatsData.year == week_year.year,
        SeasonOffensiveStatsData.pass_att > 0
    ).order_by(desc(SeasonOffensiveStatsData.pass_yards)).all()

    receiving_data = session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
        PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
        PlayerInfoData.team_id == team.id,
        SeasonOffensiveStatsData.year == week_year.year,
        SeasonOffensiveStatsData.receptions > 0
    ).order_by(desc(SeasonOffensiveStatsData.rec_yards)).all()

    rushing_data = session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
        PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
        PlayerInfoData.team_id == team.id,
        SeasonOffensiveStatsData.year == week_year.year,
        SeasonOffensiveStatsData.rush_att > 0
    ).order_by(desc(SeasonOffensiveStatsData.rush_yards)).all()

    # Get kicking stats
    kicking_data = session.query(PlayerInfoData, SeasonKickingStatsData).filter(
        PlayerInfoData.id == SeasonKickingStatsData.player_id,
        PlayerInfoData.team_id == team.id,
        SeasonKickingStatsData.year == week_year.year,
        SeasonKickingStatsData.fg_att > 0
    ).order_by(desc(SeasonKickingStatsData.fg_made)).all()

    punting_data = session.query(PlayerInfoData, SeasonKickingStatsData).filter(
        PlayerInfoData.id == SeasonKickingStatsData.player_id,
        PlayerInfoData.team_id == team.id,
        SeasonKickingStatsData.year == week_year.year,
        SeasonKickingStatsData.number_punts > 0
    ).order_by(desc(SeasonKickingStatsData.total_punt_yards)).all()

    # Get return stats
    kick_return_data = session.query(PlayerInfoData, SeasonReturnStatsData).filter(
        PlayerInfoData.id == SeasonReturnStatsData.player_id,
        PlayerInfoData.team_id == team.id,
        SeasonReturnStatsData.year == week_year.year,
        SeasonReturnStatsData.kick_returns > 0
    ).order_by(desc(SeasonReturnStatsData.kr_yds)).all()

    punt_return_data = session.query(PlayerInfoData, SeasonReturnStatsData).filter(
        PlayerInfoData.id == SeasonReturnStatsData.player_id,
        PlayerInfoData.team_id == team.id,
        SeasonReturnStatsData.year == week_year.year,
        SeasonReturnStatsData.punt_returns > 0
    ).order_by(desc(SeasonReturnStatsData.pr_yds)).all()

    # Convert players to the appropriate models based on stat category
    defensive_stats: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in defense_data]
    kick_return_stats: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in kick_return_data]
    kick_stats: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in kicking_data]
    passing_stats: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in passing_data]
    punt_return_stats: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in punt_return_data]
    punt_stats: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in punting_data]
    receiving_stats: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in receiving_data]
    rushing_stats: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in rushing_data]

    # Convert players to json for response
    defensive_stats_json = defensive_stats_schema.dump(defensive_stats)
    kicking_stats_json = kicking_stats_schema.dump(kick_stats)
    kick_return_stats_json = return_stats_schema.dump(kick_return_stats)
    passing_stats_json = passing_stats_schema.dump(passing_stats)
    punt_return_json = return_stats_schema.dump(punt_return_stats)
    punting_stats_json = kicking_stats_schema.dump(punt_stats)
    receiving_stats_json = receiving_stats_schema.dump(receiving_stats)
    rushing_stats_json = rushing_stats_schema.dump(rushing_stats)

    response = {
        'defense': defensive_stats_json,
        'kicking': kicking_stats_json,
        'kick_return': kick_return_stats_json,
        'passing': passing_stats_json,
        'punting': punting_stats_json,
        'punt_return': punt_return_json,
        'receiving': receiving_stats_json,
        'rushing': rushing_stats_json
    }

    return response
