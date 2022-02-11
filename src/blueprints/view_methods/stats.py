from typing import List

from src.constants import session
from src.data_models.OffensiveStats import OffensiveStats
from src.data_models.PlayerInfo import PlayerInfo
from src.data_models.WeekYear import WeekYear
from src.helpers import(
    _get_player_passing_stats
)
from src.models.Stats import(
    PlayerPassingStats
)
from src.responses.Stats import PlayerPassingStatsSchema


# Schemas to deserialize objects
passing_stat_schema = PlayerPassingStatsSchema()
passing_stats_schema = PlayerPassingStatsSchema(many=True)


def get_season_passing_stats(request):
    week_year: WeekYear = session.query(WeekYear).first()
    # Querying PlayerInfo first and OffensiveStats second will return 
    # a set or tuple to the players variable.
    players = session.query(PlayerInfo, OffensiveStats).filter(
            OffensiveStats.player_id == PlayerInfo.id,
            OffensiveStats.year == week_year.year
        ).all()

    converted_players: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in players]

    players_json = passing_stats_schema.dump(converted_players)
    
    response = {
        'players': players_json
    }
    
    return response


def get_season_passing_leaders_stats(request):
    # Query the year to filter out irrelevant years
    week_year: WeekYear = session.query(WeekYear).first()
    # Querying PlayerInfo first and OffensiveStats second will return 
    # a set or tuple to the players variable.
    players = session.query(PlayerInfo, OffensiveStats).filter(
            PlayerInfo.id == OffensiveStats.player_id,
            OffensiveStats.year == week_year.year
            ).all()

    # Convert players to PlayerPassingStats model so they can be sorted
    player_objects: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in players]
    # Sort players based on passing stat categories
    completions_leaders = sorted(player_objects, key=lambda p: p.passing_stats.completions, reverse=True)[:10]
    pass_att_leaders = sorted(player_objects, key=lambda p: p.passing_stats.pass_att, reverse=True)[:10]
    longest_pass_leaders = sorted(player_objects, key=lambda p: p.passing_stats.longest_pass, reverse=True)[:10]
    pass_yards_leaders = sorted(player_objects, key=lambda p: p.passing_stats.pass_yards, reverse=True)[:10]
    pass_td_leaders = sorted(player_objects, key=lambda p: p.passing_stats.pass_tds, reverse=True)[:10]
    int_leaders = sorted(player_objects, key=lambda p: p.passing_stats.ints, reverse=True)[:10]
    # Convert top ten lists into json
    completions_leaders_json = passing_stats_schema.dump(completions_leaders)
    pass_att_leaders_jason = passing_stat_schema.dump(pass_att_leaders)
    longest_pass_leaders_jason = passing_stat_schema.dump(longest_pass_leaders)
    pass_yard_leaders_json = passing_stats_schema.dump(pass_yards_leaders)
    pass_td_leaders_json = passing_stats_schema.dump(pass_td_leaders)
    int_leaders_json = passing_stats_schema.dump(int_leaders)


    response = {
        'completions': completions_leaders_json,
        'pass_att': pass_att_leaders_jason,
        'longest_pass': longest_pass_leaders_jason,
        'pass_yards': pass_yard_leaders_json,
        'pass_tds': pass_td_leaders_json,
        'interceptions': int_leaders_json
    }

    return response

