from typing import List

from sqlalchemy.sql.expression import desc

from src.constants import(
    defensive_stats_schema,
    kicking_stats_schema,
    passing_stat_schema,
    passing_stats_schema,
    receiving_stats_schema,
    return_stats_schema,
    rushing_stats_schema,
    session,
    team_schema,
    teams_schema,
)
from src.data_models.DefensiveStats import DefensiveStats
from src.data_models.OffensiveStats import OffensiveStats
from src.data_models.PlayerInfo import PlayerInfo
from src.data_models.TeamInfo import TeamInfo
from src.data_models.WeekYear import WeekYear
from src.helpers import (
    _get_player_defensive_stats,
    _get_player_details_and_abilities,
    _get_player_passing_stats,
    _get_player_receiving_stats,
    _get_player_rushing_stats,
    _get_team_info
)
from src.models.Player import Player
from src.models.Stats import (
    PlayerDefensiveStats,
    PlayerPassingStats,
    PlayerReceivingStats,
    PlayerRushingStats
)
from src.models.Team import Team
from src.responses.Teams import TeamSchema


def get_all_teams(request) -> TeamSchema:
    
    teams: List[TeamInfo] = session.query(TeamInfo).order_by(desc(TeamInfo.is_user)).all()
    teams_json = teams_schema.dump(teams)
    
    response = {
        'teams': teams_json
    }
    
    return response


def get_team_by_team_id(request, team_id) -> TeamSchema:
    
    team_info: TeamInfo = session.query(TeamInfo).where(TeamInfo.id == team_id).one()

    players: List[PlayerInfo] = session.query(PlayerInfo).where(
        PlayerInfo.team_id == team_id).all()


    team: Team = _get_team_info(team_info=team_info, players=players)

    response: TeamSchema = team_schema.dump(team)
    
    return response


def get_team_stats_leaders(request, team_id):
    # Query the year to filter out irrelevant years
    week_year: WeekYear = session.query(WeekYear).first()
    # Query the team to get the team_id
    team: TeamInfo = session.query(TeamInfo).where(TeamInfo.id == team_id).one()

    # Get defensive stats
    defense_stats = session.query(PlayerInfo, DefensiveStats).filter(
        PlayerInfo.id == DefensiveStats.player_id,
        PlayerInfo.team_id == team.id,
        DefensiveStats.year == week_year.year
    ).all()
    # Get offensive stats
    offense_stats = session.query(PlayerInfo, OffensiveStats).filter(
        PlayerInfo.id == OffensiveStats.player_id,
        PlayerInfo.team_id == team.id,
        OffensiveStats.year == week_year.year
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
