from typing import List

from src.constants import session
from src.data_models.OffensiveStats import OffensiveStats
from src.data_models.PlayerInfo import PlayerInfo
from src.models.Player import PlayerDetails
from src.models.Stats import PassingStats, PlayerPassingStats
from src.responses.Stats import PlayerPassingStatsSchema
from src.responses.Players import PlayerSchema


passing_stat_schema = PlayerPassingStatsSchema()
passing_stats_schema = PlayerPassingStatsSchema(many=True)
player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)


def get_season_passing_stats(request):

    players = session.query(PlayerInfo, OffensiveStats)\
        .filter(OffensiveStats.player_id == PlayerInfo.id)\
        .all()

    converted_players: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in players]

    players_json = passing_stats_schema.dump(converted_players)
    
    response = {
        'players': players_json
    }
    
    return response


def get_season_passing_leaders_stats(request):

    players = session.query(PlayerInfo, OffensiveStats)\
        .filter(PlayerInfo.id == OffensiveStats.player_id)\
        .all()

    player_objects: List[PlayerPassingStats] = [_get_player_passing_stats(player) for player in players]

    pass_yards_leaders = sorted(player_objects, key=lambda p: p.passing_stats.pass_yards, reverse=True)[:10]
    pass_td_leaders = sorted(player_objects, key=lambda p: p.passing_stats.pass_tds, reverse=True)[:10]

    pass_yard_leaders_json = passing_stats_schema.dump(pass_yards_leaders)
    pass_td_leaders_json = passing_stats_schema.dump(pass_td_leaders)

    response = {
        'pass_yards': pass_yard_leaders_json,
        'pass_tds': pass_td_leaders_json
    }

    return response


def _get_player_passing_stats(player) -> PlayerPassingStats:

    player_info: PlayerDetails = player[0]
    player_passing_stats: PassingStats = player[1]

    player_details: PlayerDetails = PlayerDetails(
        id=player_info.id,
        team_id=player_info.team_id,
        first_name=player_info.first_name,
        last_name=player_info.last_name,
        height=player_info.height,
        weight=player_info.weight,
        jersey_number=player_info.jersey_number,
        player_year=player_info.player_year,
        redshirt=player_info.redshirt,
        position=player_info.position,
        hometown_desc=player_info.hometown_desc
    )

    passing_stats: PassingStats = PassingStats(
        pass_yards=player_passing_stats.pass_yards,
        longest_pass=player_passing_stats.longest_pass,
        year=player_passing_stats.year,
        pass_tds=player_passing_stats.pass_tds,
        games_played=player_passing_stats.games_played,
        completions=player_passing_stats.completions,
        ints=player_passing_stats.ints,
        pass_att=player_passing_stats.pass_att
    )

    player_passing_stats: PlayerPassingStats = PlayerPassingStats(
        player_details=player_details,
        passing_stats=passing_stats
    )

    return player_passing_stats
