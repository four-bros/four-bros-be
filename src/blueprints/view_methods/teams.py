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
        PlayerInfoData.team_id == team_id).all()

    players.sort(key=lambda p: p.overall, reverse=True)

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
    week_year: WeekYearData = session.query(WeekYearData).first()
    # Query the team to get the team_id
    team: TeamInfoData = session.query(TeamInfoData).where(TeamInfoData.id == team_id).one()

    # Get defensive stats
    defense_data = session.query(PlayerInfoData, SeasonDefensiveStatsData).filter(
        PlayerInfoData.id == SeasonDefensiveStatsData.player_id,
        PlayerInfoData.team_id == team.id,
        SeasonDefensiveStatsData.year == week_year.year,
        SeasonDefensiveStatsData.total_tkls > 0
    ).all()

    # Get offensive stats
    passing_data = session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
        PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
        PlayerInfoData.team_id == team.id,
        SeasonOffensiveStatsData.year == week_year.year,
        SeasonOffensiveStatsData.pass_att > 0
        ).all()

    receiving_data = session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
        PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
        PlayerInfoData.team_id == team.id,
        SeasonOffensiveStatsData.year == week_year.year,
        SeasonOffensiveStatsData.receptions > 0
        ).all()

    rushing_data = session.query(PlayerInfoData, SeasonOffensiveStatsData).filter(
        PlayerInfoData.id == SeasonOffensiveStatsData.player_id,
        PlayerInfoData.team_id == team.id,
        SeasonOffensiveStatsData.year == week_year.year,
        SeasonOffensiveStatsData.rush_att > 0
        ).all()

    # Get kicking stats
    kicking_data = session.query(PlayerInfoData, SeasonKickingStatsData).filter(
        PlayerInfoData.id == SeasonKickingStatsData.player_id,
        PlayerInfoData.team_id == team.id,
        SeasonKickingStatsData.year == week_year.year,
        SeasonKickingStatsData.fg_att > 0
    ).all()

    punting_data = session.query(PlayerInfoData, SeasonKickingStatsData).filter(
        PlayerInfoData.id == SeasonKickingStatsData.player_id,
        PlayerInfoData.team_id == team.id,
        SeasonKickingStatsData.year == week_year.year,
        SeasonKickingStatsData.number_punts > 0
    ).all()

    # Get return stats
    kick_return_data = session.query(PlayerInfoData, SeasonReturnStatsData).filter(
        PlayerInfoData.id == SeasonReturnStatsData.player_id,
        PlayerInfoData.team_id == team.id,
        SeasonReturnStatsData.year == week_year.year,
        SeasonReturnStatsData.kick_returns > 0
    ).all()

    punt_return_data = session.query(PlayerInfoData, SeasonReturnStatsData).filter(
        PlayerInfoData.id == SeasonReturnStatsData.player_id,
        PlayerInfoData.team_id == team.id,
        SeasonReturnStatsData.year == week_year.year,
        SeasonReturnStatsData.punt_returns > 0
    ).all()

    # Convert players to the appropriate models based on stat category
    converted_players_defense: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in defense_data]
    converted_players_passing: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in passing_data]
    converted_players_receiving: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in receiving_data]
    converted_players_rushing: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in rushing_data]
    converted_players_kicking: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in kicking_data]
    converted_players_punting: List[PlayerKickingStats] = [_get_player_kicking_stats(player) for player in punting_data]
    converted_players_kick_return: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in kick_return_data]
    converted_players_punt_return: List[PlayerReturnStats] = [_get_player_return_stats(player) for player in punt_return_data]
    # Sort converted players based on stat category
    # All stats
    defensive_stats = sorted(converted_players_defense, key=lambda p: p.defensive_stats.solo_tkls, reverse=True)
    passing_stats = sorted(converted_players_passing, key=lambda p: p.passing_stats.pass_yards, reverse=True)
    receiving_stats = sorted(converted_players_receiving, key=lambda p: p.receiving_stats.rec_yards, reverse=True)
    rushing_stats = sorted(converted_players_rushing, key=lambda p: p.rushing_stats.rush_yards, reverse=True)
    kick_return_stats = sorted(converted_players_kick_return, key=lambda p: p.return_stats.kr_yds, reverse=True)
    punt_return_data = sorted(converted_players_kick_return, key=lambda p: p.return_stats.pr_yds, reverse=True)
    kick_stats = sorted(converted_players_kicking, key=lambda p: p.kicking_stats.fg_made, reverse=True)
    punt_stats = sorted(converted_players_punting, key=lambda p: p.kicking_stats.number_punts, reverse=True)
    # Stats leaders
    defensive_leaders = sorted(converted_players_defense, key=lambda p: p.defensive_stats.solo_tkls, reverse=True)[:3]
    passing_leaders = sorted(converted_players_passing, key=lambda p: p.passing_stats.pass_yards, reverse=True)[:3]
    receiving_leaders = sorted(converted_players_receiving, key=lambda p: p.receiving_stats.rec_yards, reverse=True)[:3]
    rushing_leaders = sorted(converted_players_rushing, key=lambda p: p.rushing_stats.rush_yards, reverse=True)[:3]
    kick_return_leaders = sorted(converted_players_kick_return, key=lambda p: p.return_stats.kr_yds, reverse=True)[:3]
    kicking_leaders = sorted(converted_players_kicking, key=lambda p: p.kicking_stats.fg_made, reverse=True)[:3]
    punt_return_leaders = sorted(converted_players_punt_return, key=lambda p: p.return_stats.pr_yds, reverse=True)[:3]
    punting_leaders = sorted(converted_players_punting, key=lambda p: p.kicking_stats.number_punts, reverse=True)[:3]
    # Convert players to json for response
    # All stats
    defensive_stats_json = defensive_stats_schema.dump(defensive_stats)
    kicking_stats_json = kicking_stats_schema.dump(kick_stats)
    kick_return_stats_json = return_stats_schema.dump(kick_return_stats)
    passing_stats_json = passing_stats_schema.dump(passing_stats)
    punting_stats_json = kicking_stats_schema.dump(punt_stats)
    punt_return_json = return_stats_schema.dump(punt_return_data)
    receiving_stats_json = receiving_stats_schema.dump(receiving_stats)
    rushing_stats_json = rushing_stats_schema.dump(rushing_stats)
    # Stats leaders
    defensive_leaders_json = defensive_stats_schema.dump(defensive_leaders)
    kicking_leaders_json = kicking_stats_schema.dump(kicking_leaders)
    kick_return_leaders_json = return_stats_schema.dump(kick_return_leaders)
    passing_leaders_json = passing_stats_schema.dump(passing_leaders)
    punting_leaders_json = kicking_stats_schema.dump(punting_leaders)
    punt_return_leaders_json = return_stats_schema.dump(punt_return_leaders)
    receiving_leaders_json = receiving_stats_schema.dump(receiving_leaders)
    rushing_leaders_json = rushing_stats_schema.dump(rushing_leaders)

    response = {
        'all_stats': {
            'defense': defensive_stats_json,
            'kicking': kicking_stats_json,
            'kick_return': kick_return_stats_json,
            'passing': passing_stats_json,
            'punting': punting_stats_json,
            'punt_return': punt_return_json,
            'receiving': receiving_stats_json,
            'rushing': rushing_stats_json,
        },
        'stats_leaders': {
            'defense': defensive_leaders_json,
            'kicking': kicking_leaders_json,
            'kick_return': kick_return_leaders_json,
            'passing': passing_leaders_json,
            'punting': punting_leaders_json,
            'punt_return': punt_return_leaders_json,
            'receiving': receiving_leaders_json,
            'rushing': rushing_leaders_json
        }
    }

    return response
