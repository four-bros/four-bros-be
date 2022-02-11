from typing import List

from src.constants import session
from src.data_models.OffensiveStats import OffensiveStats
from src.data_models.PlayerInfo import PlayerInfo
from src.data_models.WeekYear import WeekYear
from src.helpers import(
    _get_player_passing_stats,
    _get_player_receiving_stats,
    _get_player_rushing_stats
)
from src.models.Stats import(
    PlayerPassingStats,
    PlayerReceivingStats,
    PlayerRushingStats
)
from src.responses.Stats import(
    PlayerPassingStatsSchema,
    PlayerReceivingStatsSchema,
    PlayerRushingStatsSchema
)


# Schemas to deserialize objects
passing_stat_schema = PlayerPassingStatsSchema()
passing_stats_schema = PlayerPassingStatsSchema(many=True)
receiving_stat_schema = PlayerReceivingStatsSchema()
receiving_stats_schema = PlayerReceivingStatsSchema(many=True)
rushing_stat_schema = PlayerRushingStatsSchema()
rushing_stats_schema = PlayerRushingStatsSchema(many=True)


def get_season_passing_stats(request):
    # Query the year to filter out irrelevant years
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


def get_season_passing_stats_leaders(request):
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


def get_season_receiving_stats_leaders(request):
    # Query the year to filter out irrelevant years
    week_year: WeekYear = session.query(WeekYear).first()
    # Querying PlayerInfo first and OffensiveStats second will return 
    # a set or tuple to the players variable.
    players = session.query(PlayerInfo, OffensiveStats).filter(
            PlayerInfo.id == OffensiveStats.player_id,
            OffensiveStats.year == week_year.year
            ).all()
    # Convert players to PlayerReceivingStats model so they can be sorted
    player_objects: List[PlayerReceivingStats] = [_get_player_receiving_stats(player) for player in players]

    # Sort by category
    reception_leaders = sorted(player_objects, key=lambda p: p.receiving_stats.receptions, reverse=True)[0:10]
    rec_yards_leaders = sorted(player_objects, key=lambda p: p.receiving_stats.rec_yards, reverse=True)[0:10]
    rec_tds_leaders = sorted(player_objects, key=lambda p: p.receiving_stats.rec_tds, reverse=True)[0:10]
    yac_leaders = sorted(player_objects, key=lambda p: p.receiving_stats.yac, reverse=True)[0:10]
    drops_leaders = sorted(player_objects, key=lambda p: p.receiving_stats.drops, reverse=True)[0:10]

    # Convert top ten lists to json
    reception_leaders_json = receiving_stats_schema.dump(reception_leaders)
    rec_yards_leaders_json = receiving_stats_schema.dump(rec_yards_leaders)
    rec_tds_leaders_json = receiving_stats_schema.dump(rec_tds_leaders)
    yac_leaders_json = receiving_stats_schema.dump(yac_leaders)
    drops_leaders_json = receiving_stats_schema.dump(drops_leaders)

    response = {
        'receptions': reception_leaders_json,
        'rec_yards': rec_yards_leaders_json,
        'rec_tds': rec_tds_leaders_json,
        'yac': yac_leaders_json,
        'drops': drops_leaders_json
    }

    return response


def get_season_rushing_stats_leaders(request):
    # Query the year to filter out irrelevant years
    week_year: WeekYear = session.query(WeekYear).first()
    # Querying PlayerInfo first and OffensiveStats second will return 
    # a set or tuple to the players variable.
    players = session.query(PlayerInfo, OffensiveStats).filter(
            PlayerInfo.id == OffensiveStats.player_id,
            OffensiveStats.year == week_year.year
            ).all()

    # Convert players to PlayerPassingStats model so they can be sorted
    player_objects: List[PlayerRushingStats] = [_get_player_rushing_stats(player) for player in players]

    # Sort
    rush_att_leaders = sorted(player_objects, key=lambda p: p.rushing_stats.rush_att, reverse=True)[:10]
    rush_yards_leaders = sorted(player_objects, key=lambda p: p.rushing_stats.rush_yards, reverse=True)[:10]
    ya_contact_leaders = sorted(player_objects, key=lambda p: p.rushing_stats.ya_contact, reverse=True)[:10]
    broke_tkls_leaders = sorted(player_objects, key=lambda p: p.rushing_stats.broke_tkls, reverse=True)[:10]
    fumbles_leaders = sorted(player_objects, key=lambda p: p.rushing_stats.fumbles, reverse=True)[:10]
    twenty_plus_yd_runs_leaders = sorted(player_objects, key=lambda p: p.rushing_stats.twenty_plus_yd_runs, reverse=True)[:10]
    # Convert top ten lists to json
    rush_att_leaders_json = rushing_stats_schema.dump(rush_att_leaders)
    rush_yards_leaders_json = rushing_stats_schema.dump(rush_yards_leaders)
    ya_contact_leaders_json = rushing_stats_schema.dump(ya_contact_leaders)
    broke_tkls_leaders_json = rushing_stats_schema.dump(broke_tkls_leaders)
    fumbles_leaders_json = rushing_stats_schema.dump(fumbles_leaders)
    twenty_plus_yd_runs_leaders_json = rushing_stats_schema.dump(twenty_plus_yd_runs_leaders)

    response = {
        'rush_att': rush_att_leaders_json,
        'rush_yards': rush_yards_leaders_json,
        'ya_contact': ya_contact_leaders_json,
        'broken_tackles': broke_tkls_leaders_json,
        'fumbles': fumbles_leaders_json,
        'twenty_plus_runs': twenty_plus_yd_runs_leaders_json
    }

    return response
