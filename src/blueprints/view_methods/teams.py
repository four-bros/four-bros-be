from typing import List
from sqlalchemy.sql.expression import desc

from src.constants import(
    defensive_stats_schema,
    passing_stats_schema,
    receiving_stats_schema,
    rushing_stats_schema,
    session,
    team_details_schema,
    team_schema
)
from src.data_models.DefensiveStatsData import DefensiveStatsData
from src.data_models.OffensiveStatsData import OffensiveStatsData
from src.data_models.PlayerInfoData import PlayerInfoData
from src.data_models.TeamInfoData import TeamInfoData
from src.data_models.TeamStatsData import TeamStatsData
from src.data_models.WeekYearData import WeekYearData
from src.utils.player_stats import (
    _get_player_defensive_stats,
    _get_player_passing_stats,
    _get_player_receiving_stats,
    _get_player_rushing_stats
)
from src.utils.team_stats import (
    _get_team_details,
    _get_team_roster,
    _get_team_stats
)
from src.models.Stats import (
    PlayerDefensiveStats,
    PlayerPassingStats,
    PlayerReceivingStats,
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


def get_team_stats_leaders(request, team_id):
    # Query the year to filter out irrelevant years
    week_year: WeekYearData = session.query(WeekYearData).first()
    # Query the team to get the team_id
    team: TeamInfoData = session.query(TeamInfoData).where(TeamInfoData.id == team_id).one()

    # Get defensive stats
    defense_stats = session.query(PlayerInfoData, DefensiveStatsData).filter(
        PlayerInfoData.id == DefensiveStatsData.player_id,
        PlayerInfoData.team_id == team.id,
        DefensiveStatsData.year == week_year.year
    ).all()
    # Get offensive stats
    offense_stats = session.query(PlayerInfoData, OffensiveStatsData).filter(
        PlayerInfoData.id == OffensiveStatsData.player_id,
        PlayerInfoData.team_id == team.id,
        OffensiveStatsData.year == week_year.year
        ).all()
    # Convert players to the appropriate models based on stat category
    converted_players_defense: List[PlayerDefensiveStats] = [_get_player_defensive_stats(player) for player in defense_stats]
    converted_players_passing: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in offense_stats]
    converted_players_receiving: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in offense_stats]
    converted_players_rushing: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in offense_stats]
    # Sort converted players based on stat category
    defensive_leaders = sorted(converted_players_defense, key=lambda p: p.defensive_stats.solo_tkls, reverse=True)[:3]
    passing_leaders = sorted(converted_players_passing, key=lambda p: p.passing_stats.pass_yards, reverse=True)[:3]
    receiving_leaders = sorted(converted_players_receiving, key=lambda p: p.receiving_stats.rec_yards, reverse=True)[:3]
    rushing_leaders = sorted(converted_players_rushing, key=lambda p: p.rushing_stats.rush_yards, reverse=True)[:3]
    # Convert players to json for response
    defensive_leaders_json = defensive_stats_schema.dump(defensive_leaders)
    passing_leaders_json = passing_stats_schema.dump(passing_leaders)
    receiving_leaders_json = receiving_stats_schema.dump(receiving_leaders)
    rushing_leaders_json = rushing_stats_schema.dump(rushing_leaders)

    response = {
    'defense_leaders': defensive_leaders_json,
    'passing_leaders': passing_leaders_json,
    'receiving_leaders': receiving_leaders_json,
    'rushing_leaders': rushing_leaders_json
}

    return response
